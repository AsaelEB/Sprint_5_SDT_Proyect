# Sprint_5_SDT_Proyect

TripleTen Sprint 5: Learning Software Development Tools.

Este proyecto, se hace con la finalidad de aprender a utilizar servicios web para despligue de análisis de datos usando la librería de Streamlit y el servicio de Render para el despliegue por medio de la web.

La aplicación que realicé, utiliza un dataset de anuncios de vehiculos en venta y contiene 4 secciones para análisis diferentes:

* La primera sección es una visualización de los datos que serán utilizados.
* La segunda sección contiene un botón que muestra un gráfico de barras apilado, con la cantidad de autos correspondientes a un mismo manufacturador y se apilan por el tipo de auto.
* La tercera sección contiene un botón que muestra un histograma, con la cantidad de autos por año del modelo, y permite elegir la condición en la que se encuentran.
* La cuarta sección contiene una casilla de verificación, la cual mostrará un gráfico de dispersión del kilometraje marcado en el odómetro con relación al precio de venta del auto.

- Sección 1: Únicamente permite visualizar el Dataset, no tiene operaciones adicionales.
- Sección 2: Al oprimir el botón (Construir Gráfico) se muestra el grafico de barras apiladas de la cantidad de autos para cada manufacturador, que permite elegir el tipo de auto que se observa para cada uno al presionar sobre el nombre en la leyenda derecha.
- Sección 3: Al presionar el botón (Construir Histograma) se muestra el histograma de la cantidad de autos por modelo y condición actual, en la parte derecha se puede seleccionar la condición para mostrar el histograma.
- Sección 4: Incluye una casilla de verificación que al seleccionarse mostrará el gráfico de dispersión con la relación entre el precio y el odómetro de los autos.

En las secciones 2 y 3 solamente puede estar activa una a la vez, y en la parte de la leyenda de los gráficos: Todos los elementos son mostrados por defecto. Al dar un click sobre el nombre el elemento de la lista dejará de estar seleccionado. Al dar doble clic sobre un nombre se aislará y ese será el único elemento que se muestre, posteriormente se pueden seguir seleccionando todos los demás que se requieran.

Espero que la aplicación se pueda entender y ejecutar correctamente. El link de la aplicación en render es: [https://sprint-5-sdt-proyect.onrender.com/](https://sprint-5-sdt-proyect.onrender.com/)