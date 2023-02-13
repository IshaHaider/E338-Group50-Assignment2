
import sys
import random
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = improved_func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def improved_func2(array, start, end):
    pivotIndex = random.randint(start, end) 
    array[start], array[pivotIndex] = array[pivotIndex], array[start]
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

if __name__ == '__main__': 

    import json 
    import timeit
    import matplotlib.pyplot as plt

    # Load the json file
    with open("ex2.json", "r") as inFile: 
        content = json.load(inFile)
    
    timearray = []
    arraylen = []

    # iterate through each array and time how long it takes to sort it
    for array in content:
        arraylen.append(len(array))
        tm = timeit.timeit(lambda: func1(array, 0, len(array)-1),number=1)
        timearray.append(tm)
        #print("Time for sorting array of length %d: %f seconds" % (len(array), tm))

    # plot timing results
    plt.scatter(arraylen, timearray)
    plt.xlabel("Length of Array (n)")
    plt.ylabel("Time of Quick Sort (sec)")
    plt.title("Timing Results of Sorting Arrays of Various Lengths")
    plt.show()
    
