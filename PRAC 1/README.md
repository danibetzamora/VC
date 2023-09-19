## Práctica 1 VC - Curso 2023/2024

En este fichero se llevará a cabo una breve explicación del trabajo que se ha realizado para cada una de las tareas solicitadas para la **práctica 1** de la asignatura **Visión por Computador**. 

Esto implica comentar brevemente como se han llevado a cabo cada una de las tareas, aclarar aquellas cuestiones que puedan llevar a confusiones, explicar el funcionamiento de aquellas funciones o librerías que hayan sido utilizadas, etc.

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

### Tarea 1

**Enlace a la tarea**: [Tarea 1](Tarea%201.ipynb).

En esta primera tarea se puede entender, con cierta facilidad, la solución propuesta para crear un tablero de ajedrez, haciendo uso de las funciones de `numpy` y `matplotlib`.

En primer lugar, se creará una matriz tridimensional (alto, ancho, canal) rellena de ceros y de un único canal. Lo cual dará como resultado una imagen completamente negra. Al tener un solo canal, la imagen será representada como una escala de grises.

Partiendo de esta base, solo quedará recorrer la imagen, e ir modificando los píxeles exactos, para que pasen a ser blancos y representen el patrón de un tablero de ajedrez.

Como la imagen es de *800 x 800*, se interpreta que hay 8 filas y 8 columnas, ya que cada cuadrado del tablero tendrá tamaño *100 x 100* y esto da lugar a 8 cuadrados por fila/columna.

Por eso mismo, se recorrerá la imagen mediante dos bucles **_for_**. Para cada fila, se recorrerán las 8 columnas, y se decidirá si el cuadrado *100 x 100* es blanco o negro en base a si el número de la columna es *par* o *impar* y a una variable que cambia en cada ciclo. Esta variable varía entre 0 y 1 para indicar si en una determinada fila los cuadrados blancos estarán en posiciones pares o en posiciones impares.

### Tarea 2

**Enlace a la tarea**: [Tarea 2](Tarea%202.ipynb).

Esta tarea es muy similar a la anterior, pero, en lugar de automatizar el proceso de creación de la imagen como se hizo con el tablero de ajedrez, en este caso la creación de la imagen se hará de una forma más manual. Esto se debe a que el tablero de ajedrez sigue un determinado patrón, sin embargo, una imagen de estilo **Mondrian** representa patrones totalmente "aleatorios".

Por eso mismo, en la resolución de la tarea puede observarse que para la creación de todas las formas que se visualizan, básicamente se han seleccionado las regiones de la imagen a modificar (a partir de los índices indicados en la matriz que representa la imagen), y se han indicado los valores decimales que tendrá cada canal (al ser una imagen a color dispone de 3 canales, RGB) para obtener un determinado color (blanco, negro, rojo, amarillo o azul).

### Tarea 3

**Enlace a la tarea**: [Tarea 3](Tarea%203.ipynb).

En la tercera tarea se hace uso de las funciones de dibujo que ofrece **OpenCV**, teniendo la posibilidad de dibujar diferentes formas como pueden ser: una línea, un círculo, un cuadrado, una elipse...

Por eso mismo, en la resolución de esta tarea se proponen dos imágenes creadas con las funciones de dibujo. 

La primera de ellas, es una pequeña muestra de las diferentes formas que pueden ser creadas haciendo uso de esta librería. Se ve claramente como en una imagen de fondo negro se dibujan formas de diferentes colores y grosores, como pueden ser cuadrados, círculos, líneas...

Sin embargo, en la segunda imagen se decidió llevar a cabo un diseño **Mondrian** como en la tarea anterior, pero esta vez haciendo uso de las funciones básicas de dibujo de **OpenCV** (líneas y cuadrados). Es por ello que para la creación de la segunda imagen se fueron incluyendo a mano las diferentes formas, en las coordenadas necesarias, para obtener el resultado que se muestra al final de la tarea.

### Tarea 4

**Enlace a la tarea**: [Tarea 4](Tarea%204.ipynb).

Para este caso, se propone llevar a cabo ciertas modificaciones en un plano de la imagen. Recordemos que las imágenes a color están formadas por tres planos, por lo que se deberá realizar algún tipo de modificación en alguno de los tres para que se produzca algún efecto visual que modifique la imagen original.

En nuestro caso, hemos decidido aplicar ciertas modificaciones a los tres planos de una imagen que es cargada directamente desde el disco duro. La modificación en cuestión ha sido invertir los valores de cada uno de los planos, lo cual se consigue realizando la siguiente operación matemática: 

```python
# Inversión de color del plano rojo
plano_rojo = 255 - img_rgb[:,:,2]

# Inversión de color del plano verde
plano_verde = 255 - img_rgb[:,:,1]

# Inversión de color del plano azul
plano_azul = 255 - img_rgb[:,:,0]
```

De esta manera, se logra invertir el valor de cada uno de los planos. Por ejemplo, si el plano rojo tenía un valor de **255**, al hacer la operación `255 -255`, nos dará como resultado un **0**, es decir, el valor opuesto al valor actual del plano.

Acto seguido, se hizo un *merge* de los tres planos, lo cual produce un efecto de colores invertidos en la imagen original. La línea en concreto que produce ese resultado es la siguiente:

	inver_img = cv2.merge((plano_rojo,plano_verde,plano_azul))

Como propuesta adicional a esta tarea, se ha decido aprovechar la estructura de *collage* que se muestra en el cuaderno de enunciado de la práctica. En esa estructura, se muestra cada uno de los planos (RGB) correspondientes a la entrada de la webcam. 

El objetivo de esto es hacer modificaciones totalmente independientes a cada uno de los tres planos, de tal manera que se pueda ver en tiempo real (en cada una de las imágenes mostradas en el collage) la modificación que se le ha realizado a cada plano.

Por ejemplo, para el plano **rojo** (primer recuadro), se ha propuesto realizar nuevamente una **inversión de colores**. En segundo lugar, para el plano **verde** (segundo recuadro), se ha propuesto un **aumento de brillo** (el cual se obtiene aumentando el valor actual de cada uno de los píxeles. Por último, para el plano **azul** (tercer recuadro) se ha decidido hacer uso de una función de **OpenCV**, la cual aplica un filtro de tipo *blur* que difumina la imagen de dicho plano.

En caso de querer saber más sobre las modificaciones realizadas o la función `GaussianBlur` de **OpenCV**, dejamos el enlace a la explicación que hemos hecho en el propio cuaderno de la tarea 4:

- [Explicación de las modificaciones de los planos](Tarea%204.ipynb#explicacion-modificaciones).


