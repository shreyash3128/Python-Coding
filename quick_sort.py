def divide(arr, start, end):
    i = start - 1
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        pi = divide(arr, start, end)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)


num_arr = [3, 11, 8, 67, 33, 12, 15, 89]

print("Array before sorting:", num_arr)

quick_sort(num_arr, 0, len(num_arr) - 1)

print("Array after sorting:", num_arr)