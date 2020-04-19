import matplotlib.pyplot as plt
import csv
import numpy as np
from os import listdir
from os.path import isfile, join

def bestandinlezen(file):
    x = []
    y = []
    with open(file, newline='') as csvfile:
        bestand1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in bestand1:
            x.append(float(row[0]))
            y.append(int(row[1]))
    return x, y

path2files = "demo/data/" # Path to csv-files directory
path2idle = "demo/idle-value/ruis2.csv" # Path to idle file (noise)

files = [f for f in listdir(path2files) if isfile(join(path2files, f))]
for i in range(len(files)):
    print("{:<4}{:>}".format(i, files[i]))
index = int(input("Give index number: "))
x1, y1 = bestandinlezen(path2files+files[index])
x2, y2 = bestandinlezen(path2idle) # Idle value to set 0 point

y = y1 - np.average(y2)

plt.plot(x1, y)
plt.show()
