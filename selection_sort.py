def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

    return arr

num_arr = [74, 11, 7, 14, 35]

print("Array before sorting : ", end='')
print(num_arr)

print()

selection_sort(num_arr)

print("Array After sorting : ", end='')
print(num_arr)