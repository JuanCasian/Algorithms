def sum(arr):
    if (len(arr) == 1):
        return arr[0]
    return arr[0] + sum(arr[1:])

def test():
    arr = [1, 2, 3, 4]
    print('Result of sum: {}'.format(sum(arr)))

test()