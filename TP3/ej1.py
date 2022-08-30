from numpy import random
from time import process_time
#bubbleSort
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return

#selectionSort
def selectionSort(array, size):    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
#quickSort
def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:  
        return array
#shellSort
def shellSort(arr): 
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):

            temp = arr[i]

            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr = random.randint(100, size=(1024))
arr1 = random.randint(100, size=(1024))
arr2 = random.randint(100, size=(1024))
arr3 = random.randint(100, size=(1024))

bs_start = process_time()
bubbleSort(arr)
bs_stop = process_time() 
print("Elapsed time during the bubblesort in seconds:", (bs_stop-bs_start)) 

ss_start = process_time()
selectionSort(arr1,len(arr1))
ss_stop = process_time()   
print("Elapsed time during selectionsort in seconds:", (ss_stop-ss_start)) 

shs_start = process_time()
shellSort(arr2)
shs_stop = process_time()   
print("Elapsed time during the shellsort in seconds:", (shs_stop-shs_start)) 

qs_start = process_time()
quicksort(arr3)
qs_stop = process_time()   
print("Elapsed time during the quicksort in seconds:", (qs_stop-qs_start)) 

#shellSort(arr)
#bubbleSort(arr)
#selectionSort(arr,len(arr))
#quicksort(0, len(arr)-1, arr)