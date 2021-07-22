'''
sorting.py
Author: Jason Nguyen
module contains all sorting algorithms for sortingVisualizer program
'''

import time

# Insertion Sort
def insertionSort(arr, drawData, increment_comparisons, timeTick):
    start = time.time()
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            increment_comparisons()
            drawData(arr, ['green' if x == j or x == j-1 else 'red' for x in range(len(arr))])
            time.sleep(timeTick)
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            drawData(arr, ['green' if x == j or x == j-1 else 'red' for x in range(len(arr))])
            time.sleep(timeTick)
            j = j - 1
        i = i + 1
    end = time.time()
    drawData(arr, ['green' for x in range(len(arr))])
    return (end - start)

# Selection Sort
def selectionSort(arr, drawData, timeTick):
    pass

    