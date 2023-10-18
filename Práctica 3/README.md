# Práctica 3 VC - Curso 2023/2024

En esta tercera práctica se proponen 3 nuevas tareas. Las dos primeras, están relacionadas con la **contabilización de monedas**, teniendo que identificar cuantas monedas se detectan en la imagen en la primera tarea, y contando la cantidad total de dinero que se muestra en la imagen en la segunda. Por último, se deberán emplear las herramientas usadas en las primeras tareas con el objetivo de realizar una clasificación, lo más próxima posible a la realidad, entre diferentes tipos de **microplásticos** (fragmentos, pellet y alquitrán).

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

## Tarea 1

**Enlace a la tarea**: [Tarea 1](Tarea%201.ipynb).

El código comienza importando las bibliotecas necesarias: cv2 para OpenCV, numpy para la manipulación de matrices y matplotlib.pyplot para la visualización de imágenes. Luego, se carga una imagen de monedas desde un archivo llamado 'monedas-objetos-1.jpg' y se convierte de BGR a RGB para su visualización. La imagen se muestra en una ventana utilizando matplotlib, lo que permite ver la imagen original.

A continuación, se convierte la imagen a escala de grises para facilitar el procesamiento. Se calcula el histograma de la imagen en escala de grises con 256 bins, lo que muestra la distribución de intensidades de píxeles en la imagen. Se crea una figura con dos subparcelas para mostrar la imagen en escala de grises y su histograma.

![Imagen 1](README%20Images/tarea1-histograma.png)

Se define un umbral (umbral = 115) y se realiza una umbralización binaria invertida en la imagen en escala de grises. Esto se hace para resaltar las monedas y otros objetos en la imagen. Se muestran la imagen original y la imagen umbralizada (invertida) en dos subparcelas.

![Imagen 2](README%20Images/tarea1-invertida.png)

Luego, se utilizan las funciones de OpenCV cv2.findContours para encontrar todos los contornos en la imagen umbralizada. Se utiliza nuevamente la función cv2.findContours con cv2.RETR_EXTERNAL para encontrar solo los contornos externos en la imagen. Los contornos externos se dibujan en la imagen original en verde.

Se inicia un contador para realizar un seguimiento del número de monedas. Se recorren los contornos externos y se verifica si se asemejan a un círculo. Si el contorno se asemeja a un círculo, se incrementa el contador de monedas. Se imprime en la consola el número total de monedas detectadas en la imagen original. Se muestra una imagen en la que los contornos externos se han rellenado.

![Imagen 3](README%20Images/tarea1-bordes1.png)

Posteriormente, se carga otra imagen de monedas desde un archivo llamado 'monedas-objetos-2.jpg' y se muestra en una ventana. La segunda imagen se convierte a escala de grises y se suavizan las altas frecuencias. Se utiliza la función cv2.HoughCircles para detectar círculos en la imagen procesada. Se imprime en la consola el número total de monedas detectadas en la segunda imagen.

Finalmente, se dibujan los círculos detectados en la imagen original y en una imagen negra, y se muestran ambas imágenes en una ventana.

![Imagen 4](README%20Images/tarea1-bordes2.png)

## Tarea 2

**Enlace a la tarea**: [Tarea 2](Tarea%202.ipynb).

Para la realización de esta tarea partiremos de la solución obtenida en la tarea anterior. El objetivo ahora, será contar el total de dinero que se visualiza en la imagen. En este caso, hemos decidido escoger una nueva imagen en la cual solo hayan monedas, y que, además, tenga varias repetidas con la finalidad de comprobar el correcto funcionamiento del programa para contar el dinero total. La imagen de la cual haremos uso será la siguiente:

![Monedas](Images/monedas-personal-1.jpg)

Acto seguido, se deberá aplicar un umbralizado a la imagen lo más preciso posible para conseguir que los contornos de las monedas sean fieles a los de la imagen original. Todos estos pasos son exactamente los mismos que fueron llevados a cabo en la tarea anterior.

Tras seleccionar el umbral idóneo, y aplicar las operaciones correspondientes para extraer los contornos de las monedas de la imagen umbralizada, se obtendrá el siguiente resultado: 

