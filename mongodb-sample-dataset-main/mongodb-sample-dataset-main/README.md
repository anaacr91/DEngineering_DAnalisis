# [MongoDB Sample Dataset](https://docs.atlas.mongodb.com/sample-data/available-sample-datasets/)

> this is a fork of [repo](https://github.com/mcampo2/mongodb-sample-databases).
> the original repo has BSON dump. I've removed it and I added a bash [script](https://github.com/neelabalan/mongodb-sample-dataset/blob/main/script.sh) to import the JSON to respective db 

MongoDB does not provide any sample databases on their website, However, they do provide sample databases for their cloud service Atlas.  These databases have been dumped from a MongoDB Atlas cluster using the MongoDB Compass GUI.  There are 7 databases, with each database collection (table) stored in a seperate JSON file.  These files will accelerate learning of MongoDB's features by allowing new developers to quickly experiment with prepopulated datasets.


## Sample Datasets

| Dataset Name                                                                                | Description                                                       | Collections                                                                |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------- |
| [Sample AirBnB Listings Dataset](https://docs.atlas.mongodb.com/sample-data/sample-airbnb/) | Contains details on AirBnB listings.                              | listingsAndReviews                                                         |
| [Sample Analytics Dataset](https://docs.atlas.mongodb.com/sample-data/sample-analytics/)    | Contains training data for a mock financial services application. | accounts, customers, transactions                                          |
| [Sample Geospatial Dataset](https://docs.atlas.mongodb.com/sample-data/sample-geospatial/)  | Contains shipwreck data.                                          | shipwrecks                                                                 |
| [Sample Mflix Dataset](https://docs.atlas.mongodb.com/sample-data/sample-mflix/)            | Contains movie data.                                              | comments, movies, theaters, users                                          |
| [Sample Supply Store Dataset](https://docs.atlas.mongodb.com/sample-data/sample-supplies/)  | Contains data from a mock office supply store.                    | sales                                                                      |
| [Sample Training Dataset](https://docs.atlas.mongodb.com/sample-data/sample-training/)      | Contains MongoDB training services dataset.                       | companies, grades, inspection, posts, routes, stories, trips, tweets, zips |
| [Sample Weather Dataset](https://docs.atlas.mongodb.com/sample-data/sample-weather/)        | Contains detailed weather reports.                                | data                                                                       |

## Running in docker

```bash
# Inicializamos mongoDB
docker compose up -d

# Accedemos al servidor de mongo
docker compose exec mongo /bin/bash

# Accedemos a los datasets y los cargamos usando el script proporcionado
cd /practicas
./script.sh localhost 27017 root example
```

En caso de error revisar el tipo de final de linea (puede cambiarse con el comando 'sed -i 's/\r$//' script.sh')



