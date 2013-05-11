#!/usr/bin/python
#############################################################
# Bubblesort for Python                                     #
# by: Dennis Linuz <dennismald@gmail.com>                   #
# Demonstration of a bubble 	sort	                    #
#############################################################

import sys,time

input_array=[]
if (len(sys.argv) < 2):
    print ""
    print "Please input list items as arguments"
    print "\nExample: ./bubblesort.py <item1> [item2] [item3] [item4] to be sorted ..."
    quit()
i=1
while (i < len(sys.argv)):
    input_array.append(int(sys.argv[i]))
    i+=1

def bubbleSort(array):
	length=len(array)
	result = True
	global count
	while result:
		result = False #after one pass result becomes false hence program starts scanning begining
		i=0
		while (i < length-1):
			if (array[i] < array[i+1]):	# starts sorting first 2 valuesfrom start of array.
				tempVar = array[i+1]  	#tempVar is used for swapping.
				array[i] = array[i+1]
				array[i+1] = tempVar    #if first element is larger than second element then swapping is done.
				result = True
			i=i+1
			count+=1			#count is used for no. of passes (steps).
			print "Sorting: " + str(array)
	return array
count = 0
time1 = time.time()
arrayResult = str(bubbleSort(input_array))
print ""
print "Sorted after " + str(count) + " tries."
print "Sorted:  " + arrayResult 
print "---"
print "Overall Time: " + str(time.time()-time1) + " seconds"	#time required for bubble sorting.
