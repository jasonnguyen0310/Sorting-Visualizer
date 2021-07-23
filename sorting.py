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
def selectionSort(arr, drawData, increment_comparisons, timeTick):
    start = time.time()
    for i in range(len(arr)):
        min_idx = i 
        for j in range(i+1, len(arr)):
            drawData(arr, ['blue' if x == i else 'green' if x == min_idx or x == j else 'red' for x in range(len(arr))])
            time.sleep(timeTick)
            if arr[min_idx] > arr[j]:
                increment_comparisons()
                min_idx = j
                drawData(arr, ['blue' if x == i else 'green' if x == min_idx or x == j else 'red' for x in range(len(arr))])
                time.sleep(timeTick)
        temp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = temp
        drawData(arr, ['blue' if x == i else 'green' if x == min_idx or x == j else 'red' for x in range(len(arr))])
        time.sleep(timeTick)
    end = time.time()
    drawData(arr, ['green' for x in range(len(arr))])
    return (end - start)

    