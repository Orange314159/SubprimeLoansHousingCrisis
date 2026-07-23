import csv
import sys

input_file  = sys.argv[1]
output_file = sys.argv[2]

def file_converter(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as fin:
        with open(output_file, 'w', encoding='utf-8') as fout:
            reader = csv.reader(fin, delimiter='|')
            writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(reader)

print("-" * 30)
print(f"Converting {input_file}")
file_converter(input_file, output_file)
print(f"Converted {output_file}")
