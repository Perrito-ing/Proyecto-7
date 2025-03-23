import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página: esta línea debe ser la primera en el script
st.set_page_config(page_title="Mi Aplicación Streamlit")

st.title("Proyecto 7")

port = os.getenv('PORT', 8502)

# Cargar los datos
st.header("Dataframe")
car_data = pd.read_csv("https://raw.githubusercontent.com/Perrito-ing/Proyecto-7/refs/heads/main/vehicles_us.csv")
st.write(car_data)  # Muestra las primeras filas del CSV para ver si se carga bien

# Crear los botones
st.header("Histograma")
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Botón de histograma presionado')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


st.header("Gráfico de Dispersión")
plotly_button = st.button('Construir gráfico de dispersión')
if plotly_button:
    st.write('Botón de gráfico de dispersión presionado')
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)