import re

def parse_cmm_data_pc1(file_path):
	"""
	Takes a path pointing to a text file in "Print" format from the Micro-Hite CMM.
	Returns a dictionary with relevant flatness, parallelism, and distance measurements.
	"""
	output = {'specimen_code':'',
			  'datum_flatness':0,
			  'perp_dist':0}

	if not type(file_path) == str:
		raise TypeError('Expecting argument of type string.')

	with open(file_path) as fs:
		output['specimen_code'] = re.search('(PC1-\d+-\d+-R\d).txt',fs.name).group(1)
		file_contents = fs.read()
	  
	pat_1 = r'==> Plane \(1\)\n\.\.: Flatness\nFlatness\s+(\d\.\d+)'
	pat_3 = r'==> Plane \(3\) --> Plane \(1\)\n\.\.: Perpendicular Distance\nPerp. Distance\s+(\d+\.\d+)'

	re_1 = re.compile(pat_1)
	re_3 = re.compile(pat_3)

	match_obj = re.search(re_1,file_contents)
	output['datum_flatness'] = match_obj.group(1)

	match_obj = re.search(re_3,file_contents)
	output['perp_dist'] = match_obj.group(1)

	return output