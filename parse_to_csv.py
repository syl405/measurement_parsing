import os
import csv
from parse_cmm_data import parse_cmm_data

INPUT_DIR_PATH = r'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\metrology_data\\sc1\\raw_cmm_data\\'
OUTPUT_DIR_PATH = r'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\input_screening_experiment\\metrology_data\\sc1\\'

raw_file_list = os.listdir(INPUT_DIR_PATH)
outputs = []

for filename in raw_file_list:
	file_path = INPUT_DIR_PATH + filename
	output = parse_cmm_data(file_path)
	outputs.append(output)

with open(OUTPUT_DIR_PATH+'parse_raw_data.csv','w') as csv_fs:
	fieldnames = ['specimen_code',
				  'datum_flatness',
				  'col_1_dist',
				  'col_1_flatness',
				  'col_1_parallelism',
				  'col_2_dist',
				  'col_2_flatness',
				  'col_2_parallelism',
				  'col_3_dist',
				  'col_3_flatness',
				  'col_3_parallelism',
				  'col_4_dist',
				  'col_4_flatness',
				  'col_4_parallelism']
	writer = csv.DictWriter(csv_fs,fieldnames)
	writer.writeheader()
	writer.writerows(outputs)

print 'Successfully parsed.'