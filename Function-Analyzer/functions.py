def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for n in arr:
            if n < pivot:
                smaller.append(n)
            elif n == pivot:
                equal.append(n)
            else:
                larger.append(n)
        return quickSort(smaller) + equal + quickSort(larger)

def mergeSorted(arr1, arr2):
    # print('Merge function called with lists below')
    # print(f'left: {arr1} and right: {arr2}')
    sortedArr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sortedArr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sortedArr.append(arr2[j])
        j += 1
    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = mergeSort(arr[:middle])
        l2 = mergeSort(arr[middle:])
        return mergeSorted(l1,l2)

def bubbleSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for num in range(len(arr)- 1):
            if(arr[num] > arr[num + 1]):
                swapped = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
