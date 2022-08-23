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

t1_start = process_time()
shellSort(arr)
t1_stop = process_time()
print("Elapsed time:", t1_stop, t1_start)    
print("Elapsed time during the whole program in seconds:", (t1_stop-t1_start)) 
#shellSort(arr)
#bubbleSort(arr)
#selectionSort(arr,len(arr))
#quicksort(0, len(arr)-1, arr)