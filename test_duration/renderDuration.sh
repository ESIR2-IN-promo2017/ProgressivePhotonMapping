#!/bin/bash

for i in {1..60}
do
    echo "----rendering in " $i " seconds----"
    date >> render.log
    py render.py $i >> render.log
done
