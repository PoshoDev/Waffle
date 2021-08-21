import csv
import numpy

with open("input.csv", newline='') as file:
    array = list(csv.reader(file))
    
    # Check Headers.
    for x in array[0]:
        if x not in ["img", "text", "url"]:
            print("Error: header incorrect.")
    
    xlen = len(array[0])
    for y in range(1, len(array)):
        for x in range(xlen):
            print(array[y][x])