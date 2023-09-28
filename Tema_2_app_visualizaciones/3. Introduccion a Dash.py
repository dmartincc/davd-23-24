# Importamos las librerias mínimas necesarias
import numpy as np
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

# A la hora de desarrollar una aplicación para visualizar datos tendremos que combinar 
# elementos de HTML y CSS con elementos propios de Dash. Lo primero que tendremos que 
# hacer siempre es inicializar una aplicación de Dash

app = dash.Dash()

# Una vez hemos inicializado la aplicacion, modificamos el diseño de la aplicacion

# IMPORTANTE: Hay que ser extremadamente ordenado con el código para que se entienda
# correctamente que se está haciendo en cada parte. Se recomienda un vistazo a la 
# libreria Black para formateo del código.

# Primer dashboard 
app.layout = html.Div(  # Creamos una componente que realice la primera división del dashboard
    children = [
        html.H1( # Primera fila
            children = [
                "Introducción a Dash"
            ],
            id = "titulo",
            style = {  # Aquí aplico todo lo que necesite de CSS
                "text-align": "center", # Alineo el texto al centro
                "color": "lightsteelblue", # Cambio el color de la fuente, se puede usar codigo hexagesimal
                "font-family": "Arial", # Cambio el tipo de fuente
                "backgroundColor": "darkslategray", # Cambio el color del fondo
                "text-decoration": "underline" # Subrayar el texto
            }
        ),
        html.Div( # Segunda fila 
            children = [
                html.H2(
                    children = [
                        "Esto es un subtítulo H2 "
                    ],
                    id = "primer_subtitulo",
                    style = {
                        "text-align": "left",
                        "color": "lightsteelblue",
                        "backgroundColor": "darkslategray",
                        "width": "250px", # Pongo una anchura máxima para limitar este componente
                        "display": "inline-block"

                    }
                ),
                html.P(
                    children = [
                        "Esto es un párrafo escrito a continuación en la misma linea que el título anterior"
                    ],
                    id = "componentes_css",
                    style = {
                        "font-family": "Arial",
                        "display": "inline-block",
                        "width": "600px",
                        "margin-left": "100px" # Modificar el margen, comentar diferencias entre padding-border-margin
                    }
                )
            ],
            id = "segunda_fila"
        ),
        html.Div(
            children = [
                dcc.Graph(
                    figure = go.Figure(
                        data = [
                            go.Bar(
                                x = ["Clase 1", "Clase 2", "Clase 3"],
                                y = [10,6,13],
                                marker_color = ["gold","darkorange","firebrick"],
                            )
                        ],
                        layout = go.Layout(
                            title = "Primer gráfico de prueba",
                            xaxis_title = "Clases",
                            yaxis_title = "Elementos",
                            width = 600,
                            height = 600
                        )
                    ),
                    id = "primera_figura",
                    style = {
                        "display": "block", # Diferenciar entre block, inline-block , inline
                        "margin-left": "25%",
                        "margin-right": "30%", # margin : auto
                    }
                )
            ],
            id = "tercera_fila"
        ),
        html.Div( # Cuarta fila
            children = [
                dcc.Graph(
                    figure = go.Figure(
                        data = [
                            go.Histogram(
                                x = np.random.normal(size = 1000),
                                marker_color = "steelblue",
                                name = "Histograma",
                                histnorm = "probability"
                            ),
                        ],
                        layout = go.Layout(
                            title = "Histograma de valores",
                            xaxis_title = "Valores de una normal de media 0 y std 1",
                            width = 600,
                            height = 600,
                            bargap = 0.1
                        )
                    ),
                    id = "segunda_figura",
                    style = {
                        "display": "inline-block",
                    }
                ),

                dcc.Graph(
                    figure = go.Figure(
                        data = [
                            go.Histogram(
                                x = np.random.gamma(shape = 1/2, scale = 1/2, size = 1000),
                                marker_color = "indigo",
                                name = "Histograma",
                                histnorm = "probability"
                            ),
                        ],
                        layout = go.Layout(
                            title = "Histograma de valores",
                            xaxis_title = "Valores de una gamma",
                            width = 600,
                            height = 600,
                            bargap = 0.1
                        )
                    ),
                    id = "tercera_figura",
                    style = {
                        "display": "inline-block"
                    }
                ),
            ],
            id = "cuarta_fila",
        )

    ],
    id = "primera_fila",
    style = {
        "margin-right": "125px",
        "margin-left": "125px",
        "margin-top": "100px",
        "border-style": "groove",
    } 
)

if __name__ == '__main__':
    app.run_server()

