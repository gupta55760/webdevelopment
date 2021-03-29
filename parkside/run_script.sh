#!/bin/bash

for i in `ls check*.py`
do
    echo "Running ${i}..."
    python $i
done
