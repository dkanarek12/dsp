def match_ends(words):
	count = 0 
	for i in words:
		if len(i) > 1:
			if i[0]==i[len(i)-1]:
				count += 1
	return count

def front_x(words):
	words.sort()
	list1=[]
	xlist=[]
	count = 0
	for i in words:
		if i[0]=='x':
			xlist.append(i)
		else:
			list1.append(i)
	for j in list1:
		xlist.append(j)
	return xlist

def sort_last(tuples):
	return sorted(tuples, key=lambda t: t[-1])


def remove_adjacent(nums):
	if len(nums) > 0:
		key = nums[0]
		list1=[nums[0]]
	else:
		return []
	for i in nums:
		if i != key:
			key  = i
			list1.append(i)
	return list1

def linear_merge(list1,list2):
	index1 = 0
	index2 = 0
	list3 = []
	while index1 < len(list1) and index2 < len(list2):
		if list1[index1] < list2[index2]:
			list3.append(list1[index1])
			index1+=1
		else:
			list3.append(list2[index2])
			index2+=1
	while index1 < len(list1):
		list3.append(list1[index1])
		index1+=1
	while index2 < len(list2):
		list3.append(list2[index2])
		index2+=1
	return list3


    
