#Se importa SparkContext y SparkConf
from pyspark import SparkContext, SparkConf

#Se crea la instancia de la configuración con el nombre de la aplicación contador
conf1 = SparkConf().setAppName("contador")

#Se crea el contexto pasando la instancia de la configuración
sc = SparkContext(conf = conf1).getOrCreate()

#Se extrae las líneas del texto 
lineas = sc.textFile("/tmp/data/declaracion_onut.text")

#Se extrae las palabras del texto y se cuentan
contarPalabras = lineas.flatMap(lambda linea: linea.split(" ")).countByValue()

#Se muestra las palabras con la cantidad de veces que tiene su aparición
for palabra, contador in contarPalabras.items():
    print("{} : {}".format(palabra, contador))