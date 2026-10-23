#!/bin/bash

num=$1
resultado=""

(( num % 3 == 0 )) && resultado+="Pling"
(( num % 5 == 0 )) && resultado+="Plang"
(( num % 7 == 0 )) && resultado+="Plong"

if [[ -z "$resultado" ]]; then
    echo "$num"
else
    echo "$resultado"
fi