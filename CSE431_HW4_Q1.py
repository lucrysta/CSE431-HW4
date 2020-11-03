'''
CSE431 HW4 Q1
Chris/Crystal Lu

Sources:
Insertion sort in python: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
Merge sort in python: https://www.geeksforgeeks.org/merge-sort/

'''
import time
import random
import copy

# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves
 
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1

# initiate unsorted array of n size
ary_ins = list(range(0, 10))
random.shuffle(ary_ins)
ary_mer = copy.deepcopy(ary_ins)

# insertion
start_ins = time.perf_counter() 
insertionSort(ary_ins)
end_ins = time.perf_counter()
diff_ins = end_ins - start_ins

# merge
start_mer = time.perf_counter()
mergeSort(ary_mer)
end_mer = time.perf_counter()
diff_mer = end_mer - start_mer

print(diff_ins, diff_mer)
print(diff_ins - diff_mer)
