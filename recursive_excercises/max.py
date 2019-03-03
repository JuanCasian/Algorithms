def r_max(arr):
    if (len(arr) == 2):
        return arr[0] if arr[0] >= arr[1] else arr[1]
    tmpMax = max(arr[1:])
    return arr[0] if arr[0] >= tmpMax else tmpMax

def test():
    arr = [4, 1, 2, 6, 24, 3]
    print('Array: {}'.format(arr))
    print('Max result: {}'.format(r_max(arr)))

test()