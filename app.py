import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos (ruta sin '../' porque app.py está en la raíz)
car_data = pd.read_csv('vehicles_us.csv')

# Limpieza de datos (misma lógica validada en el notebook EDA.ipynb)
car_data['model_year'] = car_data.groupby('model')['model_year'].transform(
    lambda x: x.fillna(x.median())
)
car_data['cylinders'] = car_data.groupby('model')['cylinders'].transform(
    lambda x: x.fillna(x.median())
)
car_data['odometer'] = car_data.groupby('model')['odometer'].transform(
    lambda x: x.fillna(x.median())
)

# Respaldo: rellenar cualquier NaN residual con la mediana global
# (ocurre cuando un modelo específico no tiene NINGÚN valor reportado en esa columna)
for col in ['model_year', 'cylinders', 'odometer']:
    car_data[col] = car_data[col].fillna(car_data[col].median())

car_data['paint_color'] = car_data['paint_color'].fillna('unknown')
car_data['is_4wd'] = car_data['is_4wd'].fillna(0)

# Remover outliers identificados en el EDA
car_data = car_data[car_data['price'] <= 200000]
car_data = car_data[~((car_data['model'] == 'chevrolet corvette') & (car_data['odometer'] > 500000))]

# Encabezado principal
st.header('Análisis exploratorio de anuncios de venta de vehículos')

# Botón para el histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Distribución del kilometraje de los vehículos')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, width='stretch')

# Botón para el scatter plot
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Relación entre precio y kilometraje')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, width='stretch')