![Contornos Monedas](README%20Images/tarea2-contornos.jpg)

Esta imagen será clave a la hora de contabilizar el dinero total que aparece en la imagen, pues si hemos aplicado un buen umbralizado y una buena extracción de contornos, las proporciones entre monedas serán fieles a la realidad y se podrán distinguir unas de otras.

A continuación, definimos dos diccionarios. En el primero, se establece para cada clave (nombres de las monedas: 1cts, 2cts...) la proporción que presentan con respecto a la moneda de 1 euro. De esta manera, una vez se haya obtenido el diámetro de la moneda de 1 euro en la imagen, se podrá obtener el diámetro del resto de monedas de forma proporcional. El segundo diccionario simplemente asocia cada clave (nombres de las monedas) a el valor de las mismas (0.01, 0.50...).

![Diccionarios](README%20Images/tarea2-diccionarios.jpg)

Como es obvio, el siguiente paso será obtener el diámetro real de la moneda de 1 euro que aparece en la imagen. Para ello, aparecerá una ventana emergente en la que se nos permitirá seleccionar dicha moneda. La forma en la que funciona la selección de la moneda y la obtención del diámetro es sencilla:

- Configuración del evento de hacer *clic* para que ejecute la función correspondiente.
- Recorre todos los contornos de las monedas detectadas en los pasos anteriores.
- Calcula la distancia entre el punto en el que se hizo *clic* y el centro de la moneda de esa iteración.
- Si la distancia calculada es menor al radio de la moneda: se ha hecho *clic* en esa moneda.
- Se guarda el diámetro de la moneda en una variable.

Teniendo el diámetro de la moneda de 1 euro, se podrá calcular perfectamente el diámetro del resto de monedas.

Por último, se volverán a recorrer todos los contornos correspondientes a las monedas, y se obtendrá el diámetro de cada contorno. Se compara ese diámetro con los diámetros calculados en el paso anterior (se encuentran en un nuevo diccionario), y se selecciona la clave (nombre de la moneda) que tenga el valor de diámetro más parecido al del contorno que está siendo evaluado. Después de esto, solo quedará sumar en una variable el valor correspondiente a ese nombre de moneda (el cual puede ser encontrado en un diccionario que asocia nombres de moneda con valores).

Además de mostrar el dinero total que aparece en la imagen, hemos querido mostrar la imagen de las monedas original, pero indicando con texto cuál es el valor de cada una de las monedas presentes en ella con el objetivo de comprobar que el programa ha funcionado correctamente.

**Dinero Total = 5.08 €**

![Dinero Total](README%20Images/tarea2-dinero.jpg)

Por otra parte, tratamos de realizar el conteo de dinero presente en la imagen con monedas solapadas, lo cual supuso un gran problema por los siguientes motivos:

- **Pérdida de información**: Cuando las monedas se solapan, partes de ellas están ocultas por otras monedas. Esto significa que no se pueden ver completamente y, por lo tanto, no es posible medir con precisión su diámetro.

- **Ambigüedad**: La superposición de monedas crea ambigüedad en cuanto a cuántas monedas están involucradas y qué parte de cada moneda es visible.

- **Dificultad en la detección de contornos**: Identificar y seguir los contornos de las monedas se complica cuando están solapadas. Esto puede observarse en la siguiente imagen, en la cual se ve como no se detectan todos los contornos existentes, ya que no todos conforman círculos perfectos detectables mediante la transformada de Hough.  

![Monedas solapadas](README%20Images/tarea2-solapadas.jpg)

Para abordar este problema, se necesitarían técnicas de procesamiento de imágenes muy avanzadas, como la segmentación de instancias o la utilización de redes neuronales profundas, que pueden identificar y separar las monedas superpuestas. Incluso con técnicas avanzadas, la tarea sigue siendo desafiante y propensa a errores, y la precisión del conteo de dinero puede verse afectada por la complejidad de la superposición de monedas en la imagen.

## Tarea 3

**Enlace a la tarea**: [Tarea 3](Tarea%203.ipynb).

