# Práctica 2 VC - Curso 2023/2024

Fichero destinado a la explicación de las tareas realizadas durante la **práctica 2**. 

Entre ellas, se destaca la aplicación de *Canny* e interpretación del histograma correspondiente al número de píxeles negros y blancos (tarea 1), uso del operador *Sobel* y ajuste de la escala de las imágenes (tarea 2), umbralizado de una imagen y uso de histogramas para la obtención del valor umbral (tarea 3), explicación teórica de alguna de las funciones vistas durante las prácticas (tarea 4), aplicación de técnicas vistas para el procesamiento de imágenes (tarea 5).

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

## Tarea 1

**Enlace a la tarea**: [Tarea 1](Tarea%201.ipynb).

En esta primera tarea se muestra, a modo de ejemplo, el conteo de píxeles **no nulos** (blancos) por columna de una imagen a la que se le ha aplicado *Canny* (detector de bordes multietapa). A través de un histograma, puede verse el número de píxeles blancos que se han contado en cada columna. Además, se puede apreciar cierta simetría en el histograma, lo cual es bastante lógico, debido a que la cara del mandril es "simétrica".

Sin embargo, como primera tarea de esta práctica, se propone realizar el conteo de píxeles blancos por filas. Para ello, se llevaron a cabo los siguientes pasos.

1. Modificación del parámetro correspondiente en la función `reduce` de **OpenCV**, pasando de 0 a 1, para que la suma de los valores pase a ser por filas en lugar de por columnas.
2. Pequeña modificación en la normalización de los valores de cada fila, ya que la lista en la que se guardan los valores a normalizar de cada una de las filas, ahora se trata de una lista que contiene listas por cada fila (mientras que en el conteo por columnas era una única lista con el valor de píxeles blancos en cada posición de esa lista).

Por último, se pide para esta tarea, que se identifique cual es el valor máximo de píxeles blancos por filas y por columnas, y que, además, se muestre el número de valores que superan el 95% del máximo.

Para realizar dicha tarea, se ha hecho uso de funciones propias de **NumPy**, las cuales permiten obtener el valor máximo de una lista, la posición en la que se encuentra dicho valor máximo y contar el número de valores que superan el 95% del máximo de la lista.

## Tarea 2

**Enlace a la tarea**: [Tarea 2](Tarea%202.ipynb).

En este caso, se aplica el operador de *Sobel* a una imagen, a partir de la cual se pide visualizar y comprender el contenido de dicha imagen con la escala ajustada y sin ajustar.

Para ello, en primer lugar suavizamos la imagen haciendo uso de `GaussianBlur`, para posteriormente aplicar Sobel en dirección vertical y horizontal (obteniendo el resultado final al combinarlos).

Por otro lado, cada una de las tres imágenes obtenidas al aplicar el operador de Sobel (bordes verticales, horizontales y combinados) fueron escaladas, de tal manera que los valores que contienen las imágenes se establezcan entre 0 y 255, dando lugar a una imagen en escala de grises pero con valores muy cercanos al negro y al blanco para resaltar los bordes.

Por último, mediante un bucle `for` se muestran las seis imágenes resultantes, pudiendo ver con claridad la diferencia entre ellas.

Además, se muestra el contenido de una imagen escalada y de otra sin escalar en forma de matriz. Viendo con claridad como la imagen a la que se le ha aplicado el operador Sobel y no se le ha ajustado la escala presenta valores negativos. Mientras que en la otra, al haber sido escalada, los valores están entre el 0 y el 255, pudiendo ver una clara detección de bordes en escala de grises muy parecida a la obtenida con Canny (aunque no tan binaria).

## Tarea 3

**Enlace a la tarea**: [Tarea 3](Tarea%203.ipynb).

Partiendo de la tarea anterior, en esta tercera parte se propone hacer uso de la imagen resultante de Sobel y aplicarle umbralizado. Para lo que primeramente será necesario que la imagen esté compuesta por valores entre 0 y 255, y convertida a 8 bits mediante la función de NumPy `np.uint8()`. 

Como resultado, se obtiene una imagen con una textura muy marcada y con tonos muy oscuros. Obviamente, la imagen está representada en una escala de grises, pero no se logran diferenciar del todo los bordes debido a que hay una dispersión muy grande de valores negros y blancos, lo que da lugar a una imagen muy oscura. Por eso mismo, se deberá umbralizar la imagen, para poder diferenciar los elementos principales de la imagen (edificación y árboles) del fondo de la misma.

Para ello, hemos decidido representar la imagen mediante un histograma, con el objetivo de ver de una forma más gráfica los valores que presenta la imagen y poder seleccionar un buen umbral. 

