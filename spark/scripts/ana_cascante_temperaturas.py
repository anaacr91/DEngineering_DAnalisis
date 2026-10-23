#!/usr/bin/env python3
"""
One Billion Row Challenge - Adaptación con PySpark
Procesa mediciones de temperatura de estaciones meteorológicas
Calcula min, promedio y max por estación, ordenado alfabéticamente
"""

from pyspark import SparkContext, SparkConf
import math

def parse_line(line):
    """
    extrae de cada línea del archivo en formato: estación;temperatura
    Returns: (estación, temperatura)
    """
    try:
        parts = line.split(';')
        if len(parts) == 2:
            station = parts[0].strip()
            temp = float(parts[1].strip())
            return (station, temp)
    except:
        return None

def round_down(value):
    """
    Redondea hacia abajo a un decimal
    """
    return math.floor(value * 10) / 10

def main():
    conf = SparkConf().setAppName("One Billion Row Challenge - Temperaturas")
    sc = SparkContext(conf=conf)
    
    try:
        print("Cargando archivo measurements.txt...")
        input_path = "/opt/spark/work-dir/measurements.txt"
        lines_rdd = sc.textFile(input_path)
        
        parsed_rdd = lines_rdd.map(parse_line).filter(lambda x: x is not None)
        

        def create_stats(temp):
            """Crea una tupla con estadísticas iniciales
            Para cada estación: min, max, suma, count"""
            return (temp, temp, temp, 1)  
        
        def combine_stats(stats1, stats2):
            """Combina dos tuplas de estadísticas"""
            min1, max1, sum1, count1 = stats1
            min2, max2, sum2, count2 = stats2
            return (
                min(min1, min2),
                max(max1, max2),
                sum1 + sum2,
                count1 + count2
            )
        
        """ Transformar valores a estadísticas y combinar por estación """
        stats_rdd = parsed_rdd.mapValues(create_stats).reduceByKey(combine_stats)
        
        def format_result(station_stats):
            """Formatea el resultado según el formato requerido"""
            station, (min_temp, max_temp, sum_temp, count) = station_stats
            mean_temp = sum_temp / count
            
            min_rounded = round_down(min_temp)
            mean_rounded = round_down(mean_temp)
            max_rounded = round_down(max_temp)
            
            return f"{station};{min_rounded:.1f}/{mean_rounded:.1f}/{max_rounded:.1f}"
        
        results_rdd = stats_rdd.map(format_result)
        
        results_sorted = results_rdd.sortBy(lambda x: x.split(';')[0])
        
        print("\n" + "="*70)
        print("RESULTADOS - Estadísticas de Temperatura por Estación")
        print("Formato: Estación;min/mean/max")
        print("="*70 + "\n")
        
        results = results_sorted.collect()
        
        print(f"Total de estaciones procesadas: {len(results)}\n")
        print("Primeras 50 estaciones:")
        print("-" * 70)
        
        for i, result in enumerate(results[:50], 1):
            print(result)
        
        if len(results) > 50:
            print(f"\n... y {len(results) - 50} estaciones más")
        
        output_path = "/opt/spark/work-dir/resultados_temperaturas.txt"
        with open(output_path, 'w') as f:
            for result in results:
                f.write(result + '\n')

        print(f"\n{'='*70}")
        print(f"Resultados completos guardados en: {output_path}")
        print(f"{'='*70}\n")
        
        total_lines = lines_rdd.count()
        valid_measurements = parsed_rdd.count()
        print(f"Estadísticas del procesamiento:")
        print(f"  - Total de líneas leídas: {total_lines:,}")
        print(f"  - Mediciones válidas: {valid_measurements:,}")
        print(f"  - Estaciones únicas: {len(results):,}")
        
    finally:
        sc.stop()

if __name__ == "__main__":
    main()
