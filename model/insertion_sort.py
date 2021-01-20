import time

def insertion_sort(array, update_callback):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
            update_callback(array, ['yellow' if x == j else 'red' if x == i else 'lightblue' for x in range(len(array))])
        array[j+1] = key
        update_callback(array, ['yellow' if x == j else 'red' if x == i else 'lightblue' for x in range(len(array))])
        time.sleep(0.5)

