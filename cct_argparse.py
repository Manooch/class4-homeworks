#!/usr/bin/env python

import argparse
import os

# To validate the existance of the input

def validatePath(DirectoryName):
    if os.path.exists(str(DirectoryName)):
       return True
    raise argparse.ArgumentTypeError("{0} does not exist! Please enter existing directory and filename".format(DirectoryName))

# To put user input into Argparse argument

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs='?', help="Input folder Name", type=str)
args = parser.parse_args()
validatePath(args.filename)

#To replace multiple spaces and coma with one space

with open(args.filename) as file_handle:
    mylist = []
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ').replace(',', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        linelist = []
# To conver string into float and int
        for value in values:
           try:
                linelist += [int(value)]
           except ValueError as e:
               linelist += [float(value)]
        mylist += [linelist]
# To transpose
print("just printing a bit to save our eyes....")
print(mylist[0:2])
rotated_list = [[mylist[jdx][idx]
                 for jdx, row in enumerate(mylist)]
                for idx, column in enumerate(mylist[0])]
print(rotated_list[0])
