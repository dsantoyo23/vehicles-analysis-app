# Análisis de Anuncios de Venta de Vehículos

## Descripción del proyecto

Esta aplicación web permite explorar de forma interactiva un conjunto de datos
de anuncios de venta de vehículos usados en Estados Unidos. El objetivo es
practicar tareas habituales de ingeniería de software para un perfil de
analista de datos: gestión de entornos virtuales, análisis exploratorio de
datos (EDA), limpieza de datos con criterio analítico, y despliegue de una
aplicación web en la nube.

## Funcionalidad

La aplicación, construida con **Streamlit**, permite:

- Visualizar un **histograma** de la distribución del kilometraje (`odometer`)
  de los vehículos anunciados.
- Visualizar un **gráfico de dispersión** que relaciona el precio (`price`)
  con el kilometraje (`odometer`) de cada vehículo, permitiendo observar la
  tendencia de depreciación del valor según el uso del vehículo.

Ambas visualizaciones se generan de forma interactiva mediante botones.

## Datos

El conjunto de datos (`vehicles_us.csv`) contiene anuncios de coches usados,
con información como precio, año del modelo, kilometraje, condición, tipo de
combustible, entre otros. Previo a la visualización, los datos pasan por un
proceso de limpieza:

- Imputación de valores ausentes en columnas numéricas (`model_year`,
  `cylinders`, `odometer`) usando la mediana agrupada por modelo de vehículo,
  respetando las diferencias estructurales entre distintos modelos.
- Tratamiento de la columna `is_4wd`, donde los valores ausentes representan
  implícitamente vehículos sin tracción 4x4.
- Eliminación de outliers identificados como errores de captura de datos
  (precios y kilometrajes inconsistentes con el resto del dataset).

El razonamiento detallado detrás de cada decisión de limpieza se documenta en
el notebook de análisis exploratorio.

## Despliegue

La aplicación está desplegada en Render y es accesible en:
https://vehicles-analysis-app.onrender.com/