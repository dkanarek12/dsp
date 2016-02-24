#PLACE YOUR CODE HERE

import csv
import re
from string import maketrans

def read_data(data):
	f = open(data,'r')
	reader = csv.reader(f)
	faculty = []
	count = 0
	for row in reader:
		if count !=0:
			faculty.append(row)
		else:
			count +=1
	return faculty

def find_frequencies(parsed_data): #returns a histogram of the list of data in a dictionary
	d = dict() 
	for i in parsed_data:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	return d

def degrees_freq(parsed_data):
	d = dict() #dictionary of frequencies with the column header as the key
	for i in parsed_data:
		#regex = re.compile(('.'))
		#x=regex.sub('',i[columnIndex])
		items =i[1].translate(maketrans('',''),'.')
		items = items.split(' ')
		for j in items:
			if j in d:
				d[j] += 1
			elif j not in d and len(j)>1:
				d[j] = 1
	return d

def return_column(parsed_data,columnIndex): #returns a single list of a specified column of the data
	column = []
	for i in parsed_data:
		column.append(i[columnIndex])
	return column

def email_freq(parsed_data):
	emails = return_column(parsed_data,3)
	domains = []
	for x in emails:
		name,dom = x.split('@')
		domains.append(dom)
	return find_frequencies(domains)

def title_freq(parsed_data):
	full_titles = return_column(parsed_data,2)
	titles =[]
	for x in full_titles:
		index = x.find("Biostatistics")
		titles.append(x[:index-4])
	return find_frequencies(titles)
