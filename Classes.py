import random 
import time 

class SearchAlgorithms: 
    #Generates an array taking in a size for the array
    def generate_array(self,size):
        #Generates a random seed to get a random number each time
        random.seed()
        #Creating an empty array to then append integers (each integer is a random number 1-10), n times (n being the size of the array)
        array = []
        for i in range(size):
            array.append(random.randint(0,320000))
        return array
    
    #Searches through the array for the target number, traversing each index until it reaches it (if it does it returns the index found at). If the search fails then it returns -1 as the index.
    def linear_search(self,array, target):
        #For each integer in the array
        for i in range(len(array)):
            #If the target is found at index i, return i
            if array[i] == target:
                return (i)
        #If the target isn't found in the array, return -1
        return (-1)
    
    #Searches a sorted array for the target, creates a midpoint (index of the middle of the array) and keeps halving the array until we get to the target, if we can't find the target then it returns -1
    def binary_search(self,array,target):
        #Assigning lower index as the start of the array, upper index as the end of the array
        lower = 0
        upper = len(array)-1
        found = False
        #While we haven't found the target
        while(found == False):
            #if the upper index is less than the lower index, return -1 
            if upper < lower:
                return (-1)
            
            #Generating the midpoint 
            mp = int(lower + (upper - lower) / 2)

            #if the number at the midpoint is less than the target, look at the greater half of the array
            if array[mp] < target:
                lower = mp + 1
            
            #if the number at the midpoint is greater than the target, look at the less half of the array
            elif array[mp] > target:
                upper = mp - 1
            
            #if the number at the midpoint is the target, return the index of the target 
            else:
                return (mp)
            
    
    #Partition and quicksort function are personal implementations to sort the array for binary search, not needed for assignment 
    def partition(self, array, low, high):
        pivot = array[high]
        i = (low-1)
        for j in range(low,high):
            if array[j] <= pivot:
                i = i + 1
                (array[i],array[j]) = (array[j],array[i])
        (array[i+1],array[high]) = (array[high],array[i+1])
        return (i+1)


    def quickSort(self,array, low, high):
        if low < high:
            partitionIndex = self.partition(array,low,high)
            self.quickSort(array,low,partitionIndex-1)
            self.quickSort(array,partitionIndex+1,high)
        return array
    
    #Using Counting Sort for sorting for part 3
    def count_sort(self,input_array):
        M = max(input_array)
        count_array = [0] * (M+1)
        for num in input_array:
            count_array[num] += 1
        for i in range(1,M+1):
            count_array[i] += count_array[i-1]
        output_array = [0] * len(input_array)
        for i in range(len(input_array)-1,-1,-1):
            output_array[count_array[input_array[i]]-1] = input_array[i]
            count_array[input_array[i]] -= 1
        return output_array