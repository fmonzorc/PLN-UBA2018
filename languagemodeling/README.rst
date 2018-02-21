Florencia Monczor 18/02/2018

Entrega de TP 1 de materia PLN 2018 (UBA) 

Se cargo un corpus usando la libreria NLTK. El corpus es el "Facundo" de Domingo F. Sarmiento

Se implementaron las clases y los metodos para el tratamiento del texto, incluyendo la tokenizacion, 
la division en N-Gramas, el calculo de probabilidades condicionales de los N-Gramas para la generacion de texto al azar. 

Resultados de la evaluacion de los modelos : 

bigrams :

Log probability: -486.8207447480457
Cross entropy: 0.003830459389639361
Perplexity: 1.002658599951695


3 grams
Log probability: -392.31927952564865
Cross entropy: 0.003086892011500713
Perplexity: 1.0021419612228872

4 grams
Log probability: -311.18962147732816
Cross entropy: 0.00244853823590256
Perplexity: 1.0016986384293094

5 grams
Log probability: -311.18962147732816
Cross entropy: 0.00244853823590256
Perplexity: 1.0016986384293094

6 grams

Log probability: -311.18962147732816
Cross entropy: 0.00244853823590256
Perplexity: 1.0016986384293094


Se observa que la Perplejidad no mejora a partir de n = 4 en los modelos de NGrams.

Ejemplo de codigo generado por el NGramGenerator: 

Córdoba no sabe que existe en la tierra , seca y sin aguas corrientes .
Si el origen de la antipatía .
Diera con lo que precede , he recibido de varios amigos sus adioses a la ciudad ; por ella , en fin , ofendida del ultraje , y esperando venganza y reparación , escribió con la mano docta de la Universidad , el Seminario y los muchos establecimientos de educación que pululaban en aquella ciudad que tuvo un día el candor de llamarse la _Atenas_ americana habían preparado para la vida pública , diré , del gaucho de la manta colorada .
¡ Rosas y sangre !...
Sea hostigados por humillaciones y sufrimientos , sea que previesen la posibilidad de reunirse de nuevo , caer de improviso sobre los que duermen , arrebatarle los caballos , nada se establece .
Porque así es el hombre cuando se ha perdido toda conciencia del derecho ?

