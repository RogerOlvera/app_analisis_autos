# **Versión 1.1 app_analisis_anuncios_autos_usados**

## :bookmark_tabs: **Descripción del proyecto**

Se cuenta con una base de datos de anuncios de autos usados a la venta. Se solicita crear una aplicación tipo dashboard para analizar la información contenida en la base y facilitar la comparación entre los anuncios y los autos publicados.

## :dart: **Objetivo:** Crear una app interactiva que analice la información de los anuncios de venta de autos usados.

## :clipboard: **Funcionalidades de la app:**

* Año del auto más antiguo.
* Año del auto más reciente.
* Auto más caro.
* Tipos de autos.
* Colores disponibles.
* Precios.
* Millas de los autos.
* Dispersión de los autos y sus precios.
* Dispersión de tipo de combustible y precio de los autos.
* Relación color-precio por tipo de auto.
* Relación de año de modelo-precio por modelo de auto.

## :white_check_mark: **Link web de la aplicación:** https://app-analisis-autos.onrender.com

## :book: **Diccionario información:**

* Base de datos: car_data, base de datos que contiene la información de los anuncios de venta de autos usados.

* Columnas:

    * price: precio de los autos anunciados en dólar americano.
    * model_year: año del modelo del auto.
    * model: modelo del auto.
    * condition: condiciones generales en las que se encuentra el auto.
    * cylinders: número de cilindros del motor.
    * fuel: tipo de combustible.   
    * odometer: recuento de millas registradas en el odómetro.
    * transmisión: tipo de transmisión del motor.
    * type: tipo de auto.
    * paint_color: color de la pintura.
    * is_4wd: indica si el auto es tracción a 4 ruedas.
    * date_posted: fecha de la publicación del anuncio.
    * days_listed: conteo de días transcurridos desde la publicación del anuncio.

## :computer: **Librerías utilizadas**

:diamond_shape_with_a_dot_inside: pandas

:diamond_shape_with_a_dot_inside: plotly

:diamond_shape_with_a_dot_inside: streamlit

:diamond_shape_with_a_dot_inside: onrender

## :up: **Actualizaciones**

- Se mejora distribución del contenido.
- Se crean espacios entre secciones y botones
- Se centran títulos de secciones
- Se agrega gráfica de comparación de histogramas de modelos de autos
- Se agrega linea de créditos
