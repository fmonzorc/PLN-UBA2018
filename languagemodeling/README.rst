Florencia Monczor 18/02/2018

Entrega de TP 1 de materia PLN 2018 (UBA) 

Se cargo un corpus usando la libreria NLTK

Se implementaron las clases y los metodos para el tratamiento del texto, incluyendo la tokenizacion, 
la division en N-Gramas, el calculo de probabilidades condicionales de los N-Gramas para la generacion de texto al azar. 

Si bien los tests entregados para la evaluacion de dichas clases y metodos no fallan, 
el resultado de la evaluacion de los modelos no es satisfactorio en esta primer version. 

Tanto para n=2 y n= 3 
log probability = -inf
cross entropy = inf 
perplexity = inf 

En la version 2 se corregira el codigo para evitar el error de probabilidad = 0 que esta probablemente causando estos errores




