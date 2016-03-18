# Matrix Algebra

import numpy as np

A = np.matrix([[1, 2, 3],
     [2, 7, 4]])

B = np.matrix([[1,-1],
     [0, 1]])

C = np.matrix([[5,-1],
     [9, 1],
     [6, 0]])

D = np.matrix([[3,-2,-1],
     [1, 2, 3]])

u = np.array([ 6, 2,-3, 5])

v = np.array([ 3, 5,-1, 4])

w = np.array([[1],
     [8],
     [0],
     [5]])

#1. Matrix Dimensions

print A.shape			#(2,3)
print B.shape			#(2,2)
print C.shape			#(3,2)
print D.shape			#(2,3)
print u.shape			#(1,4)
print w.shape			#(4,1)

#2. Vector Operations

print (u+v)					#[9 7 -4 9]
print (u-v)					#[3 -3 -2 1]
print np.multiply(6,u) 		#[36 12 -18 30]
print np.dot(u,v)			#[18 10 3 20]
print np.linalg.norm(u)		#8.6

#3. Matrix Operations

if A.shape == C.shape:
	print np.add(A,C)							#not defined
else:
	print "not defined"

print np.add(A,(-1*np.transpose(C)))			#[-4 -7 -3],[3 6 4]
print np.add(np.transpose(C),(3*D)) 			#[14 3 3],[2 7 9]
print np.dot(B,A)								#[-1 -5 -1],[2 7 4]

if B.shape[1]==np.transpose(A).shape[0]:
	print np.dot(B,np.transpose(A))				#not defined
else:
	print "not defined"