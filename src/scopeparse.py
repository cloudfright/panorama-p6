#!/usr/bin/python3

import sys
import getopt
import csv

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
        map_writer = csv.writer(output_remotemap, delimiter='\t', quotechar='"')

        with open(inputfile, newline='') as input_remotemap:
            map_reader = csv.reader(input_remotemap, delimiter='\t', quotechar='"')
            # extract the remotemap header
            row = next(map_reader)
            print(row)
            
            while ('Scope' not in row):
                map_writer.writerow(row)
                row = next(map_reader)
                print(row)

                # extact the scope
            #row = next(map_reader)
            while (True):
                if ('Scope' in row and ('Propellerheads' in row or 'Propellerhead Software' in row)):
                    map_writer.writerow(row)
                    row = next(map_reader)
                    while ('Scope' not in row):
                        map_writer.writerow(row)
                        row = next(map_reader)
                else:
                    row = next(map_reader)



if __name__ == "__main__":
    main(sys.argv[1:])#


# http://pymotw.com/2/csv/