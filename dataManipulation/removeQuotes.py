import sys


## input_file  = "/home/matt/Desktop/Projects/InternshipProject/LoanData/HMDA_DATA_SET/HMDA_2009/hmda_2009_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv"
input_file = sys.argv[1]

## output_file = "/home/matt/Desktop/Projects/InternshipProject/LoanData/HMDA_DATA_SET/HMDA_2009/HMDA_2009.csv"
output_file = f"{input_file}.clean"

import os
import csv


with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    # Let Python auto-detect dialect and unquote fields safely
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        writer.writerow(row)

os.replace(output_file, input_file)
