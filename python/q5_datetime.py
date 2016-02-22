
# Hint:  use Google to find python function
import time

form1='%m-%d-%Y'
form2='%d-%b-%Y'
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

def toEpoch (d,form):
	return time.mktime(time.strptime(d,form))  

def printDays(start,stop,form):
	print int((toEpoch(stop,form)-toEpoch(start,form))/(60*60*24))

printDays(date_start,date_stop,form1)
####b)  
date_start = '12312013'  
date_stop = '05282015'  

def toForm1(d):
	return d[:2]+'-'+d[2:4]+'-'+d[4:]

printDays(toForm1(date_start),toForm1(date_stop),form1)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 

printDays(date_start,date_stop,form2) 
