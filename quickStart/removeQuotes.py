import sys
import csv

input_file  = sys.argv[1]
output_file = sys.argv[2]

print("-" * 20)
print(f"Removing quotes from {input_file}")

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:


    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        writer.writerow(row)


print(f"Removed quotes from {output_file}")
