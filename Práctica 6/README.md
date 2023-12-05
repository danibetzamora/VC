# Práctica 6 VC - Curso 2023/2024

Esta última práctica tiene como objetivo aplicar las herramientas vistas a lo largo de las dos últimas semanas, las cuales nos permiten trabajar de manera relativamente sencilla con la detección y el reconocimiento facial. Es por ello que hemos hecho dos propuestas distintas: la primera hará uso de la biblioteca `scikit-learn` para aplicar aprendizaje automático y ser capaces de identificar los rostros que aparecen en la webcam, mientras que, en la segunda, se hará uso de `DeepFace` para implementar un juego que pondrá a prueba las expresiones faciales del jugador. 

**Scikit-Learn** se ha convertido en un pilar fundamental para los profesionales del aprendizaje automático, facilitando la implementación de modelos desde problemas simples hasta tareas más complejas. Su diseño modular y su documentación detallada hacen que sea accesible tanto para principiantes como para expertos.

Mientras que, **DeepFace**, es un sistema de reconocimiento facial impulsado por redes neuronales profundas. En esta práctica, concretamente, haremos uso de las herramientas que nos proporciona DeepFace para predecir las expresiones faciales detectadas en un rostro.

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

## Propuesta 1

**Enlace a la primera propuesta**: [Identificador Facial](IdentificadorFacial.ipynb).

## Propuesta 2

**Enlace a la segunda propuesta**: [Juego de Expresiones con DeepFace](JuegoDeepFace.ipynb).

En esta segunda propuesta, la idea ha consistido en desarrollar un pequeño juego a través del cual el jugador pueda poner a prueba sus expresiones faciales. Básicamente, el jugador deberá intentar imitar las expresiones faciales que van saliendo en las imágenes flotantes, mientras que, DeepFace, tratará de predecir la expresión que está poniendo el jugador. En caso de que las expresiones de la imagen y del jugador a través de la webcam coincidan, se añadirá un punto al contador, en caso contrario, se contará como fallo y se pasará a la siguiente imagen.

Para desarrollar el juego se han tenido en cuenta los siguientes puntos:

- Se deberán almacenar las imágenes que se deseen en una carpeta, para que, posteriormente, sean cargadas en el juego y se vayan mostrando de una en una. Además, en el propio código se etiqueta cada imagen con la expresión a la que corresponde (a través de un diccionario de Python), para después hacer la comprobación de forma más sencilla.
- Se empezará la captura de la webcam y, cada 5 *frames*, se usará el método `extract_faces` de DeepFace para detectar la cara que aparece en el frame, y sus coordenadas (pues nos servirán más adelante en el juego para poner los comentarios sobre la cabeza, a modo de filtro).
- Una vez han pasado 100 *frames*, se aplica el método `analyze` de DeepFace para detectar la expresión que el jugador ha puesto en ese momento. Se dejan pasar 100 *frames* para que al jugador le de tiempo (1 segundo aproximadamente) de poner la expresión facial solicitada.
- Las imágenes irán cambiando después de informar al jugador de si ha acertado o ha fallado.
- Finalmente, aparecerá un pequeño texto sobre la cabeza del jugador (haciendo uso de las coordenadas proporcionadas por `extract_faces`) que indicará que el juego ha terminado, y que mostrará el resultado obtenido.

A continuación, se mostrarán algunas imágenes del juego:

- El jugador acierta la expresión.

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/acierto.jpg">
</div>

<p>&nbsp;</p>

- El jugador falla la expresión.

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/fallo.jpg">
</div>

<p>&nbsp;</p>

- Resultado final del juego.

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/resultado.jpg">
</div>

<p>&nbsp;</p>