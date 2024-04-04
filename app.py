import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # Leer los datos

st.title('ANUNCIOS DE AUTOS EN VENTA') # Titulo general
st.header('Visualizador de Datos') # Encabezado de Sección 1: Visualizar los Datos
st.dataframe(car_data)

st.header('Tipos de autos por manufacturador') # Encabezado de sección 2: Tipos de Autos por Manufacturador
bar_button = st.button('Construir Gráfico') # Crear un botón
if bar_button: # Al hacer clic en el botón
    st.write('Creación del gráfico para los anuncios de autos, agrupados por tipo y manufacturador')

    car_data_2 = car_data # Copia del DataFrame
    # Buscar unicamente en model, quitando el modelo, dejar solo creador y agregar la columna nueva a la copia (manufacturer)
    manufacturers = []
    for model in car_data['model']:
        manufacturers.append(model.split(' ')[0])
    car_data_2['manufacturer'] = manufacturers

    # Agrupar por manufacturador y tipo de auto. El nuevo DataFrame será representado en la gráfica
    counted = car_data_2.groupby(['manufacturer', 'type'], as_index=False).count()
    counted['count'] = counted['model']

    # Crear el gráfico
    fig = px.bar(counted, x="manufacturer", y="count", color="type") # , title="Tipos de Autos por Manufacturador"
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.header("Condición del auto vs. Año del auto")
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Histograma para observar las condiciones respecto al año de fabricación de los autos')
    # Crear y mostrar el histograma
    fig_2 = px.histogram(car_data, x="model_year", color="condition") # , title="Histograma de condición vs año del auto"
    st.plotly_chart(fig_2, use_container_width=True)

st.header("Kilometraje marcado vs Precio")
scatt_button = st.checkbox('Construir Gráfico de Dispersión')
if scatt_button:
    st.write('Gráfico de dispersión para observar la relación del kilometraje marcado en el odómetro y el precio de venta de los autos')
    # Crear y mostrar el gráfico de dispersión
    fig_3 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_3, use_container_width=True)