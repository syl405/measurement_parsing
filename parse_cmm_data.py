import re

def parse_cmm_data(file_path):
	"""
	Takes a path pointing to a text file in "Print" format from the Micro-Hite CMM.
	Returns a list of dictionaries with relevant flatness, parallelism, and distance measurements.
	"""
	output = {'specimen_code':''}

	if not type(file_path) == str:
		raise TypeError('Expecting argument of type string.')

	with open(file_path) as fs:
		output['specimen_code'] = '3D-MAP-01'
		file_contents = fs.read()
	
	pat_f = r'==> Plane \('
	pat_r = r'\)\n\.\.: Plane\nZ\s+(\d+\.\d+)\nFlatness\s+(\d+\.\d+)\n\n\.\.: Parallelism\n.*\nParallelism\s+(\d+\.\d+)'

	outputs = []

	# Match datum A
	match_obj = re.search(r'==> Plane \(6\)\n\.\.: Parallelism\nDatum Plane\s+XY\nParallelism\s+(\d+\.\d+)',file_contents)
 
	# Match column top surfaces
	for i in range(7,196,1):
		pat = pat_f+str(i)+pat_r
		match_obj = re.search(pat,file_contents)

		if match_obj:
			outputs.append({'Specimen Code': '3D-MAP-01_ver1',
							'Feature Number': i,
							'Z': match_obj.group(1),
							'Flatness': match_obj.group(2),
							'XY Parallelism': match_obj.group(3)})

	return outputs