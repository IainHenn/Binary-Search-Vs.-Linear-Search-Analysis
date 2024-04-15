import random
import time
from Classes import SearchAlgorithms 
import pandas as pd
import plotly.express as px

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
random.seed()
#Asking user for the size of the array to use to generate an array
n = int(input("Array Size: "))
testArr = obj2.generate_array(n)
#Generating a random index that'll hold a random integer 1-10, this will be the target for the simulation
rand_index = random.randint(0,n-1)
rand_num_in_arr = testArr[rand_index]
print("Searching For: " + str(rand_num_in_arr))

#Running a linear search on the array and printing the time 
LS_start = time.time()
print("\nLinear Search Result --> " + str(obj2.linear_search(testArr,rand_num_in_arr)))
LS_end = time.time()
print("Linear Search Time --> " + str(LS_end - LS_start) + " seconds\n")

#Sorting the array and then running a binary search and printing the time 
testArr_Sorted = obj2.quickSort(testArr,0,n-1)
BS_start = time.time()
print("Binary Search Result --> " + str(obj2.binary_search(testArr_Sorted,rand_num_in_arr)))
BS_end = time.time() 
print("Binary Search Time --> " + str(BS_end - BS_start) + " seconds")

#Summary/Results: For the most part their times to run are about the same for smaller arrays (linear seems to be slightly faster), if not very small difference in times and it often varies on the index they're hunting for. 
#         Larger lists/arrays will on average be faster with binary search. But linear search can be faster if it ends up finding the target very early on in the search. 


def measure_execution_time_for_searches_LS(obj,array,num_searches):
    start_time = time.time()
    for i in range(num_searches):
        target = random.randint(0,320000)
        index_LS = obj.linear_search(array,target)
    end_time = time.time()
    return end_time - start_time

def measure_execution_time_for_searches_BS(obj,array,num_searches):
    start_time = time.time()
    array_sorted = obj.count_sort(array)
    for i in range(num_searches):
        target = random.randint(0,320000)
        index_BS = obj.binary_search(array_sorted,target)
    end_time = time.time()
    return end_time - start_time

#Part 3 - Testing and Analysis 

obj3 = SearchAlgorithms()
n = int(input("Array Size (LS): "))
testArr_LS = obj3.generate_array(n)
num_searches_list_LS = range(1,10001,50)
execution_times_LS = []

for num_searches in num_searches_list_LS:
    execution_time = measure_execution_time_for_searches_LS(obj3,testArr_LS,num_searches)
    execution_times_LS.append(execution_time)

obj4 = SearchAlgorithms()
n = int(input("Array Size (BS): "))
testArr_BS = obj4.generate_array(n)
num_searches_list_BS = range(1,10001,50)
execution_times_BS = []

for num_searches in num_searches_list_BS:
    execution_time = measure_execution_time_for_searches_BS(obj4,testArr_BS,num_searches)
    execution_times_BS.append(execution_time)

d_LS = {'num_searches':num_searches_list_LS, 'execution_time':execution_times_LS}
df_LS = pd.DataFrame(data = d_LS)
d_BS = {'num_searches':num_searches_list_BS, 'execution_time':execution_times_BS}
df_BS = pd.DataFrame(data = d_BS)

LR_LS = px.scatter(x = df_LS["num_searches"], y = df_LS["execution_time"], labels = {
    "x" : "Number Of Searches",
    "y" : "Execution Time (seconds)"
}, title = "Number Of Searches Vs. Execution Time (seconds) For Linear Search")
LR_LS.show()

LR_BS = px.scatter(x = df_BS["num_searches"], y = df_BS["execution_time"],labels = {
    "x" : "Number Of Searches",
    "y" : "Execution Time (seconds)"
}, title = "Number Of Searches Vs. Execution Time (seconds) For Binary Search")
LR_BS.show()



def measure_execution_time_for_arraySize_BS(obj,array):
    start_time = time.time()
    target = random.randint(0,320000)
    array_sorted = obj.count_sort(array)
    start_time = time.time()
    index_BS = obj.binary_search(array_sorted,target)
    end_time = time.time()
    return end_time - start_time

obj5 = SearchAlgorithms()
num_array_list_BS = range(1,100001,50)
array_execution_times_BS = []

for array_size in num_array_list_BS:
    array = obj5.generate_array(array_size)
    execution_time = measure_execution_time_for_arraySize_BS(obj5,array)
    array_execution_times_BS.append(execution_time)


def measure_execution_time_for_arraySize_LS(obj,array):
    start_time = time.time()
    target = random.randint(0,320000)
    index_LS = obj.linear_search(array,target)
    end_time = time.time()
    return end_time - start_time

obj6 = SearchAlgorithms()
num_array_list_LS = range(1,100001,50)
array_execution_times_LS = []

for array_size in num_array_list_LS:
    array = obj6.generate_array(array_size)
    execution_time = measure_execution_time_for_arraySize_LS(obj6,array)
    array_execution_times_LS.append(execution_time)

d_BS_arrays = {'num_array':num_array_list_BS, 'execution_time':array_execution_times_BS}
df_BS_arrays = pd.DataFrame(data = d_BS_arrays)
d_LS_arrays = {'num_array':num_array_list_LS, 'execution_time':array_execution_times_LS}
df_LS_arrays = pd.DataFrame(data = d_LS_arrays)

LR_LS_arrays = px.scatter(x = df_LS_arrays["num_array"], y = df_LS_arrays["execution_time"], labels = {
    "x" : "Array Size",
    "y" : "Execution Time (seconds)"
}, title = "Array Size Vs. Execution Time (seconds) For Linear Search")
LR_LS_arrays.show()

LR_BS_arrays = px.scatter(x = df_BS_arrays["num_array"], y = df_BS_arrays["execution_time"],labels = {
    "x" : "Array Size",
    "y" : "Execution Time (seconds)"
}, title = "Array Size Vs. Execution Time (seconds) For Binary Search")
LR_BS_arrays.show()