for file in *.csv; do
./menu_normalizer.py "$file" "Normalizado/$file"
done