El propósito de esta última tarea consiste en crear un clasificador que permita identificar los tres tipos de **microplásticos** propuestos: los **Fragmentos**, los **Pellet** y el **Alquitrán**.

Para ello, el primer paso a seguir será cargar las tres imágenes correspondientes y convertirlas a imágenes en escala de grises, tal y como se muestra a continuación:

![Microplásticos Grises](README%20Images/tarea3-grises.jpg)

Acto seguido, se deberán aplicar los umbrales necesarios para conseguir una buena separación y distinción de los objetos con respecto al fondo sobre el que se encuentran. Para ello, se ha establecido un umbral fijo para los Fragmentos y para los Pellet, mientras que para el Alquitrán se ha usado **OTSU**.

![Microplásticos Umbralizados](README%20Images/tarea3-umbralizado.jpg)

Partiendo desde este punto, se procederá a la identificación de cada uno de los contornos presentes en las tres imágenes, clasificándolos como Fragmento, Pellet o Alquitrán. 

Para lograr este objetivo, se han calculado las características geométricas básicas de cada uno de los contornos, las cuales serán muy útiles a la hora de distinguir los diferentes microplásticos. Las características geométricas calculadas fueron las siguientes:

- Área del contorno.
- Perímetro.
- Alto y ancho del mínimo contenedor que contiene al contorno.
- Compacidad.
- Eje mayor y menor de la elipse que contiene el contorno.
- Relación de aspecto (ancho/alto).
- Relación área contenedor (área/relación de aspecto).

Mediante estas características geométricas, hemos sido capaces de clasificar cada uno de los contornos dentro de algunas de las clases posibles.

Por ejemplo, para clasificar un contorno como Pellet, se han de cumplir las dos siguientes condiciones:

- Compacidad < 15.9
- Relación de aspecto cercana a 1

La compacidad se entiende como la relación que existe entre el perímetro del contorno y el área que dicho contorno ocupa. Es decir, que si se trata de un contorno que es muy alargado (gran perímetro) pero que sin embargo abarca poco área, el valor de la compacidad de dicho contorno será alto. Lo contrario ocurre en aquellos contornos en los que el perímetro y el área están compensados (como suele ocurrir con formas circulares como los Pellet, donde la relación perímetro^2/área resulta en un valor bajo).

Por otro lado, la relación de aspecto nos ayuda a deducir si un contorno es circular o no. Normalmente, los círculos tienen el mismo ancho que alto, por eso mismo, si la relación de aspecto (ancho/altura) es muy cercana a 1, se podría intuir que la forma es circular.

En cuanto a la identificación de Fragmentos, hemos tenido en cuenta la relación de área con respecto al contenedor que contiene el contorno. En este caso, si el área del contenedor que contiene al contorno es muy grande (dado que el contorno interior es muy alargado por ejemplo) y el área del contorno es relativamente baja, el resultado que daría la relación *área_contorno/área_contenedor* sería muy baja. Como nos hemos dado cuenta que el valor de esta relación en los Fragmentos estaba por debajo del 0.65, hemos decidido poner la siguiente condición:

- Relación área del contorno y área del contenedor < 0.65

Además, hemos tenido que incluir una condición más, que permita diferenciar los Fragmentos del Alquitrán, pues hemos encontrado bastantes problemas a la hora de clasificar estos dos microplásticos. 

La condición en cuestión consiste en tener en cuenta la relación entre el eje mayor de la elipse que contiene al contorno y el eje menor. Esto se debe a que, en los Fragmentos, hemos detectado que el eje mayor suele ser bastante más grande que el eje menor (debido a que son más alargados), al contrario que en el Alquitrán, donde ambos ejes tienden a ser algo más parecidos. Por eso mismo, al aplicar esta relación (eje_menor/eje_mayor), los valores que se encuentren por debajo de 0.78 deberían corresponderse con Fragmentos, y todos aquellos que estén por encima y más cercanos a 1, deberían ser Alquitrán.

Todos aquellos contornos que no cumplan con las condiciones anteriores, serán clasificados como Alquitrán. En la siguiente imagen se puede observar la matriz de confusión obtenida.

![Matriz de Confusión](README%20Images/tarea3-matriz.jpg)


