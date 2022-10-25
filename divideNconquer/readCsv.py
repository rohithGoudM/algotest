import csv

token_set = []
with open('instruments.csv') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',')
	line_count=0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
		elif line_count<=1000:
			symbolObj = {"symbol":row[0]}
			token_set.append(symbolObj)
		line_count += 1
	print(f'Processed {len(token_set)} lines')
print(token_set)