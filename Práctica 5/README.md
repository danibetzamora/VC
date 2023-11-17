# Práctica 5 VC - Curso 2023/2024

A lo largo de esta carpeta se muestra el trabajo realizado para la quinta práctica de la asignatura de **Visión por Computador**. El objetivo principal de la práctica 5 consiste en desarrollar un prototipo de sistema que sea capaz de identificar la matrícula de un vehículo, ya sea desde una imagen o desde un vídeo. 

Como material de apoyo para llevar a cabo dicho propósito, se proporciona un modelo de detección de objetos, el cual nos servirá en primera instancia para detectar coches: **YOLOv8**. Y, por otra parte, para el reconocimiento de texto se da la posibilidad de trabajar con **pytesseract** o con **easyocr**.

En nuestro caso, hemos decidido llevar a cabo el reconocimiento de matrículas españolas a partir de imágenes. Para ello, hemos propuesto dos detectores de matrículas:

- **Primer detector**: En esta primera fase dividiremos el proceso de detección de matrículas en tres partes, pues, en primer lugar, trataremos de detectar coches en una imagen haciendo uso del modelo de **YOLOv8**. Una vez obtenidas las detecciones de coches, se llevará a cabo un procesamiento sobre la imagen del coche detectado para tratar de localizar formas rectangulares (correspondientes a matrículas). Por último, se aplicará OCR a la región obtenida con **pytesseract** para extraer el texto de la matrícula.
- **Segundo detector**: En este caso, entrenaremos nuestro propio detector basado en **YOLOv8**, el cual se encargará de identificar directamente las matrículas existentes en la imagen, para posteriormente aplicarle OCR.

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

## Detector 1

**Enlace al primer detector**: [Detector 1](Detector%201.ipynb).

En este detector, como bien se comentó al principio, se ha dividido el proceso en tres partes bien diferenciadas. En la primera de ellas, la idea era usar el detector de **YOLOv8** para identificar coches en la imagen. Una vez obtenido el "*box*" el cual contiene el coche presente en la imagen, se ha de realizar un procesamiento de la imagen envuelta por ese contenedor, para localizar y extraer la matrícula.

El procesamiento de imagen llevado a cabo para detectar y extraer zonas rectangulares (matrículas), dentro del *box* en el que se encuentra el coche, se divide en varios pasos:

1. En primer lugar, dividimos a la mitad la imagen correspondiente al *box* devuelto por YOLO, en el cual se encuentra el coche, y guardamos el resultado en una variable. Esto se hace porque se intuye que la matrícula del coche probablemente se encontrará en la parte inferior del *box* y, de esta manera, reduciremos considerablemente la dimensión de la imagen que procesaremos para detectar zonas rectangulares. Esto se logra de la siguiente manera:

		roi_bottom = car[int((y1_car + y2_car) / 2):int(y2_car), int(x1_car):int(x2_car)]

2. Acto seguido, convertiremos la región obtenida a una escala de grises, para posteriormente aplicar el detector de bordes *Canny*, el cual hemos usado en prácticas anteriores. En la siguiente imagen se puede observar el resultado obtenido con *Canny*:

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/canny.png">
</div>

<p>&nbsp;</p>

3. Una vez detectados los bordes con *Canny*, podremos hacer uso de la función `findContours` de **OpenCV** para extraer todos los contornos existentes. Al aplicar *Canny* antes, la extracción de contornos es mucho más eficaz, pudiendo extraer el contorno rectangular de la matrícula de forma clara y nítida. Una vez aplicada esta función, obtendremos el siguiente resultado, en el cual se puede observar que de todos los bordes detectados con *Canny* nos quedamos con los contornos principales de la imagen, entre los cuales se encuentra el contorno rectangular correspondiente a la matrícula:

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/contours.png">
</div>

<p>&nbsp;</p>

4. Ahora solo quedará recorrer todos los contornos detectados en un bucle y seleccionar aquellos que tengan una forma cuadrada o rectangular. En principio, un contorno rectangular tendrá 4 vértices, por lo que con las dos siguientes líneas de código podremos obtener el número de vértices del contorno y, en caso de que sean cuatro, será un contorno rectangular, lo cual nos da a entender que probablemente sea la matrícula.

		perimeter = cv2.arcLength(contour, True)
		edges_count = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

