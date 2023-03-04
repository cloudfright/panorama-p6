#!/usr/bin/python3

import sys
import getopt
import csv

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg


    with open(inputfile, newline='') as input_remotemap:
        map_reader = csv.reader(input_remotemap, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # create a new file which contains only the scope

        for row in map_reader:
            if ('Scope' in row):
                scope = []
                unique_id = make_safe_filename(f"{row[1]}_{row[2]}")
                out_filename = f"./csv/{unique_id}.csv"
                
                # build the scope
                while(True):
                    scope.append(row)
                    row = next(map_reader)
                    if ('Scope' in row):
                        break
                write_scope(out_filename, scope)


def make_safe_filename(s):
    return "".join(c for c in s if c.isalnum())

# write the scope to a file
def write_scope(filename, scope):
    with open(filename, 'w', newline='') as output_scope:
        map_writer = csv.writer(output_scope, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in scope:
            map_writer.writerow(row)

if __name__ == "__main__":
    main(sys.argv[1:])