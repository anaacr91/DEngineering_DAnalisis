#!/bin/bash

if [[ "$1" =~ ^[0-9]$ ]]; then
    echo "El argumento introducido es un dígito"
else
    echo "El argumento introducido no es un dígito"
fi