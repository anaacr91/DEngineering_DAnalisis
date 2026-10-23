#!/bin/bash

read -p "Introduce un número: " num

if [ "$num" -ne 0 ]; then
    echo "El número es distinto de cero"
else
    echo "El número es cero"
fi