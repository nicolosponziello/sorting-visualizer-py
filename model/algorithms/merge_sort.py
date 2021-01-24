import time

def merge_sort(array, update_func, delay=0.01):
    if len(array) > 1:
        #find the middle point
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        #recursively sort first half
        merge_sort(left, update_func, delay)
        #recursively sort second half
        merge_sort(right, update_func, delay)

        #merge the halves

        i = 0
        k = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            update_func(array, [])
            time.sleep(delay)
            k += 1

        while i < len(left):
            array[k] = left[i]
            update_func(array, [])
            time.sleep(delay)
            i += 1
            k += 1
    
        while j < len(right):
            array[k] = right[j]
            update_func(array, [])
            time.sleep(delay)
            j += 1
            k += 1
        update_func(array, ['lightgreen' for _ in range(len(array))])