En el histograma se muestra un gran valle, que suele ser el indicador clave para seleccionar un umbral. Sin embargo, debido a que hay una gran presencia de valores oscuros en la imagen, hemos optado por establecer un valor umbral muy cercano al 0, consiguiendo de esta manera que aquellos valores por encima de él se establezcan en 255, pudiendo diferenciar con mayor claridad los elementos principales de la imagen.

Una vez aplicado el umbralizado, se puede observar que en la imagen inicial, la edificación, los árboles, y la escalera, están mucho más resaltados y se diferencian mucho más del fondo.

Por último, se pide realizar nuevamente el conteo de píxeles blancos por columnas y por filas, y calcular los máximos valores para cada una de ellas. 

En la gráfica que muestra el conteo de píxeles blancos en las columnas se puede apreciar con claridad la simetría de la imagen, ya que la imagen original es totalmente simétrica, por lo que presenta el mismo número de píxeles blancos en ambas mitades de la imagen.

Sin embargo, en el conteo por filas, se puede ver como las primeras filas presentan muy pocos píxeles blancos (dado que es el fondo), y en el resto de filas el número de píxeles claros va aumentando progresivamente.

Para finalizar, se muestra el valor máximo de píxeles blancos tanto para las filas como para las columnas y, además, se calcula el número de filas y de columnas que tienen un valor igual o mayor al 95% del máximo, remarcando, en cada caso, aquellas filas y columnas que cumplan esa condición mediante una línea roja.

#### Comparación de resultados de Canny y Sobel

La principal diferencia entre ambas técnicas, es que Sobel se utiliza para calcular el gradiente de la imagen, lo cual permite resaltar los bordes horizontales y verticales de la imagen, sin embargo, no proporciona una detección de bordes binaria clara. Y, por otro lado, Canny tiene un enfoque más completo para la detección de bordes, utilizando múltiples etapas: suavizado de la imagen, cálculo del gradiente, detección de umbrales, etc. De forma general, Canny suele producir resultados más precisos en la detección de bordes con menos esfuerzo.

Por lo que se podría decir que Sobel resalta más los bordes verticales y horizontales en una imagen, y por lo tanto, proporciona más información sobre la dirección y la magnitud del gradiente en cada píxel. Mientras que Canny devuelve una imagen binaria que ofrece una detección de bordes más precisa y limpia en comparación con Sobel.

## Tarea 4

Escogeríamos las funciones vistas en el anterior trabajo ya que explican y muestran visualmente lo más básico para un mejor entendimiento de la materia y de las posibilidades que tiene. Concretamente, el ejercicio 5, el cual muestra en la webcam la zona más clara y la más oscura, aplicando sobre cada frame del vídeo dos variables las cuales sobre cada recorrido de cada fila de la imagen van actualizando sus valores y comparando con los sucesivos hasta dar con los más acentuados habiendo previamente cambiado la imagen a una escala de grises donde es más fácil hacer su calculo. Donde se localizan esas zonas, se dibujan dos círculos  de colores.

## Tarea 5

**Enlace a la tarea**: [Tarea 5](Tarea%205.ipynb).

En la tarea 5, hemos desarrollado una aplicación que procesa la imagen proporcionada por la webcam para realizar un seguimiento de los ojos en tiempo real. Para lograrlo, hemos utilizado un detector de ojos basado en el clasificador en cascada de Haar proporcionado por OpenCV, que es una técnica de aprendizaje automático entrenada para reconocer patrones de ojos en imágenes. El modelo fue descargado directamente desde el repositorio oficial de OpenCV, y se puede visualizar en el siguiente enlace: [Haar Cascade Model](Resources/haarcascade_eye.xml).

Esta aplicación puede ser muy útil en muchos casos. Por un lado, puede ser aplicada en sistemas de seguridad, como en la videovigilancia y el control de acceso, donde la detección de personas y el seguimiento de sus movimientos son fundamentales. Además, puede tener un impacto significativo en la interacción humano-ordenador, permitiendo que las personas controlen interfaces de usuario mediante la mirada, lo que es especialmente relevante en aplicaciones de tecnología y juegos. Además, el seguimiento ocular puede ser útil para detectar fatiga en conductores en sistemas avanzados de asistencia al conductor y para investigaciones en campos como la psicología y las ciencias del comportamiento.

En esta tarea también hemos implementado una posible funcionalidad en la que gracias a la detección de los ojos hemos situado una banda negra, que en cada frame detectado por la webcam, sitúa según unas dimensiones determinadas por la posición de los ojos, unos puntos que posteriormente son utilizados para formar un rectángulo de color negro y así proteger la identidad del usuario.
