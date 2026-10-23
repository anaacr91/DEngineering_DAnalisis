#!/bin/bash

if [[ -f "$1" ]]; then
    tr '[:upper:]' '[:lower:]' < "$1" > temporal.txt
    mv temporal.txt "$1"

    read -p "¿Desea ver el contenido? (y/n): " resp

    if [[ "$resp" == "y" ]]; then
        cat "$1"
    else
        echo "ok"
    fi
else
    echo "el argumento no es un archivo regular o no existe"
fi