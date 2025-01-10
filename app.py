# Importar librerias

"""App de análisis de anuncios de venta de autos usados. Proyecto Sprint 7."""

import streamlit as st
import pandas as pd
import plotly.express as px


# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Tratamiento datos ausentes de la columna 'paint_color' para posterior uso

car_data['paint_color'] = car_data['paint_color'].fillna('unknown')

# Crear el header

st.header('Información de autos usados a la venta')

# Muestra información general

st.write('Año del auto más antiguo:', car_data['model_year'].min())
st.write('Año del auto más reciente:', car_data['model_year'].max())
st.write('Auto más caro (usd): $', car_data['price'].max())

# Crear boton para construir histograma de tipo de autos

boton_hist_tipo = st.button('Tipos de autos')  # crear un botón

if boton_hist_tipo:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Tipos de autos')

    # crear un histograma
    fig_hist_tipo = px.histogram(car_data, x="type")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_tipo, use_container_width=True)

# Crear boton para construir histograma por colores

boton_hist_color = st.button('Colores disponibles')  # crear un botón

if boton_hist_color:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Colores disponibles')

    # crear un histograma
    fig_hist_color = px.histogram(car_data, x="paint_color")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_color, use_container_width=True)

# Crear boton para construir histograma de precio

boton_hist_precios = st.button('Precios autos anunciados')  # crear un botón

if boton_hist_precios:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Precios autos anunciados')

    # crear un histograma
    fig_hist_precios = px.histogram(car_data, x="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_precios, use_container_width=True)

# Crear boton para construir histograma de millas

boton_hist_millas = st.button('Millas de los autos')  # crear un botón

if boton_hist_millas:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Millas de los autos')

    # crear un histograma
    fig_hist_millas = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_millas, use_container_width=True)

# Crear botón para construir gráfico de dispersión

boton_disp_tipo_precio = st.button("Dispersión tipo de autos y sus precios")  # Crear botón

if boton_disp_tipo_precio:  # al hacer clic en el botón
    # escribir mensaje
    st.write('Dispersión tipo autos y sus precios')

    # gráfico de dispersión
    fig_disp_tipo_precio = px.scatter(car_data, x='type', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp_tipo_precio, use_container_width=True)

# Crear botón para construir gráfico de dispersión

boton_disp_fuel_precio = st.button("Dispersión tipo de combustible y precio de los autos")

if boton_disp_fuel_precio:  # al hacer clic en el botón
    # escribir mensaje
    st.write('Dispersión tipo de combustible y precio de los autos')

    # gráfico de dispersión
    fig_disp_fuel_precio = px.scatter(car_data, x='fuel', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp_fuel_precio, use_container_width=True)

# Gráfica de tipo de auto, color con checkboxes

st.write('Selecciona el tipo de auto deseado para ver la relación color - precio.')

tipos = car_data['type'].unique()  # Tipos de autos

tipos_seleccionados =[]  # Lista vacia para los tipos seleccionados

for tipo in tipos:    # Selección de tipos
    if st.checkbox(tipo):
        tipos_seleccionados.append(tipo)

if tipos_seleccionados:   # Filtrar datos de acuerdo a la selección
    filtered_data = car_data[car_data['type'].isin(tipos_seleccionados)]

    # Crea la gráfica de dispersión
    fig_tipos = px.scatter(filtered_data, x = 'paint_color', y = 'price')    
    fig_tipos.update_layout(title="Relación color-precio por tipo de auto")
    st.plotly_chart(fig_tipos, use_container_width=True)

else:
    st.write('Selecciona al menos un tipo de auto')

# Gráfica de relación auto-precio-año

st.write('Selecciona el auto deseado para ver la relación año - precio.')

auto = car_data['model'].unique()  # Tipos de autos

auto_seleccionado = st.selectbox('Selecciona un modelo de auto:', auto)  # Lista desplegable

filtered_data_auto = car_data[car_data['model'] == auto_seleccionado]

# Crea la gráfica de dispersión
fig_auto = px.scatter(filtered_data_auto, x='model_year', y='price')
fig_auto.update_layout(title="Relación año y precio por auto")
st.plotly_chart(fig_auto, use_container_width=True)

st.write('Información general:\n\n', car_data)  # Mostrar la información del dataframe
