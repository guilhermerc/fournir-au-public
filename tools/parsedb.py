#! /usr/bin/env python3

import csv
import sys

try:
    input_name = sys.argv[1]
    output_name = sys.argv[2]
except:
    print('Usage: input.csv output.csv')
    exit()

with open(input_name, newline='') as csvinput_file:
    with open(output_name, 'w', newline='') as csvoutput_file:
        db_spreadsheet = csv.DictReader(csvinput_file, delimiter='\t', quotechar='"')
        db_output = csv.writer(csvoutput_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in db_spreadsheet:
            if row['Tipo de Refeição'] == 'Almoço' and int(row["Num. Refeicões RU"]) > 1 and int(row["Refeições Servidas"]) > 1:
                menu = row['Cardápio']
                for i in range(3):
                    mistura = menu.split('-')[i]
                    mistura = mistura.strip()
                    if len(mistura) > 0:
                        break
                mistura = mistura.upper()
                mistura = mistura.replace('Ã', 'A')
                mistura = mistura.replace('Á', 'A')
                mistura = mistura.replace('À', 'A')
                mistura = mistura.replace('Ê', 'E')
                mistura = mistura.replace('É', 'E')
                mistura = mistura.replace('Í', 'I')
                mistura = mistura.replace('Ó', 'O')
                mistura = mistura.replace('Õ', 'O')
                mistura = mistura.replace('Ô', 'O')
                mistura = mistura.replace('Ú', 'U')
                mistura = mistura.replace('Ü', 'U')
                mistura = mistura.replace('Ç', 'C')
                            
                db_output.writerow([row['Data'], mistura, row['Num. Refeições Planejadas'], row['Num. Refeições Servidas']])

    
