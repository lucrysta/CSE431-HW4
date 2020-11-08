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

        k = 200 # k variable to change

        if len(L) <= k:
            insertionSort(L)
        else:
            mergeSort(L) # Sorting the first half
        if len(R) <= k:
            insertionSort(R)
        else:
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

def test():
    # initiate unsorted arrays
    ary_1 = list(range(0, 10))
    ary_2 = list(range(0, 100))
    ary_3 = list(range(0, 1000))
    ary_4 = list(range(0, 10000))
    ary_5 = list(range(0, 100000))
    random.shuffle(ary_1)
    random.shuffle(ary_2)
    random.shuffle(ary_3)
    random.shuffle(ary_4)
    random.shuffle(ary_5)
    
    # merges
    start_1 = time.perf_counter()
    mergeSort(ary_1)
    end_1 = time.perf_counter()
    diff_1 = end_1 - start_1

    start_2 = time.perf_counter()
    mergeSort(ary_2)
    end_2 = time.perf_counter()
    diff_2 = end_2 - start_2

    start_3 = time.perf_counter()
    mergeSort(ary_3)
    end_3 = time.perf_counter()
    diff_3 = end_3 - start_3

    start_4 = time.perf_counter()
    mergeSort(ary_4)
    end_4 = time.perf_counter()
    diff_4 = end_4 - start_4

    start_5 = time.perf_counter()
    mergeSort(ary_5)
    end_5 = time.perf_counter()
    diff_5 = end_5 - start_5


    print("10= {}, 100= {}, 1000= {}, 10000= {}, 100000= {}".format(diff_1, diff_2, diff_3, diff_4, diff_5))
    return[diff_1, diff_2, diff_3, diff_4, diff_5]

n = 250
tests = [0] * 5

for i in range(n):
    ary = test()
    tests[0] += ary[0]
    tests[1] += ary[1]
    tests[2] += ary[2]
    tests[3] += ary[3]
    tests[4] += ary[4]

print("averages: 10^1 {:.3e}, 10^2 {:.3e}, 10^3 {:.3e}, 10^4 {:.3e}, 10^5 {:.3e}".format(tests[0]/n, tests[1]/n, tests[2]/n, tests[3]/n, tests[4]/n))
