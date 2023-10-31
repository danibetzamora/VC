# Práctica 4 VC - Curso 2023/2024

La práctica cuatro propone, a partir de los detectores faciales presentados en la explicación, que se lleve a cabo una implementación que haga uso de alguno de dichos detectores faciales con cualquier tipo de finalidad. 

En nuestro caso, hemos decidido utilizar el detector basado en **Convolutional Neural Networks (CNNs)**, pues tras hacer varias pruebas con él y el resto de detectores, hemos llegado a la conclusión de que es uno de los más eficientes y que mejor detección facial presenta. Además, como modelo de máscara facial hemos usado el archivo *shape_predictor_68_face_landmarks.dat*, el cual nos permite extraer mucha más información de la cara detectada, teniendo hasta 68 puntos distintos alrededor del rostro que nos posibilitan implementar diferentes filtros con una mayor precisión.

Para esta práctica, hemos propuesto 3 filtros distintos con diferentes finalidades cada uno. El primero de ellos consiste en un filtro divertido, mediante el cual se nos pone una peluca, unas gafas y un bigote, cambiando ligeramente nuestra apariencia. Por otro lado, el segundo filtro tiene como objetivo probarnos distintos tipos de gafas, pudiendo ver que tipo de gafas nos queda mejor y aclararnos las ideas a la hora de elegir unas. Por último, el tercer filtro lleva a cabo una transposición entre los ojos y la boca de la cara, colocando uno de los ojos en la boca, y la boca en ambos ojos.

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

## Filtro 1

**Enlace al primer filtro**: [Filtro 1](Filtro%201.ipynb).

En esta primera propuesta, como ya se comentó en la introducción, se hizo uso del detector facial basado en **Convolutional Neural Networks**, al igual que en el resto de filtros implementados.

El objetivo principal de esta primera implementación es crear un filtro divertido, en el que se nos pone en tiempo real una peluca, unas gafas y un bigote. Como aspectos más relevantes del código desarrollado se destaca lo siguiente:

- Se ha definido un método el cual se encarga de fijar las coordenadas **x** e **y** exactas en las cuales se debe superponer cada una de las imágenes (ajustando el centro de las imágenes con las coordenadas correspondientes de la cara en las que se desea superponer).
- En dicho método, se lleva a cabo la superposición de las imágenes sobre el *frame* de la webcam en la coordenada calculada para cada uno de los tres canales de color, y teniendo en cuenta la transparencia (*alpha*).
- Para cada *frame* se llama al método anterior, colocando el bigote sobre el punto 51 del modelo de máscara facial, y la peluca y las gafas sobre el punto 27.

A continuación se muestra el resultado obtenido:

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/filtro1.jpg">
</div>

<p>&nbsp;</p>

## Filtro 2

**Enlace al segundo filtro**: [Filtro 2](Filtro%202.ipynb).

Como segundo filtro, hemos desarrollado uno parecido al primero, con la diferencia de que en este caso el filtro puede llegar a tener una utilidad real. 

La finalidad concreta de este filtro es que podemos probarnos distintos modelos de gafas, pudiendo ver cual de ellas nos queda mejor. El filtro nos permitirá ir cambiando entre las distintas gafas disponibles mediante la tecla **D**, consiguiendo de esta forma ver que tipo de gafas nos sienta mejor, para ir haciéndonos una idea antes de ir a comprarlas.

En la siguiente imagen se muestra un ejemplo con tres modelos de gafas diferentes (con el filtro en ejecución se podrían ver más gafas e ir intercambiándolas):

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/filtro2.png">
</div>

<p>&nbsp;</p>

## Filtro 3

**Enlace al tercer filtro**: [Filtro 3](Filtro%203.ipynb).

En este tercer filtro se vuelve a hacer una propuesta divertida. Ahora, el objetivo principal es hacer una pequeña transposición entre los elementos principales de la cara, poniendo uno de los ojos en el lugar de la boca y la boca en el lugar de los dos ojos.

Gracias al detector facial y a los 68 puntos proporcionados por el modelo de máscara facial, se han podido obtener las regiones de interés de la cara con una alta precisión. Por ejemplo, para llevar a cabo este filtro, se ha tenido que obtener la región que encierra a ambos ojos y la región que encierra a la boca, por lo que mediante los 68 puntos se han podido establecer las coordenadas necesarias para cubrir las zonas que nos interesan. Una vez obtenidas las regiones que almacenan los ojos y la boca, solo queda igualar la región de la boca a la de uno de los ojos y la de los ojos a la de la boca.

Por supuesto, y tal y como se puede ver en el código, se han tenido que llevar a cabo ciertas comprobaciones y redimensiones de las regiones para que no surja ningún error, pues la dimensión de la boca y de los ojos no es la misma, y esto puede dar problemas a la hora de superponer las imágenes en el *frame*.

En la siguiente imagen se muestra el resultado del filtro aplicado:

<p>&nbsp;</p>


<div align="center">
    <img src="./README%20Images/filtro3.jpg">
</div>

<p>&nbsp;</p>

## Filtro 4

**Enlace al cuarto filtro**: [Filtro 4](Filtro%204.ipynb).

En este cuarto y último filtro intercambiamos las caras de dos personas. Obtenemos las dimesiones de ambas caras, alto y ancho, al igual que las que compara son las dos caras más cercanas.

Posteriormente igualamos los puntos de la primera cara a la segunda cara marcando en todo momento con un rectangulo verde el marco original de cada una de las caras. Estas se irán reescalando a medida que vayan cambiando los puntos. Para verificar lo que se va detectando, se muestra por consola los mensajes de "error" para que se pueda ejecutar correctamente el código.

Se muestra en la siguiente imágen a dos personas, siendo una de ellas un modelo de andar por casa:


<p>&nbsp;</p>


<div align="center">
    <img src="./README%20Images/filtro4.jpg">
</div>

<p>&nbsp;</p>
