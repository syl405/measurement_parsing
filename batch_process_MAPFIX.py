import os
import csv
from parse_cmm_data import parse_cmm_data

INPUT_DIR_PATH = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\error_mapping_artifact\\metrology_data\\MAPFIX1\\raw_data\\'
OUTPUT_DIR_PATH = 'D:\\Dropbox (MIT)\\Spring 2017\\NVBOTS Dropbox\\Summer\\error_mapping_artifact\\metrology_data\\MAPFIX1\\parsed_csv\\'

raw_file_list = os.listdir(INPUT_DIR_PATH)
outputs = []

for filename in raw_file_list:
	file_path = INPUT_DIR_PATH + filename
	output = parse_cmm_data(file_path)

	with open(OUTPUT_DIR_PATH+filename[0:-4]+'_parsed.csv','w') as csv_fs:
		fieldnames = ['Specimen Code',
					  'Feature Number',
					  'Flatness',
					  'Z',
					  'XY Parallelism']
		writer = csv.DictWriter(csv_fs,fieldnames)
		writer.writeheader()
		writer.writerows(output)

print 'Successfully parsed.'