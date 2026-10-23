# Quick start

## docker-compose

To create a simplistic standalone cluster with [docker-compose](http://docs.docker.com/compose):

```bash
docker-compose up
```

Could Add more worker nodes with

```bash
docker-compose up --scale worker=3
```

The **SparkUI** will be running at `http://127.0.0.1:8080` with one worker listed.

Access the master node to run your application

```bash
docker compose exec master /bin/bash
```

## Examples:

### Calculate Pi

To run `SparkPi`, inside de master node run

```bash
/opt/spark/bin/spark-submit \
    --master spark://master:7077 \
    --class org.apache.spark.examples.SparkPi \
    /opt/spark/examples/jars/spark-examples_2.13-4.0.1.jar 1000
```

### Run your python scripts

#### Parallel Sum

```bash
/opt/spark/bin/spark-submit \
    --master spark://master:7077 \
    scripts/example-1.py
```

#### Word Count

```bash
/opt/spark/bin/spark-submit \
    --master spark://master:7077 \
    scripts/example-2.py
```
