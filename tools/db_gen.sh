#! /usr/bin/env bash

arg_array=( "S@" )

count=0
for name in "$@"; do
	./food_classifier.py output_${count}.csv $name.csv output_$((count+1)).csv $name
	count=$((count+1))
done
