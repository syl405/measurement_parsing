import re

def parse_cmm_data(file_path):
	"""
	Takes a path pointing to a text file in "Print" format from the Micro-Hite CMM.
	Returns a dictionary with relevant flatness, parallelism, and distance measurements.
	"""
	output = {'specimen_code':'',
			  'datum_flatness':0,
			  'col_1_dist':0,
			  'col_1_flatness':0,
			  'col_1_parallelism':0,
			  'col_2_dist':0,
			  'col_2_flatness':0,
			  'col_2_parallelism':0,
			  'col_3_dist':0,
			  'col_3_flatness':0,
			  'col_3_parallelism':0,
			  'col_4_dist':0,
			  'col_4_flatness':0,
			  'col_4_parallelism':0}

	if not type(file_path) == str:
		raise TypeError('Expecting argument of type string.')

	with open(file_path) as fs:
		output['specimen_code'] = re.search('(\d-\d{6}-\d).txt',fs.name).group(1)
		file_contents = fs.read()
	  
	pat_1 = r'==> Plane \(1\)\n\.\.: Flatness\nFlatness\s+(\d\.\d+)'
	pat_3 = r'==> Plane \(3\)\n\.\.: Plane\nZ\s+(\d\.\d+)\nFlatness\s+(\d\.\d+)\n\n\.\.: Parallelism\n.*\nParallelism\s+(\d\.\d+)'
	pat_4 = r'==> Plane \(4\)\n\.\.: Plane\nZ\s+(\d\.\d+)\nFlatness\s+(\d\.\d+)\n\n\.\.: Parallelism\n.*\nParallelism\s+(\d\.\d+)'
	pat_5 = r'==> Plane \(5\)\n\.\.: Plane\nZ\s+(\d\.\d+)\nFlatness\s+(\d\.\d+)\n\n\.\.: Parallelism\n.*\nParallelism\s+(\d\.\d+)'
	pat_6 = r'==> Plane \(6\)\n\.\.: Plane\nZ\s+(\d\.\d+)\nFlatness\s+(\d\.\d+)\n\n\.\.: Parallelism\n.*\nParallelism\s+(\d\.\d+)'

	re_1 = re.compile(pat_1)
	re_3 = re.compile(pat_3)
	re_4 = re.compile(pat_4)
	re_5 = re.compile(pat_5)
	re_6 = re.compile(pat_6)
	
	match_obj = re.search(re_1,file_contents)
	output['datum_flatness'] = match_obj.group(1)

	match_obj = re.search(re_3,file_contents)
	output['col_1_dist'] = match_obj.group(1)
	output['col_1_flatness'] = match_obj.group(2)
	output['col_1_parallelism'] = match_obj.group(3)

	match_obj = re.search(re_4,file_contents)
	output['col_2_dist'] = match_obj.group(1)
	output['col_2_flatness'] = match_obj.group(2)
	output['col_2_parallelism'] =match_obj.group(3)

	match_obj = re.search(re_5,file_contents)
	output['col_3_dist'] = match_obj.group(1)
	output['col_3_flatness'] = match_obj.group(2)
	output['col_3_parallelism'] = match_obj.group(3)

	match_obj = re.search(re_6,file_contents)
	output['col_4_dist'] = match_obj.group(1)
	output['col_4_flatness'] = match_obj.group(2)
	output['col_4_parallelism'] = match_obj.group(3)

	return output