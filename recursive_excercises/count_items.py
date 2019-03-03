def recursive_count(arr):
    if (len(arr) == 1):
        return 1
    return 1 + recursive_count(arr[1:])

def test():
    arr = [34, 53, 2345, 254, 254, 25]
    print('Array len function result: {}'.format(len(arr)))
    print('Recursive count result: {}'.format(len(arr)))

test()