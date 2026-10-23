#!/bin/bash

read -p "Introduce un número: " num

while [ "$num" -eq 0 ]; do
    echo "el número debe de ser mayor que cero, introdúcelo de nuevo:"
    read num
done

echo $((num * 10))