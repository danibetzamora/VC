# Práctica 4 VC - Curso 2023/2024

La práctica cuatro propone, a partir de los detectores faciales presentados en la explicación, que se lleve a cabo una implementación que haga uso de alguno de dichos detectores faciales con cualquier tipo de finalidad. 

En nuestro caso, hemos decidido utilizar el detector basado en **Convolutional Neural Networks (CNNs)**, pues tras hacer varias pruebas con él y el resto de detectores, hemos llegado a la conclusión de que es uno de los más eficientes y que mejor detección facial presenta. Además, como modelo de máscara facial hemos usado el archivo *shape_predictor_68_face_landmarks.dat*, el cual nos permite extraer mucha más información de la cara detectada, teniendo hasta 68 puntos distintos alrededor del rostro que nos posibilitan implementar diferentes filtros con una mayor precisión.

Para esta práctica, hemos propuesto 3 filtros distintos con diferentes finalidades cada uno. El primero de ellos consiste en un filtro divertido, mediante el cual se nos pone una peluca, unas gafas y un bigote, cambiando ligeramente nuestra apariencia. Por otro lado, el segundo filtro tiene como objetivo probarnos distintos tipos de gafas, pudiendo ver que tipo de gafas nos queda mejor y aclararnos las ideas a la hora de elegir unas. Por último, el tercer filtro lleva a cabo una transposición entre los ojos y la boca de la cara, colocando uno de los ojos en la boca, y la boca en ambos ojos.

*Trabajo realizado por*:
- **Jorge Vega Sánchez**
- **Daniel Betancor Zamora**

## Filtro 1

**Enlace a la tarea**: [Filtro 1](Filtro%201.ipynb).

Resultado

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/filtro1.jpg">
</div>

<p>&nbsp;</p>

## Filtro 2

**Enlace a la tarea**: [Filtro 2](Filtro%202.ipynb).

Resultado

<p>&nbsp;</p>

<div align="center">
    <img src="./README%20Images/filtro2.png">
</div>

<p>&nbsp;</p>

## Filtro 3

**Enlace a la tarea**: [Filtro 3](Filtro%203.ipynb).

Resultado

<p>&nbsp;</p>


<div align="center">
    <img src="./README%20Images/filtro3.jpg">
</div>

<p>&nbsp;</p>