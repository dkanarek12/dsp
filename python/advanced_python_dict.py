from advanced_python_regex import *

def sort_names(names):
	return sorted(names, key=lambda t: t[0])

def convert_title(title):
	pattern = r'\s\w{2}\s'
	fullTitle = title					#next three lines shorten the title of the professor
	match =  re.search(pattern,fullTitle)
	return fullTitle[:match.start()]

def convert_degrees(degree):
	l =[]
	deg = re.sub('\.','',degree).lstrip() #removes periods and leading whitespace from the degree
	if len(deg) > 1:
	    return l.append(deg)
	else:
		return 0

def get_info(degree,title,email):
	info=[]
	info.append(degree)
	info.append(convert_title(title))
	info.append(email)
	return info

def create_faculty_dict(parsed_data):
	d = dict()
	for professors in parsed_data:
		name = professors[0].split(' ')[-1]			#name is the last name of the professor
		info = []
		#if convert_degrees(professors[1])!=0 :
		#		info.append(convert_degrees(professors[1]))
		degree = re.sub('\.','',professors[1]).lstrip() #removes periods and leading whitespace from the degree
		if len(degree) > 1:
			info.append(degree)
		info.append(convert_title(professors[2]))							#add abbreivated title to info list
		info.append(professors[3])
		if name in d:
			temp = d[name]
			temp.append(info)
			d[name] = temp
		else:
			d[name]=info
	return d

def create_prof_dict(parsed_data):
	d=dict()
	full_names = []
	for professors in parsed_data:
		(first,last) = professors[0].split(' ')[-1], professors[0].split(' ')[0]
		full_names.append((first,last))
		info = [] 
		degree = re.sub('\.','',professors[1]).lstrip() #removes periods and leading whitespace from the degree
		if len(degree) > 1:
			info.append(degree)
		info.append(convert_title(professors[2]))							#add abbreivated title to info list
		info.append(professors[3])
		if (first,last) in d:
			temp = d[(first,last)]
			temp.append(info)
			d[(first,last)] = temp
		else:
			d[(first,last)]=info
	full_names = sort_names(full_names)
	for name in full_names:
		print str(name) + ' : ' + str(d[name])
	return d

create_prof_dict(read_data('faculty.csv'))