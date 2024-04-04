import random
import time
from Classes import SearchAlgorithms 


#Still need to comment code 


#Part 1 - Function Implementation --> Checking if the functions work, not part of the assignment 
#obj1 = SearchAlgorithms()
#arrGenerated = obj1.generate_array(5)
#print("arrGenerated: " + str(arrGenerated))

#LS_indexStr = obj1.linear_search(arrGenerated,6)
#print("Linear Search --> " + LS_indexStr)


#arrSorted = obj1.quickSort(arrGenerated,0,4)
#print("arrSorted:" + str(arrSorted))

#BS_indexStr = obj1.binary_search(arrGenerated,6)
#print("Binary Search --> " + BS_indexStr)


#Part 2 - Simulation 
#Creating a object of the Search Algoirthms class
obj2 = SearchAlgorithms()

#Asking user for the size of the array to use to generate an array
n = int(input("Array Size: "))
testArr = obj2.generate_array(n)
#Generating a random index that'll hold a random integer 1-10, this will be the target for the simulation
rand_index = random.randint(0,n-1)
rand_num_in_arr = testArr[rand_index]
print("Searching For: " + str(rand_num_in_arr))

#Running a linear search on the array and printing the time 
LS_start = time.time()
print("\nLinear Search Result --> " + obj2.linear_search(testArr,rand_num_in_arr))
LS_end = time.time()
print("Linear Search Time --> " + str(LS_end - LS_start) + " seconds\n")

#Sorting the array and then running a binary search and printing the time 
testArr_Sorted = obj2.quickSort(testArr,0,n-1)
BS_start = time.time()
print("Binary Search Result --> " + obj2.binary_search(testArr_Sorted,rand_num_in_arr))
BS_end = time.time() 
print("Binary Search Time --> " + str(BS_end - BS_start) + " seconds")

#Summary/Results: For the most part their times to run are about the same for smaller arrays (linear seems to be slightly faster), if not very small difference in times and it often varies on the index they're hunting for. 
#         Larger lists/arrays will on average be faster with binary search. But linear search can be faster if it ends up finding the target very early on in the search. 

#Part 3 - Testing and Analysis 
