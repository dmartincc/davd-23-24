## Lectura de datos y creación de modelos de ML

# E1: Lectura y escritura de csv

- A. Lee el fichero de [airport.csv](https://github.com/tidyverse/nycflights13/blob/main/data-raw/airports.csv) a partir de una ruta relativa o absoluta.

- B. Exporta ese fichero en diferentes formatos (json, excel).

- C. Crea una función que pueda leer cualquiera de los tres formatos indicándole, al menos, la ruta del fichero.

# E2: Carga de fichero con variable categórica y crear modelo de clasificación

- A. Descarga de la librería sklearn el fichero de datos de load_breast_cancer.

- B. Pasa ese fichero a formato dataframe incluyendo el target

- C. Crea un modelo de clasificación usando la técnica que prefieras dentro de Sklearn.

- D. Evalúa el modelo.

# E3: Carga de fichero con variable numérica y crear modelo de regresión

- A. Descarga el fichero de datos load_diabetes de sklearn.

- B. Pásalo a formato dataframe.

- C. Crea un modelo de regresión usando la técnica que prefieras dentro de Sklearn.

- D. Evalúa el modelo.

# E4: Crear modelos de clusterización

- A. Descarga el fichero de datos Wine Recognition Dataset de sklearn.

- B. Crear varios modelos de clusterización (K-means, NearestNeighbort, DBSCAN, ...).

- C. Evalua los clusters de cada modelo.

- D. Visualiza los clusters de cada modelo.

- E. Crea modelos de clasificación a partir de los clusters.

# E5: Creación de un juego de datos sintéticos a partir de distribuciones estadísticas

El juego de datos se compondrá de las siguientes variables:

- Sexo: Categórica
- Peso: Numérica
- Estatura: Numérica
- BMI: Numérica

Suposiciones:

- El 49,0% del total de inscritos en el Padrón son hombres y el 51,0% mujeres.
- La estatura de los hombre sigue una distribución media de 179.3 y una desviación típica 7.0.
- La estatura de las mujeres sigue una distribución media de 176.3 y una desviación típica 6.6.
- El peso de los hombre sigue una distribución media de 78.9 y una desviación típica 11.8.
- El peso de las mujeres sigue una distribución media de 60.4 y una desviación típica 9.7.
- BMI = Peso / Estatura^2

- A. Crea 100.000 individuos y sus variables.

- B. Clusteriza sus BMIs y explora si existe una relación con:
Bajo peso = menos de 18.5. Peso normal = 18.5–24.9. Sobrepeso = 25–29.9. Obesidad = BMI de 30 ó mayor

- C. Crea un modelo de regresión que calcule el BMI.

- D. Crea un modelo de clasificación que indique si una persona tiene sobrepeso o no.


