import csv
def read_file(csv_file):
	with open(csv_file, 'r') as f:
		reader = csv.reader(f)
		f_list = list(reader)

	return(f_list)