En este fichero se llevará a cabo una breve explicación del trabajo que se ha realizado para cada una de las tareas solicitadas para la **práctica 1** de la asignatura **Visión por Computador**. 

Esto implica comentar brevemente como se han llevado a cabo cada una de las tareas, aclarar aquellas cuestiones que puedan llevar a confusiones, explicar el funcionamiento de aquellas funciones o librerías que hayan sido utilizadas, etc.

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

### Tarea 1

**Enlace a la tarea**: [Tarea 1](Tarea%201.ipynb)

En esta primera tarea se puede entender, con cierta facilidad, la solución propuesta para crear un tablero de ajedrez, haciendo uso de las funciones de `numpy` y `matplotlib`.

En primer lugar, se creará una matriz tridimensional (alto, ancho, canal) rellena de ceros y de un único canal. Lo cual dará como resultado una imagen completamente negra. Al tener un solo canal, la imagen será representada como una escala de grises.

Partiendo de esta base, solo quedará recorrer la imagen, e ir modificando los píxeles exactos, para que pasen a ser blancos y representen el patrón de un tablero de ajedrez.

Como la imagen es de *800 x 800*, se interpreta que hay 8 filas y 8 columnas, ya que cada cuadrado del tablero tendrá tamaño *100 x 100* y esto da lugar a 8 cuadrados por fila/columna.

Por eso mismo, se recorrerá la imagen mediante dos bucles **_for_**. Para cada fila, se recorrerán las 8 columnas, y se decidirá si el cuadrado *100 x 100* es blanco o negro en base a si el número de la columna es *par* o *impar* y a una variable que cambia en cada ciclo. Esta variable varía entre 0 y 1 para indicar si en una determinada fila los cuadrados blancos estarán en posiciones pares o en posiciones impares.

### Tarea 2

**Enlace a la tarea**: [Tarea 2](Tarea%202.ipynb)

Esta tarea es muy similar a la anterior, pero, en lugar de automatizar el proceso de creación de la imagen como se hizo con el tablero de ajedrez, en este caso la creación de la imagen se hará de una forma más manual. Esto se debe a que el tablero de ajedrez sigue un determinado patrón, sin embargo, una imagen de estilo **Mondrian** representa patrones totalmente "aleatorios".

Por eso mismo, en la resolución de la tarea puede observarse que para la creación de todas las formas que se visualizan, básicamente se han seleccionado las regiones de la imagen a modificar (a partir de los índices indicados en la matriz que representa la imagen), y se han indicado los valores decimales que tendrá cada canal (al ser una imagen a color dispone de 3 canales, RGB) para obtener un determinado color (blanco, negro, rojo, amarillo o azul).

### Tarea 3

**Enlace a la tarea**: [Tarea 3](Tarea%203.ipynb)

En la tercera tarea

