#! /usr/bin/env python3

import csv
import sys
import datetime

try:
    db_ru = sys.argv[1]
    db_cepagri = sys.argv[2]
    db_unified = sys.argv[3]
except:
    print('Usage: input_0.csv input_1.csv output.csv')
    exit()

def search_cepagri(db_cepagri, chosen_year, chosen_day, start_period, stop_period):
    '''DESCUBRA'''
    i = 0
    temp_avg = 0
    rain_acc = 0
    for row in db_cepagri:
        if len(row) > 0:
            if row[0] == '111' and int(row[1]) == chosen_year and int(row[2]) == chosen_day:
                    if start_period <= int(row[3]) <= stop_period:
                        temp_avg += float(row[12])
                        rain_acc += float(row[17])
                        i += 1
                    elif float(row[3]) > stop_period:
                        break
    if i == 0:
        return 0, 0, 0
    temp_avg = temp_avg/i
    return temp_avg, rain_acc, 1

with open(db_ru, newline='') as db_ru:
    with open(db_cepagri, newline='') as db_cepagri:
        with open(db_unified, 'w', newline='') as db_unified:
            db_ru = csv.reader(db_ru, delimiter='\t', quotechar = '"')
            db_cepagri = csv.reader(db_cepagri, delimiter = ',', quotechar = '"')
            db_unified = csv.writer(db_unified, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            for row in db_ru:
                date = row[0].strip()
                date = date.split('-')
                year = int(date[0])
                month = int(date[1])
                day_of_month = int(date[2])
                date_info = datetime.date(year, month, day_of_month).timetuple()
                temp_avg, rain_acc, status = search_cepagri(db_cepagri, year, date_info.tm_yday, 1030, 1400)
                if status == 1:
                    row.extend([str(temp_avg),str(rain_acc)])
                    db_unified.writerow(row)
