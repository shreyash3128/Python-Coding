def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > temp:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = temp

    return

num_arr = [74, 11, 7, 14, 35]

print("Array before sorting : ", end='')
print(num_arr)

print()

insertion_sort(num_arr)

print("Array After sorting : ", end='')
print(num_arr)