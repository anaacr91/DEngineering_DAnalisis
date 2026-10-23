#!/bin/bash

if [[ -f "$1" ]]; then
    read -p "Patrón a buscar: " patron
    sed -n "/$patron/p" "$1" > "${patron}.txt"
else
    echo "El archivo no existe o no es regular"
fi