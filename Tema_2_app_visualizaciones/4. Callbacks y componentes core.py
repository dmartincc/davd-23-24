# Importamos las librerias mínimas necesarias
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import logging
from plotly.subplots import make_subplots

# Para este Dash, vamos a seleccionar un fichero de datos y realizar un dashboard descriptivo
# sobre un conjunto de datos

df = pd.read_csv("../Datos/StudentsPerformance.csv")

# Crear opciones para las razas
races = df["race/ethnicity"].unique().tolist()
races.sort()
options_dropdown_race = []
for race in races:
    options_dropdown_race.append({'label': race, 'value': race})

# Crear opciones para las asignaturas
subjects = ["math score", "reading score", "writing score"]
options_dropdown_subjects = []
for subject in subjects:
    options_dropdown_subjects.append({'label': subject.split()[0].capitalize(), 'value': subject})

# Crear opciones para las variables categóricas

cols_checklist = ["gender","race/ethnicity","parental level of education", "lunch", "test preparation course"]

options_checklist = []
for col in cols_checklist:
    options_checklist.append({'value': col, 'label': col})

app = dash.Dash()

#app.config.suppress_callback_exceptions = True

logging.getLogger('werkzeug').setLevel(logging.INFO)

app.layout = html.Div(
    children= [
        html.H1( # Primera fila
            children = [
                "Análisis descriptivo sobre la puntuación de los estudiantes"
            ],
        id = "titulo",
        style = {
            "text-align": "center",
            "text-decoration": "underline",
            "backgroundColor": "lightblue",
            "margin-bottom": "20px",
            "border-style": "outset",
            "border-color": "lightblue",
            "height": "50px"
        }
        ),

        html.H2( # Segunda fila
            children = [
                "1) Comparativa de notas entre asignaturas y tipo de etnia"
            ],
            id = "subtitulo1",
            style ={
                "text-align": "left",
                "display": "block"
            }
        ),

        html.Div( # Tercera fila
            children = [
                html.Div( # Bloque izquierdo
                    children = [
                        html.H3(
                            children = [
                                "Primer grupo a comparar"
                            ],
                            id = "primer_grupo",
                            style = {
                                "display": "block",
                                "text-align": "center"
                            }
                        ),
                        dcc.Dropdown(
                            options = options_dropdown_race,
                            placeholder = "Selecciona una raza",
                            id = "dropdown_race",
                            style = {
                                "display": "block",
                                "width": "300px",
                                "margin-left": "10px"
                            }
                        ),
                        dcc.Dropdown(
                            options = options_dropdown_subjects,
                            placeholder = "Selecciona una asignatura",
                            id = "dropdown_subject",
                            style = {
                                "display": "block",
                                "width": "300px",
                                "margin-left": "10px"
                            }
                        ),
                        dcc.Graph(
                            id = "dropdown_figure",
                            style = {
                                "display": "none"
                            }
                        )
                    ],
                    style = {
                        "width": "700px",
                        "height": "600px",
                        "display": "inline-block",
                        "border-style": "ridge",
                        "border-color": "black"
                    }, 
                ),

                html.Div( # Bloque derecho
                    children = [
                        html.H3(
                            children = [
                                "Segundo grupo a comparar"
                            ],
                            id = "segundo_grupo",
                            style = {
                                "display": "block",
                                "text-align": "center"
                            }
                        ),
                        dcc.Dropdown(
                            options = options_dropdown_race,
                            placeholder = "Selecciona una raza",
                            id = "dropdown_race_2",
                            style = {
                                "display": "block",
                                "width": "300px",
                                "margin-left": "10px"
                            }
                        ),
                        dcc.Dropdown(
                            options = options_dropdown_subjects,
                            placeholder = "Selecciona una asignatura",
                            id = "dropdown_subject_2",
                            style = {
                                "display": "block",
                                "width": "300px",
                                "margin-left": "10px"
                            }
                        ),
                        dcc.Graph(
                            id = "dropdown_figure_2",
                            style = {
                                "display": "none"
                            }
                        )
                    ],
                    style = {
                        "width": "700px",
                        "height": "600px",
                        "display": "inline-block",
                        "margin-left": "20px",
                        "border-style": "ridge",
                        "border-color": "black"
                    },
                ) 
            ]
        ),

        html.Div( # Cuarta fila
            children = [
                html.H2(
                    children = [
                        "2) Visualizar proporciones de variables categóricas"
                    ],
                    id = "titulo_cuarta_fila",
                    style ={
                        "text-align": "left",
                        "display": "block"
                    }
                ),

                html.Div(
                    children = [
                        dcc.Checklist(
                            options = options_checklist,
                            labelStyle = {
                                'display': 'inline-block',
                                'font-size': "18px",
                                'margin-right': "10px"
                            },
                            id = "checklist_cat",
                            style = {
                                "display": "inline-block",
                            }
                        ),
                        html.Button(
                            children = [
                                "Mostrar"
                            ],
                            id = "boton_cat",
                            title = "Mostrar",
                            n_clicks = 0,
                            style = {
                                'background-color': 'lightgrey',
                                'color': 'steelblue',
                                'height': '35px',
                                'width': '100px',
                                'margin-left': '50px',
                                'border-radius': "5px"
                            }
                        )
                    ],
                    style = {
                        "display": "block"
                    }
                ),
                dcc.Graph(
                    id = "pie_charts",
                    style = {
                        "display" : "none"
                    }
                )
            ],
            id = "cuarta_fila",
        )
    ],
    style = {
        "font-family": "Arial"
    }
)

