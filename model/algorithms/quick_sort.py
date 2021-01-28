import time

def find_pivot(array, update_func, delay, low, high):
    pivot = array[high]
    i = low-1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            update_func(array, ['yellow' if _ == pivot else 'lightblue' for _ in range(len(array))])
            time.sleep(delay)
            
    tmp = array[i+1]
    array[i+1] = array[high]
    array[high] = tmp

    return i+1


def quicksort(array, low, high, update_func, delay):
    if low < high:
        pivot = find_pivot(array, update_func, delay, low, high)
        quicksort(array, low, pivot-1, update_func, delay)
        quicksort(array, pivot + 1, high, update_func, delay)
