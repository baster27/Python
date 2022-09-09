import random
import time
from functions import quickSort, mergeSort, bubbleSort

def createRandomList(size, max_val):
    ranList = []
    for num in range(size):
        ranList.append(random.randint(1,max_val))
    return ranList

def analyzeFunc (func, arr):
    startTime = time.time()
    func(arr)
    endTime = time.time()
    seconds = endTime - startTime
    print(f"{(func.__name__.capitalize())}\t-> Elapsed time: {seconds:.5f}")

size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))
runTimes = int(input("How many times do you want to run? "))

for n in range(runTimes):
    print(f"Run: {n + 1}")
    lst = createRandomList(size, max)
    analyzeFunc(quickSort, lst)
    analyzeFunc(mergeSort, lst)
    analyzeFunc(bubbleSort, lst.copy())
    analyzeFunc(sorted, lst)
    print("-" * 40)
