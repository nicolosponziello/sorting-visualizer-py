import time

def bubble_sort(array, update_func, delay):
    length = len(array)
    for i in range(length-1):
        for j in range(length-1):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
                update_func(array, ['yellow' if _ == j else 'red' if _ == j+1 else 'lightblue' for _ in range(length)])
                time.sleep(delay)