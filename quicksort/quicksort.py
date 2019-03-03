def quicksort(arr):
    if (len(arr) < 2):
        return (arr)
    pivot = arr[0]
    smaller = [i for i in arr[1:] if i <= pivot]
    bigger = [i for i in arr[1:] if i > pivot]
    return quicksort(smaller) + [pivot] + quicksort(bigger)

def test():
    arr = [6, 3, 8, 4, 14, 11, 15, 12, 2, 1, 13, 20]
    print('Array: {}'.format(arr))
    print('Sorted Array: {}'.format(quicksort(arr)))

test()