5. En caso de que el contorno tenga 4 vértices, se obtendrán las coordenadas *x* e *y*, y el ancho y el alto del rectángulo que encierra a dicho contorno. De esta manera, ya tendremos la coordenada donde está situada la matrícula, y el ancho y el alto del contenedor que la contiene. Ya solo quedaría guardar en una nueva variable la imagen de la matrícula, extrayéndola de la imagen original haciendo uso de las coordenadas que obtuvimos.

Una vez finalizado el procesamiento de la imagen para detectar la matrícula, podremos visualizar el resultado:

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/plate1.png">
</div>

<p>&nbsp;</p>

Ya solo quedaría aplicar un OCR a la región de la matrícula obtenida y mostrar por pantalla el texto extraído por **pytesseract** de esa imagen. La línea que se encarga de hacer uso de pytesseract es la siguiente:

	text = pytesseract.image_to_string(plate, config='--psm 8', output_type=Output.STRING)

Nosotros además, hemos declarado un método el cual permite corregir el formato de texto devuelto por pytesseract, pues hay veces en las que el resultado del texto de la matrícula tiene ruido por delante o por detrás, así que básicamente tratamos de controlar que el formato del texto resultante sea el de una matrícula española: "*0000 AAA*".

## Detector 2

**Enlace al segundo detector**: [Detector 2](Detector%202.ipynb).

Para este segundo detector, el procedimiento es diferente al anterior, pues en lugar de procesar e identificar las matrículas de forma "manual", el objetivo es entrenar nuestro propio detector basado en YOLOv8.

Por eso mismo, el primer paso a tener en cuenta para comenzar con el entrenamiento es la anotación de imágenes. En nuestro caso, hemos hecho uso de un *dataset* procedente de la web de **Roboflow**, en el cual se proporcionan 200 imágenes de matrículas ya etiquetadas, lo cual nos simplificó el trabajo, pues el *dataset* ya contaba con las tres carpetas necesarias para el entrenamiento (*train*, *validation* y *test*), por lo que solo quedaba exportar dicho *dataset* en formato YOLOv8.

- **Enlace al _dataset_ usado**: [Roboflow Dataset](https://universe.roboflow.com/itrc/plate-detection-y5).

Una vez recopiladas las imágenes y las anotaciones, y habiendo estructurado el directorio de carpetas de la forma correcta, tuvimos que redactar nuestro archivo *.yaml*, el cual sería usado junto con el modelo de YOLOv8 para entrenar nuestro detector. El archivo *.yaml* en cuestión nos quedó de la siguiente manera:

```yaml
# PLATES DETECTION
train: C:/Users/Usuario/Documents/VC/FinalTrain/dataset/train/
val: C:/Users/Usuario/Documents/VC/FinalTrain/dataset/val/  
test: C:/Users/Usuario/Documents/VC/FinalTrain/dataset/test/  

# number of classes
nc: 1

# class names
names: [ 'plate' ]
```

Por lo que, teniendo la estructura de carpetas con imágenes etiquetadas en formato YOLOv8, el fichero *.yaml*, y el modelo *yolov8n.pt*, ya estábamos preparados para empezar el entrenamiento ejecutando el siguiente comando:

	yolo detect train model=yolov8n.pt data=plates.yaml imgsz=640 batch=4 device=CPU epochs=40

En la siguiente imagen podemos comprobar como, efectivamente, conseguimos terminar el entrenamiento correctamente. Además, también se muestra una imagen correspondiente a las gráficas resultantes del entrenamiento la cual es proporcionada por YOLO, y en la que se puede ver como el entrenamiento se ejecutó de forma satisfactoria, reduciendo la función de pérdida y aumentando la precisión de acierto en cada época.

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/entreno.jpg">
</div>

<p>&nbsp;</p>

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/results.png">
</div>

<p>&nbsp;</p>

Partiendo de este punto, ya solo queda hacer uso del modelo resultante del entrenamiento [plates_model.pt](Models/plates_model.pt) en nuestro código inicial. 

En el [detector 2](Detector%202.ipynb) básicamente lo que hacemos es aplicar el nuevo modelo de detección de matrículas, y una vez obtenido el *box* que contiene la matrícula y sus respectivos parámetros y coordenadas, ya podemos extraer la imagen de la matrícula de la imagen original y aplicarle OCR con **pytesseract**. En la siguiente imagen se puede ver el resultado obtenido con nuestro propio modelo:


<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/plate2.png">
</div>

<p>&nbsp;</p>