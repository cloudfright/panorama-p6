#!/usr/bin/python3

import sys
import getopt
import csv
import os

###########################################
# This script takes a remotemap as input, #
# extracts all the Propellerhead scopes   #
# and writes them to a new remotemap      #                      
# Arguments                               #
# -i [input file name]                    #
# -o [output file name]                   #
###########################################

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    # list the manufacturer names to filter on
    filter = ['Propellerhead']
    path = inputfile
    combine_files(path, filter, outputfile)


#######################################
# combine_files                       #
# Read selected csv files and combine #
# them into a single tab delimited    #
# file                                #
#######################################

def combine_files(path, filter, outputfile):
    with open(outputfile, 'w', newline='') as output_remotemap:
        for filename in os.listdir(path):
            # only process csv files
            if filename.endswith(".csv"):
                # only process files that contain the filter
                if any(x in filename for x in filter):
                    with open(path + '/' + filename, newline='') as input_remotemap:
                        map_reader = csv.reader(input_remotemap, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        for row in map_reader:
                            write_row(output_remotemap, row)

# Propellerhead Remote Mapping File					
# File Format Version	1.0.0				
# Control Surface Manufacturer	Nektar			
# Control Surface Model	Panorama				
# Map Version	1.3.0			
                       

######################################
# write_row                          #
# This function writes a row of data #
# to the output file with custom     #
# quoting on column 4                #
######################################

def write_row(output_remotemap, row):
    # convert to array
    cols = []
    for col in row:
        cols.append(col)
    i = 0   
    # create custom quoting on column 4 as required
    for col in cols:
        if (i == 0 and 'Map' in col and len(cols) > 3):
            cols[3] = '"' + cols[3] + '"'
        i = i + 1
    # write the array to the file adding delimiter and newline
    outs = ''    
    first = False
    for col in cols:
        if first:
            outs = outs + col + '\t'
            first = True
        else: 
            outs = outs + col + '\t'
    outs = outs + '\r\n'   
    output_remotemap.write(outs)

if __name__ == "__main__":
    main(sys.argv[1:])