import time

def insertion_sort(array, update_func, delay=0.01):
    for i in range(0, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
            update_func(array, ['yellow' if x == j else 'red' if x == i else 'lightblue' for x in range(len(array))])
            time.sleep(delay)
        array[j+1] = key
    update_func(array, ['lightgreen' for _ in range(len(array))])

