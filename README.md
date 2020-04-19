# HallSensorCSV
Getting power usage from a hall sensor using a Python3 script

## Setup
This is a simple code that changes hall sensor data to power consumption.
Her is the schematic.
![Schematic](/images/schematic.jpg)
Format: ![Alt Text](url)

## Installation
1. Clone this repository
2. You will need these dependencies:
  1. numpy
  2. csv
  3. functools
  4. matplotlib
  
## Usage
**main.py** reads all the csv files from a specific directory (default is demo/data) and outputs them in a single output.csv
**plot.py** The console will print all the csv files from a specific directory (default is demo/data), you will have to select and index to plot a graph.

## Demo
There is a demo available
**demo/data/** is where all the raw data is
**demo/idle-value/** is where the idle (noise) measurement is

Feel free to adapt/change/steal this code as many times as you want. If you have any cool projects feel free to show them to me! 

