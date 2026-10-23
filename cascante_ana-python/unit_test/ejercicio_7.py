# Para ejecutar este ejercicio debe existir el módulo database indicado en el enunciado.
import database

client = "Anne"
database.connect_to_database()

try:
    database.display_instrument_info(client)
except KeyError:
    print("Oh no! This client does not exist.")
else:
    print(client)
finally:
    database.disconnect_from_database()
