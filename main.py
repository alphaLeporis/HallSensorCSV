import csv
import numpy as np
from functools import (reduce)
from math import (sqrt)
from os import listdir
from os.path import isfile, join

def rootMeanSquare(xs):
    return sqrt(reduce(lambda a, x: a + x * x, xs, 0) / len(xs))

def gemiddelde_offset(file):
    dataarray = []
    with open(file, newline='') as csvfile:
        bestand1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in bestand1:
            dataarray.append(int(row[1])/16)
    gemiddelde = np.average(dataarray)
    return gemiddelde

def ruis_berekenaar(file, offset):
    dataarray = []
    nieuwe = []
    with open(file, newline='') as csvfile:
        bestand1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in bestand1:
            dataarray.append(int(row[1]) / 16)

    for waarde in dataarray:
        nieuwe.append(((waarde - offset) * 0.002) / 0.1)

    return nieuwe

def bestandinlezen(file):
    dataarray = []
    with open(file, newline='') as csvfile:
        bestand1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in bestand1:
            dataarray.append(int(row[1])/16)
    return dataarray

def bestandenlijst(file):
    bestanden = []
    with open(file, newline='', encoding='utf-8-sig') as csvfile:
        bestand1 = csv.reader(csvfile, delimiter=';')
        for row in bestand1:
            bestanden.append(row[0])
    return bestanden

def arrayverwerken(array, offset):
    nieuwe = []
    for waarde in array:
        nieuwe.append(((waarde - offset) * 0.002) / 0.1)
    return nieuwe

path2files = "demo/data/" # Path to csv-files directory
path2idle = "demo/idle-value/ruis2.csv" # Path to idle file (noise)

files = [f for f in listdir(path2files) if isfile(join(path2files, f))]
print(files)
with open('output.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writedata = csv.writer(csvfile, delimiter=';')
    for data in files:
        bestand = bestandinlezen(path2files + data)
        offset = gemiddelde_offset(path2idle)
        array = arrayverwerken(bestand, offset)
        ruis = ruis_berekenaar(path2idle, offset)
        value = (rootMeanSquare(array)  - rootMeanSquare(ruis))*230
        print(data, value)
        writedata.writerow([data, value])