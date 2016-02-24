#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

def read_data(data):
	f = open(data,'r')
	reader = csv.reader(f)
	league = []
	count = 0
	for row in reader:
		if count !=0:
			team = row
			league.append(team)
		count +=1
	return league


def get_min_score_difference(parsed_data):
	minTeam = ""
	minDiff= 1000
	for team in parsed_data:
		if (int(team[-3]) - int(team[-2])) < minDiff:
			minTeam = team[0]
			minDiff = int(team[-3])-int(team[-2])
	return minTeam

#Go Gunners!
