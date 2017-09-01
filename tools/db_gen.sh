#! /usr/bin/env bash

# Usage:
# ./db_gen.sh input_database.csv filtered_output.csv whats_left.csv expression

datainput="$1"
tmpfile=".tmpout.csv"
count=0
cp "$datainput" "$tmpfile.${count}"

for name in "${@:2}"; do
	./food_classifier.py "$tmpfile.${count}" "$name.csv" "$tmpfile."$((count+1)) "$name"
	rm "$tmpfile.${count}"
	count=$((count+1))
done

mv "$tmpfile.${count}" "dataleft.csv"
