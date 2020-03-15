import csv
with open('files.csv','r') as excel:
	lines = csv.reader(excel)
	for line in lines:
		print(line.sort())

