#! /usr/bin/env python3

import sys
import csv
import menu_map
import datetime
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork

db_filename = sys.argv[1]
db_repeat = int(sys.argv[2])
number = int(sys.argv[3])

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

neural_network = buildNetwork(8, 1, 1, bias=True, hiddenclass=TanhLayer)
data_set = SupervisedDataSet(8, 1)
with open(db_filename, newline='\n') as db_in:
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
        target.append(float(row[3]))
    # normalizing values into -0.5 - 0.5 range
    day_of_the_week = normalize(day_of_the_week)
    month = normalize(month)
    menu = normalize(menu)
    temp_avg = normalize(temp_avg)
    rain_acc = normalize(rain_acc)
    nutri_week = normalize(nutri_week)
    vacation = normalize(vacation)
    strike = normalize(strike)
    for i in range(0, db_repeat * len(target)):
        data_set.addSample((day_of_the_week[i], month[i], menu[i], temp_avg[i], rain_acc[i], nutri_week[i], vacation[i], strike[i]), (target[i],))


trainer = BackpropTrainer(neural_network, data_set) 
#for i in range(0, number):
#    trainer.trainEpochs(10)
#    print("Params: " + str(neural_network.params))
    

trainer.trainUntilConvergence()
print("Params: " + str(neural_network.params))

#print("Params: " + str(neural_network.params))
#print("Net: " + neural_network)
#print(str(neural_network.activate((0, 0))))
