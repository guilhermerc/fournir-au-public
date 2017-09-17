#! /usr/bin/env python3

import sys
import csv
import menu_map
import datetime

db_input = sys.argv[1]

def normalize_elem(min_, max_, value):
    '''DESCUBRA'''
    if max_ - min_ == 0:
        return 0
    return (value - min_)/(max_ - min_) - 0.5

def normalize(array):
    '''DESCUBRA'''
    max_ = array[0]
    min_ = array[0]
    for i in range(1, len(array)):
        if array[i] > max_:
            max_ = array[i]
        if array[i] < min_:
            min_ = array[i]
 
    for i in range(0, len(array)):
        array[i] = normalize_elem(min_, max_, array[i])

    return array

with open(db_input, newline='\n') as db_in:
    day_of_the_week = []
    month = []
    menu = []
    temp_avg = []
    rain_acc = []
    nutri_week = []
    vacation = []
    strike = []
    target = []
    traindb = csv.reader(db_in, delimiter='\t', quotechar='"')
    for row in traindb:
        date = row[0].split('-')
        date_info = datetime.date(int(date[0]), int(date[1]), int(date[2])).timetuple()
        day_of_the_week.append(float(date_info.tm_wday))
        month.append(float(date_info.tm_mon))
        menu.append(menu_map.map[row[1]])
        temp_avg.append(float(row[4]))
        rain_acc.append(float(row[5]))
        nutri_week.append(float(row[6]))
        vacation.append(float(row[7]))
        strike.append(float(row[8]))
        target.append(int(row[3]))
    # normalizing values into -0.5 - 0.5 range
    day_of_the_week = normalize(day_of_the_week)
    month = normalize(month)
    menu = normalize(menu)
    temp_avg = normalize(temp_avg)
    rain_acc = normalize(rain_acc)
    nutri_week = normalize(nutri_week)
    vacation = normalize(vacation)
    strike = normalize(strike)
    # input normalization for fann using 
    for i in range(0, len(target)):
         print(str(day_of_the_week[i]) + ' ' + str(month[i]) + ' ' + str(menu[i]) + ' ' + str(temp_avg[i]) + ' ' + str(rain_acc[i]) + ' ' + str(nutri_week[i]) + ' ' + str(vacation[i]))
         print(str(target[i]))
