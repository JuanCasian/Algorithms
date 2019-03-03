"""
input: (array of items, item you are looking for)

logic:
    divide the input in half every time until you get to the correct answer
"""

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while (low <= high):
        mid = (low + high) / 2
        guess = list[mid]
        if (guess == item):
            return mid
        if (guess > item):
            high = mid - 1
        else:
            low = mid + 1
    return None


def test():
    arr1 = [20, 37, 61, 72, 110, 112, 131, 191, 192, 218, 237, 250, 296, 317, 321, 338, 341, 344, 349, 388, 413, 422, 432, 435, 439, 490, 590, 609, 614, 617, 645, 662, 664, 695, 703, 722, 738, 763, 790, 838, 848, 851, 852, 873, 889, 898, 899, 921, 939, 959]
    arr2 = [74, 75, 89, 92, 135, 181, 208, 235, 253, 319, 321, 393, 405, 413, 423, 425, 443, 486, 491, 495, 510, 512, 519, 525, 547, 560, 562, 573, 584, 607, 623, 638, 662, 668, 670, 678, 716, 730, 795, 797, 821, 835, 853, 894, 903, 912, 923, 930, 958, 966]

    # print('Array #1: {}'.format(arr1))
    print('Result for Array number one looking for 413: {}'.format(binary_search(arr1, 413)))
    # print('Array #2: {}'.format(arr2))
    print('Result for Array number two looking for 413: {}'.format(binary_search(arr2, 716)))

test()