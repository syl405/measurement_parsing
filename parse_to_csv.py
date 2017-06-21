import os
import csv
from parse_cmm_data_pc1 import parse_cmm_data_pc1

INPUT_DIR_PATH = r'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\piecewise_compensation_experiment\\metrology_data\\pc1\\raw_cmm_data\\'
OUTPUT_DIR_PATH = r'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\piecewise_compensation_experiment\\metrology_data\\pc1\\'

raw_file_list = os.listdir(INPUT_DIR_PATH)
outputs = []

for filename in raw_file_list:
	file_path = INPUT_DIR_PATH + filename
	output = parse_cmm_data_pc1(file_path)
	outputs.append(output)

with open(OUTPUT_DIR_PATH+'parsed_raw_data.csv','w') as csv_fs:
	fieldnames = ['specimen_code',
				  'datum_flatness',
				  'perp_dist']
	writer = csv.DictWriter(csv_fs,fieldnames)
	writer.writeheader()
	writer.writerows(outputs)

print 'Successfully parsed.'