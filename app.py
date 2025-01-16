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

st.empty()
st.empty()
st.empty()

# Muestra información general

st.write('Año del auto más antiguo:', int(car_data['model_year'].min()))
st.empty()
st.write('Año del auto más reciente:', int(car_data['model_year'].max()))
st.empty()
st.write('Auto más caro (usd): $', car_data['price'].max())

st.empty()
st.empty()
st.empty()

# Titulo para la sección de botones de gráficos

# Mostrar mensaje
st.markdown(
    """
    <style>
        .st-b {
            text-align: center;
        }
    </style>
    <p class="st-b">Selecciona una opción para visualizar la información de los autos usados a la venta.</p>
    """, unsafe_allow_html=True)

st.empty()
st.empty()

# Crear boton para construir histograma de tipo de autos

boton_hist_tipo = st.button('Tipos de autos')  # crear un botón

if boton_hist_tipo:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Tipos de autos')

    # crear un histograma
    fig_hist_tipo = px.histogram(car_data, x="type", color_discrete_sequence=['lightblue'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_tipo, use_container_width=True)

st.empty()

# Crear boton para construir histograma por colores

boton_hist_color = st.button('Colores disponibles')  # crear un botón

if boton_hist_color:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Colores disponibles')

    # crear un histograma
    fig_hist_color = px.histogram(car_data, x="paint_color", color_discrete_sequence=['lightgreen'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_color, use_container_width=True)

st.empty()

# Crear boton para construir histograma de precio

boton_hist_precios = st.button('Precios autos anunciados')  # crear un botón

if boton_hist_precios:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Precios autos anunciados')

    # crear un histograma
    fig_hist_precios = px.histogram(car_data, x="price", color_discrete_sequence=['yellow'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_precios, use_container_width=True)

st.empty()

# Crear boton para construir histograma de millas

boton_hist_millas = st.button('Millas de los autos')  # crear un botón

if boton_hist_millas:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Millas de los autos')

    # crear un histograma
    fig_hist_millas = px.histogram(car_data, x="odometer", color_discrete_sequence=['gray'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist_millas, use_container_width=True)

st.empty()

# Crear botón para construir gráfico de dispersión

boton_disp_tipo_precio = st.button("Dispersión tipo de autos y sus precios")  # Crear botón

if boton_disp_tipo_precio:  # al hacer clic en el botón
    # escribir mensaje
    st.write('Dispersión tipo autos y sus precios')

    # gráfico de dispersión
    fig_disp_tipo_precio = px.scatter(
        car_data, x='type', y='price', color_discrete_sequence=['blue'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp_tipo_precio, use_container_width=True)

st.empty()

# Crear botón para construir gráfico de dispersión

boton_disp_fuel_precio = st.button("Dispersión tipo de combustible y precio de los autos")

if boton_disp_fuel_precio:  # al hacer clic en el botón
    # escribir mensaje
    st.write('Dispersión tipo de combustible y precio de los autos')

    # gráfico de dispersión
    fig_disp_fuel_precio = px.scatter(car_data, x = 'fuel', y = 'price', color_discrete_sequence=['green'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp_fuel_precio, use_container_width=True)

st.empty()
st.empty()

# Gráfica de tipo de auto, color con checkboxes

# Mostrar mensaje
st.markdown(
    """
    <style>
        .st-b {
            text-align: center;
        }
    </style>
    <p class="st-b">Selecciona el tipo de auto deseado para ver la relación color - precio.</p>
    """, unsafe_allow_html=True)

tipos = car_data['type'].unique()  # Tipos de autos

tipos_seleccionados =[]  # Lista vacia para los tipos seleccionados

for tipo in tipos:    # Selección de tipos
    if st.checkbox(tipo):
        tipos_seleccionados.append(tipo)

if tipos_seleccionados:   # Filtrar datos de acuerdo a la selección
    filtered_data = car_data[car_data['type'].isin(tipos_seleccionados)]

    # Crea la gráfica de dispersión
    fig_tipos = px.scatter(filtered_data, x = 'paint_color', y = 'price', color_discrete_sequence=['orange'])    
    fig_tipos.update_layout(title="Relación color-precio por tipo de auto")
    st.plotly_chart(fig_tipos, use_container_width=True)

else:
    st.write('Selecciona al menos un tipo de auto')

st.empty()
st.empty()
st.empty()

# Gráfica de relación auto-precio-año

st.markdown(
    """
    <style>
        .st-b {
            text-align: center;
        }
    </style>
    <p class="st-b">Selecciona el auto deseado para ver la relación año - precio.</p>
    """, unsafe_allow_html=True)

auto = car_data['model'].unique()  # Tipos de autos

auto_seleccionado = st.selectbox('Selecciona un modelo de auto:', auto)  # Lista desplegable

filtered_data_auto = car_data[car_data['model'] == auto_seleccionado]

# Crea la gráfica de dispersión
fig_auto = px.scatter(filtered_data_auto, x='model_year', y='price', color_discrete_sequence=['purple'])
fig_auto.update_layout(title="Relación año y precio por auto")
st.plotly_chart(fig_auto, use_container_width=True)

st.empty()
st.empty()
st.empty()

# Gráfica de comparación de autos

# Mostrar mensaje

st.markdown(
    """
    <style>
        .st-b {
            text-align: center;
        }
    </style>
    <p class="st-b">Compara precios de autos por año.</p>
    """, unsafe_allow_html=True)


# Crear un filtro para seleccionar el modelo del primer auto a comparar

auto_1 = st.selectbox(
    'Selecciona el modelo del primer auto a comparar', car_data['model'].unique())

st.empty()

# Crear un filtro para seleccionar el modelo de coche del segundo auto a comparar

auto_2 = st.selectbox(
    'Selecciona el modelo del segundo auto a comparar', car_data['model'].unique())


st.empty()

# Crear un botón para comparar los autos seleccionados

boton_comparar = st.button('Comparar autos')  # Crear botón

if boton_comparar:  # al hacer clic en el botón

    st.write('Compara autos')  # escribir mensaje

    # filtrar los datos para obtener los datos del primer auto

    auto1 = car_data[car_data['model'] == auto_1]

    # filtrar los datos para obtener los datos del segundo auto

    auto2 = car_data[car_data['model'] == auto_2]

    # gráfico primer auto

    fig_auto1 = px.histogram(auto1, x='model_year', y='price', color_discrete_sequence=['blue'], title=auto_1)

    # gráfico segundo auto

    fig_auto2 = px.histogram(auto2, x='model_year', y='price', color_discrete_sequence=['green'], title=auto_2)
   
    # mostrar un gráfico Plotly interactivo

    st.plotly_chart(fig_auto1, use_container_width=True)
    st.empty()
    st.plotly_chart(fig_auto2, use_container_width=True)

st.empty()
st.empty()

st.write('Información general:\n\n', car_data)  # Mostrar la información del dataframe

st.empty()
st.empty()
st.empty()

st.write('Créditos: Roger Olvera') # Mostrar créditos