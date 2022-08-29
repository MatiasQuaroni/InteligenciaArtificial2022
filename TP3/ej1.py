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
def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
  
def quicksort(l, r, nums):
    if len(nums) == 1:  
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums) 
    return nums
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

bs_start = process_time()
bubbleSort(arr)
bs_stop = process_time() 
print("Elapsed time during the bubblesort in seconds:", (bs_stop-bs_start)) 

ss_start = process_time()
selectionSort(arr,len(arr))
ss_stop = process_time()   
print("Elapsed time during selectionsort in seconds:", (ss_stop-ss_start)) 

shs_start = process_time()
shellSort(arr)
shs_stop = process_time()   
print("Elapsed time during the shellsort in seconds:", (shs_stop-shs_start)) 

qs_start = process_time()
quicksort(0, len(arr)-1, arr)
qs_stop = process_time()   
print("Elapsed time during the quicksort in seconds:", (qs_stop-qs_start)) 

#shellSort(arr)
#bubbleSort(arr)
#selectionSort(arr,len(arr))
#quicksort(0, len(arr)-1, arr)