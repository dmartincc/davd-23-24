from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import transformers
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Modelo con un transformer de Hugging Face 
classifier = transformers.pipeline(
    'sentiment-analysis', model = "nlptown/bert-base-multilingual-uncased-sentiment")

# Agregar parametros para las reviews
reviews_args = reqparse.RequestParser()
reviews_args.add_argument("name", type=str, required=True)
reviews_args.add_argument("review", type=str, required=True)
reviews_args.add_argument("rating", type=int, required = False)

reviews = {}

def reviews_error(review_id):
    if review_id not in reviews:
        abort(404, message = "No existe la opinión que estás buscando")

class SentimentAnalysis(Resource):
    
    def get(self,review_id=0):
        if review_id != 0: 
            reviews_error(review_id)
            return reviews[review_id]
        else:
            return reviews

    def put(self, review_id):
        args = reviews_args.parse_args()
        reviews[review_id] = args
        text = reviews[review_id]["review"]
        sentiment = classifier(text)[0]
        reviews[review_id]['prediction'] = sentiment['label'].split()[0]
        reviews[review_id]['probability'] = sentiment['score']
        reviews[review_id]["timestamp"] = str(datetime.now())
        return reviews[review_id], 201

    def post(self, review_id):
        pass
    
    def delete(self, review_id):
        reviews_error(review_id)
        del reviews[review_id]
        return 'La review con id {} ha sido eliminada'.format(review_id), 204

api.add_resource(SentimentAnalysis, "/sentiment/<int:review_id>")

if __name__ == "__main__":
    app.run(debug = True)

