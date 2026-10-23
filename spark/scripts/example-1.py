# Se importan los módilos necesarios
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Se crea SparkSession
spark = SparkSession.builder \
   .appName("parallel sum") \
   .getOrCreate()

rdd = spark.sparkContext.parallelize(range(1, 1_000_000_000))

print("THE SUM IS HERE: ", rdd.sum())

# Se detiene SparkSession
spark.stop()