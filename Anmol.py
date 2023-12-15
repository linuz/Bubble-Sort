import sys,time

input_array=[]
if (len(sys.argv) < 2):
    print ("")  # bug resolved as there is absece of brackets
    print ("Please input list items as arguments")   # bug resolved as there is absece of brackets
    print ("\nExample: ./bubblesort.py <item1> [item2] [item3] [item4] ...")    # bug resolved as there is absece of brackets
    sys.exit()  #quit()
i=1
while (i < len(sys.argv)):
    input_array.append(int(sys.argv[i]))
    i+=1

def bubbleSort(array):
	length=len(array)
	result = True
	global count
	count=0   #intialize count before using it in loop
	while result:
		result = False
		i=0
		while (i < length-1):
			if (array[i] > array[i+1]):
				tempVar = array[i]
				array[i] = array[i+1]
				array[i+1] = tempVar
				result = True
			i=i+1
			count+=1
			print ("Sorting: " + str(array))
	return array
#count = 0    intialized above
time1 = time.time()
arrayResult = (bubbleSort(input_array))
print ("")
print ("Sorted after " + count + " tries.")
print ("Sorted:  " + arrayResult) 
print ("---")
print ("Overall Time: " + (time.time()-time1) + " seconds")
