import csv
import sys
## file_header  = '/home/matt/Desktop/Projects/InternshipProject/HMDA_DATA_SET/HMDA_'
## file_midler = '/HMDA_LAR_'

def file_converter(input_file, output_file):

    ## Some of the files in this dataset use vertical bars (pipes)
    ## as delimiters for the 
    with open(input_file, 'r', encoding='utf-8') as fin:
        with open(output_file, 'w', encoding='utf-8') as fout:

            ## Read in the sections by pipe
            reader = csv.reader(fin, delimiter='|')

            ## Write out sections by comma (like a normal person)
            writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            writer.writerows(reader)


## I only have to do this for the 2001 to 2006 files, because the rest of them are ok



## for i in range(6):
#input_file  = f"{file_header}{i+2001}{file_midler}{i+2001}.txt"
input_file = sys.argv[1]  
#output_file = f"{file_header}{i+2001}{file_midler}{i+2001}.csv"
output_file = f"{input_file}.output"

print(f"Started file fixer on file:\t {input_file}")
file_converter(input_file, output_file)
print(f"File now converted to:\t\t {output_file}")


##print('\n\nFiles all converted')
