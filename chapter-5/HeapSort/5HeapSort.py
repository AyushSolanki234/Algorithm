def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = []
n = int(input("Enter the number of element in array: "))
for i in range(0, n):
    ele = int(input(f"Enter the {i} element: "))
    arr.append(ele)
heapSort(arr)
print("\nSorted Array using Heap Sort: ", end = " ")
for i in range(n):
    print(arr[i], end=" ")
