'''
sorting.py
Author: Jason Nguyen
module contains all sorting algorithms for sortingVisualizer program
'''

import time
import random
import statistics
from tkinter.constants import W

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


# Quick sort
def partition(itemFromLeft, itemFromRight, medianIndex, arr, drawData, increment_comparisons, timeTick):
    arr[itemFromLeft], arr[medianIndex] = arr[medianIndex], arr[itemFromLeft]
    # index of pivot
    pivot_index = itemFromLeft
    # value of pivot
    pivot = arr[itemFromLeft]

    # itemFromRight and itemFromLeft
    while itemFromLeft < itemFromRight:
        drawData(arr, ['blue' if x == pivot_index else 'green' if x == itemFromLeft or x == itemFromRight else 'red' for x in range(len(arr))])
        time.sleep(timeTick)
        # looking for the itemFromLeft that is greater than or equal to pivot
        while itemFromLeft < len(arr) and arr[itemFromLeft] <= pivot:
            increment_comparisons()
            itemFromLeft += 1
            drawData(arr, ['blue' if x == pivot_index else 'green' if x == itemFromLeft or x == itemFromRight else 'red' for x in range(len(arr))])
            time.sleep(timeTick)
        # looking for the itemFromRight that is less than to pivot
        while arr[itemFromRight] > pivot:
            increment_comparisons()
            itemFromRight -= 1
            drawData(arr, ['blue' if x == pivot_index else 'green' if x == itemFromLeft or x == itemFromRight else 'red' for x in range(len(arr))])
            time.sleep(timeTick)
        # swap itemFromLeft with itemFromRight
        if (itemFromLeft < itemFromRight):
            increment_comparisons()
            arr[itemFromLeft], arr[itemFromRight] = arr[itemFromRight], arr[itemFromLeft]
            drawData(arr, ['blue' if x == pivot_index else 'green' if x == itemFromLeft or x == itemFromRight else 'red' for x in range(len(arr))])
            time.sleep(timeTick)

    # swap itemfromRight with pivot
    arr[itemFromRight], arr[pivot_index] = arr[pivot_index], arr[itemFromRight]
    drawData(arr, ['blue' if x == pivot_index else 'green' if x == itemFromLeft or x == itemFromRight else 'red' for x in range(len(arr))])
    time.sleep(timeTick)

    return itemFromRight


def quickSort(itemFromLeft, itemFromRight, arr, drawData, increment_comparisons, timeTick):
    startTime = time.time()
    if (itemFromLeft < itemFromRight):
        pivot_median = []
        for i in range(3):
            ind = random.randint(itemFromLeft, itemFromRight)
            pivot_median.append(arr[ind])
        median = statistics.median(pivot_median)
        medianIndex = arr.index(median)
        p = partition(itemFromLeft, itemFromRight, medianIndex, arr, drawData, increment_comparisons, timeTick)

        # Sort elements before partition and after partition
        quickSort(itemFromLeft, p-1, arr, drawData, increment_comparisons, timeTick)
        quickSort(p+1, itemFromRight, arr, drawData, increment_comparisons, timeTick)
    
    endTime = time.time()
    drawData(arr, ['green' for x in range(len(arr))])
    return (endTime - startTime)



    