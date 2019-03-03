def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr, sortingFunc):
    newArr = []
    for i in range(len(arr)):
        target = sortingFunc(arr)
        newArr.append(arr.pop(target))
    return (newArr)

def test():
    unsortedArr = [14, 13, 20, 11, 7]
    print('Unsorted Array: {}'.format(unsortedArr))
    sortedArr = selection_sort(unsortedArr, findSmallest)
    print('Sorted Array: {}'.format(sortedArr))

test()