import csv
with open('files.csv','r') as csv_file:
	lines = csv.reader(csv_file)
	for line in lines:
		print(line)


