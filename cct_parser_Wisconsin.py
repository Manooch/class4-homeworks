#!/usr/bin/env python

import os

myfilename = "breast-cancer-wisconsin.txt"

with open(myfilename, 'r') as file_handle:
    mylist = []
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ').replace(',', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        linelist = []
        for value in values:
            try:
                linelist += [int(value)]
            except ValueError as e:
                linelist += [float(value)]
        mylist += [linelist]

print("just printing a bit to save our eyes....")
print(mylist[0:2])
rotated_list = [[mylist[jdx][idx]
                 for jdx, row in enumerate(mylist)]
                for idx, column in enumerate(mylist[0])]
print(rotated_list[0])

