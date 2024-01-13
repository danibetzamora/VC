# Proyecto Final VC - Curso 2023/2024

En este repositorio presentamos el **Proyecto Final** que hemos elaborado para la asignatura de "Visión por Computador". Básicamente, nuestra propuesta para este último proyecto consiste en combinar la **detección de manos** con la **creación musical**. Por eso mismo, a continuación expondremos dos programas que, aunque se muestren por separado, en el futuro trabajarán de forma conjunta (pues las funcionalidades de ambos están muy relacionadas).

El primero de ellos consiste en un **Piano Virtual**, el cual permite a los usuarios tocar las teclas que aparecen en pantalla gracias a la detección de las manos. Y, por otro lado, el segundo programa se trata de un **Mezclador de Sonidos**, en el cual se podrá controlar la reproducción y mezcla de sonidos mediante gestos manuales. 
  
Nuestro objetivo principal es ofrecer a los usuarios una serie de programas que les permitan sacar el máximo provecho a su creatividad y, por supuesto, ofrecer la oportunidad a aquellos con pocos conocimientos y experiencia musical de adentrarse en la creación de música. Además, buscamos hacer que el proceso de creación musical sea más inmersivo e interactivo para ellos, permitiendo que la expresión artística a través de la música sea accesible y emocionante para todos.

Para lograr todo esto, hemos hecho uso de dos tecnologías claves para la detección de manos: **CV Zone** y **MediaPipe**. En nuestro caso, hemos decidido usar ambas herramientas, ya que otro de los objetivos que nos propusimos fue el de expandir nuestros conocimientos acerca de la detección de manos y las tecnologías disponibles para llevar a cabo dicha función.

A continuación, presentaremos con un poco más de detalle ambos programas.

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

## Piano Virtual

**Enlace al primer programa**: [Piano Virtual](virtual_piano.ipynb).

El propósito fundamental de este programa consiste en ofrecer a los usuarios la capacidad de interpretar y guardar sus propias melodías mediante un piano virtual interactivo. Concretamente, la interfaz permite una experiencia musical accesible, donde el usuario, por medio de ambas manos, podrá ir tocando las teclas del piano y escuchar, en tiempo real, las notas generadas en respuesta a sus acciones.

Para la detección de manos que se aplica en este programa, se ha decidido usar **CV Zone**. La decisión de usar esta herramienta en este primer programa radica en su simplicidad de uso. Además, este programa necesita información muy directa y sencilla acerca de las manos, como por ejemplo la posición en la pantalla, lo que da lugar a que CV Zone sea la tecnología perfecta para evitar sobrecargar la ejecución y que la gestión y el uso de los recursos sea mucho más eficiente.

Por otra parte, el correcto funcionamiento de este programa depende de las siguientes funciones, las cuales realizan las acciones principales del mismo (reproducir tecla, guardar secuencia, resetear secuencia, y dibujar teclado):

- **playkeys(button)**: Se encarga de asignar el archivo .wav de la nota con la tecla pulsada y apuntar la letra en una lista estableciendo su orden. También controla las posibles irregularidades al poder tocarse más de una vez la tecla por fallas en la detección de manos. 

- **save_sequence()**: Se encarga de crear un archivo .wav con la melodía compuesta por el usuario concatenando todos los sonidos de la lista de la secuencia, pudiendo crear más de una melodía por ejecución siempre que esta al menos una tecla guardada en la secuencia. 

- **reset_sequence()**: Una vez se haya guardado la melodía, para permitir seguir componiendo más melodía se resetea la secuencia de notas anteriormente pulsadas. 

- **drawAll()**: Se encarga de dibujar todas las teclas y el botón de guardar al igual que de un rectángulo negro detrás de las teclas blancas para simular la apariencia de un piano.

Por último, tenemos el bucle principal del programa. En este, durante toda la ejecución, se está constantemente comprobando la detección de las manos del usuario y actualizando el color de las teclas que no se han pulsado. 

En caso de detectarse una mano, si el dedo índice coincide con la posición de algunas de las teclas, esta cambiará su color a verde hasta que se levante el dedo, y se llamará a la función *playkeys*. Además, se cambiará la propiedad de *isPressed* de la clase *Button* a true. Se hace lo mismo con el botón *Save*, solo que en caso de ser pulsado se llamará a las funciones *save_sequence* y *reset_sequence* respectivamente.

Finalmente, se llama a la función *drawAll* para mostrar en cada frame (la captura de la imagen de la cámara) los elementos dibujados. 

A continuación, se mostrará una imagen del Piano Virtual en ejecución:

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/piano.jpg">
</div>

<p>&nbsp;</p>

## Mezclador de Sonidos

**Enlace al segundo programa**: [Mezclador de Sonidos](sound_mixer.ipynb).

