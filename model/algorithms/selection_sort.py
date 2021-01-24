import time 

def selection_sort(array, update_func, delay):
    for i in range(len(array)):
        #find the minimum element to be put in head of array
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
            update_func(array, ['yellow' if _ == j else 'red' if _ == i else 'lightblue' for _ in range(len(array))])
            time.sleep(delay)
        array[i], array[min_idx] = array[min_idx], array[i]
    update_func(array, ['lightgreen' for _ in range(len(array))])
    time.sleep(delay)