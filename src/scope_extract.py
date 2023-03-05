#!/usr/bin/python3

import sys
import getopt
import csv

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

    with open(outputfile, 'w', newline='') as output_remotemap:
       
        with open(inputfile, newline='') as input_remotemap:
            map_reader = csv.reader(input_remotemap, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # extract the remotemap header
            row = next(map_reader)
            
            while ('Scope' not in row):
                #map_writer.writerow(row)
                write_row(output_remotemap, row)
                row = next(map_reader)

                # extact the scope
            #row = next(map_reader)
            while (True):
                if ('Scope' in row and ('Propellerheads' in row or 'Propellerhead Software' in row)):
                    write_row(output_remotemap, row)
                    row = next(map_reader)
                    while ('Scope' not in row):
                        write_row(output_remotemap, row)
                        row = next(map_reader)
                else:
                    row = next(map_reader)

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