En este caso, el mezclador de sonidos es una herramienta para que los usuarios experimenten con la creación musical de una manera intuitiva y envolvente. Por eso mismo, la interfaz presenta cuatro esquinas, cada una asociada a un sonido único. Al colocar la mano abierta en una esquina específica, se inicia la reproducción del sonido correspondiente. Y, para detener la reproducción, simplemente se requiere cerrar la mano o formar un puño en la misma esquina. 

Además, el programa ofrece la capacidad de cambiar entre diferentes géneros musicales de manera sencilla y expresiva. Para ello, el usuario puede indicar el género deseado mostrando un número de dedos con la mano frente a la cámara: un dedo para el primer género, dos para el segundo, y tres para el tercero.

Para la detección de manos aplicada a este programa, se ha hecho uso de **MediaPipe**. Básicamente, esto se debe a que en el primer programa se hizo uso de CV Zone y, en este segundo programa, quisimos hacer uso de una tecnología distinta de detección de manos para expandir nuestros conocimientos en este campo. 

Por supuesto, esto nos permitió hacer una comparación entre ambas herramientas, lo cual nos llevó a la conclusión de que CV Zone parecía funcionar de una manera mucho más eficiente, llegando a realizar la detección de manos de una forma más fluida y precisa. Sin embargo, a pesar de eso, quisimos continuar haciendo uso de MediaPipe, pues se trata de una herramienta muy potente y que nos proporciona una detección de manos muy aceptable.

Lo primero de todo, fue conseguir hacer que la detección de manos con MediaPipe se hiciese correctamente, pudiendo diferenciar entre los distintos gestos que más adelante pretendíamos usar en el mezclador. Por eso mismo, a través de las dos siguientes imágenes, vemos como se logró una correcta diferenciación entre los dos gestos principales del programa "Mano Abierta" u "Open" (para reproducir un sonido), y "Mano Cerrada" o "Closed" (para parar un sonido). 

Destacar que la diferenciación entre ambos gestos se logró calculando las coordenadas de posición de los *landmarks* superiores de cada uno de los dedos, y las coordenadas del *landmark* de la base de la mano, para posteriormente calcular la distancia Euclídea entre ellas (estando la mano abierta en caso de que la distancia superase un umbral prefijado, y cerrada en caso contrario).


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mediapipe1.jpg">
</div>

<p>&nbsp;</p>


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mediapipe2.jpg">
</div>

<p>&nbsp;</p>

Por otro lado, tuvimos que establecer la diferenciación de los gestos de "1", "2" y "3" con los dedos de la mano, para poder controlar la elección de géneros en el mezclador. En este caso, el procedimiento fue el mismo, realizar el cálculo de la distancia Euclídea y ver cuantos dedos estaban por encima del umbral establecido y cuantos no. En la siguiente imagen se muestra el resultado de esto:


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mediapipe3.jpg">
</div>

<p>&nbsp;</p>


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mediapipe4.jpg">
</div>

<p>&nbsp;</p>



<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mediapipe5.jpg">
</div>

<p>&nbsp;</p>

Por último, una vez éramos capaces de diferenciar entre los distintos gestos, solo nos quedaba desarrollar el programa que se encargaría de reproducir y parar los sonidos dependiendo de los gestos realizados. Para ello, hicimos uso de **PyGame**, una librería que nos permitía establecer canales de sonido y reproducirlos de una manera muy sencilla.

Por otro lado, se implementaron dos funciones básicas. La función **detect_hand_position(image)**, para obtener las coordenadas de la posición de la mano a través de MediaPipe. Y el método **detect_gesture(image)**, para reconocer en todo momento que gesto se está realizando por parte del usuario. 

Finalmente, en el bucle principal del programa, se realiza un continuo procesamiento de cada fotograma capturado por la cámara. Posteriormente, se corrige la inversión horizontal del fotograma utilizando `cv2.flip`, ya que la cámara suele capturar la imagen de manera invertida. 

A continuación, se crea una imagen compatible con MediaPipe a partir del fotograma procesado. Se efectúa la detección de la posición de la mano mediante la función *detect_hand_position*, proporcionando las coordenadas (x, y) de la mano en la imagen. Simultáneamente, se realiza la detección del gesto de la mano con la función *detect_gesture*, determinando si la mano está abierta, cerrada o realizando un gesto específico. 

En el caso de gestos específicos ("1", "2", "3"), se actualiza la carpeta actual de sonidos, se cargan nuevos sonidos y se detiene la reproducción en todos los canales de sonido. Luego, se procede a reproducir o detener sonidos en los canales específicos dependiendo de la posición y el gesto de la mano en relación con el fotograma.

En las imágenes siguientes, se muestra el programa en cuestión en ejecución:


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mixer1.jpg">
</div>

<p>&nbsp;</p>


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mixer2.jpg">
</div>

<p>&nbsp;</p>


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/mixer3.jpg">
</div>

<p>&nbsp;</p>