@app.callback(
    Output("dropdown_figure", "figure"),
    Output("dropdown_figure", "style"),
    Input("dropdown_race", "value"),
    Input("dropdown_subject",'value')
)
def figure_dropdown(dropdown_race_value,dropdown_subject_value):

    subject_dict = {
        "math score": "Math",
        "reading score": "Reading",
        "writing score": "Writing"
    }

    if dropdown_race_value and dropdown_subject_value:
        fig = go.Figure() 
        fig.add_trace(
            go.Histogram(
                x = df[df["race/ethnicity"] == dropdown_race_value][dropdown_subject_value],
                xbins=dict(
                    start= 0,
                    end= 100,
                    size=5,
                ),
                marker_color = "firebrick"
            )
        )
        fig.update_layout(
            title = f"Notas obtenidas en la asignatura {subject_dict[dropdown_subject_value]} de la raza {dropdown_race_value}", 
            xaxis_title = "Puntuación", 
            yaxis_title = "Frecuencia", 
            bargap = 0.1
        )
        return (fig,{"display":"block"})
    else:
        return (go.Figure(data = [], layout = {}), {"display": "none"})

@app.callback(
    Output("dropdown_figure_2", "figure"),
    Output("dropdown_figure_2", "style"),
    Input("dropdown_race_2", "value"),
    Input("dropdown_subject_2",'value')
)
def figure_dropdown_2(dropdown_race_value,dropdown_subject_value):

    subject_dict = {
        "math score": "Math",
        "reading score": "Reading",
        "writing score": "Writing"
    }

    if dropdown_race_value and dropdown_subject_value:
        fig = go.Figure() 
        fig.add_trace(
            go.Histogram(
                x = df[df["race/ethnicity"] == dropdown_race_value][dropdown_subject_value],
                xbins=dict(
                    start= 0,
                    end= 100,
                    size=5,
                ),
                marker_color = "steelblue"
            )
        )
        fig.update_layout(
            title = f"Notas obtenidas en la asignatura {subject_dict[dropdown_subject_value]} de la raza {dropdown_race_value}", 
            xaxis_title = "Puntuación", 
            yaxis_title = "Frecuencia", 
            bargap = 0.1
        )
        return (fig,{"display":"block"})
    else:
        return (go.Figure(data = [], layout = {}), {"display": "none"})

@app.callback(
    Output("pie_charts", "figure"),
    Output("pie_charts", "style"),
    Input("boton_cat", "n_clicks"),
    State("checklist_cat", "value"),
)
def checklist_callback(n_clicks,checklist_value):
    print(checklist_value)

    if (checklist_value is None) or (checklist_value == []):
        return (go.Figure(data = [], layout = {}), {"display":"none"})
    else:
        print(checklist_value)
        fig = make_subplots(
            rows=1, 
            cols=len(checklist_value),
            specs = [[{'type':'domain'}]*len(checklist_value)]
        )

        for col in checklist_value:
            level_count = pd.DataFrame(df[col].value_counts()).reset_index()
            fig.add_trace(
                go.Pie(
                    labels = level_count[col],
                    values = level_count["count"],
                    textinfo = 'label+percent',
                    insidetextorientation = 'radial',
                    textposition = 'inside',
                    sort = False,
                    showlegend = False,
                    hole = 0.5,
                    name = col
                ),
                row = 1,
                col = checklist_value.index(col) + 1
            )
        
        fig.update_traces(textfont_size=12)
        return (fig,{"display": "block"})
        

if __name__ == '__main__':
    app.run_server()