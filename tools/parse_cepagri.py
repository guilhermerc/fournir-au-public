#! /usr/bin/env python3

import csv 
import sys 

try:
    input_name = sys.argv[1]
    chosen_year = sys.argv[2]
    chosen_day = sys.argv[3]
    start_period = int(sys.argv[4])
    stop_period = int(sys.argv[5])

except:
    print('Usage: input.csv')
    exit()

with open(input_name, newline='') as csvinput_file:
    
    db_in = csv.reader(csvinput_file, delimiter=',', quotechar='"')
    temp_avg = 0.0
    rain_acc = 0.0
    i = 0
    
    for row in db_in:
        if len(row) > 0:
            if row[0] == '111' and row[1] == chosen_year and row[2] == chosen_day:
#                    if start_period <= float(row[3]) and float(row[3]) <= stop_period:
                    if start_period <= int(row[3]) <= stop_period:
                        temp_avg += float(row[12])
                        rain_acc += float(row[17])
                        i += 1
                    elif float(row[3]) > stop_period:
                        break

    temp_avg = temp_avg/i
    print('Temperatura média: ' + str(temp_avg))
    print('Chuva acumulada: ' + str(rain_acc))
