def SelectionSort(arr, n):
    for i in range(0, n - 1):
        min1 = i
        for j in range(i + 1, n):
            if arr[min1] > arr[j]:
                min1 = j

        arr[min1], arr[i] = arr[i], arr[min1]
    return arr


arr = []
n = int(input("Enter the number of element in array"))
for i in range(0, n):
    ele = int(input(f"Enter the {i} element: "))
    arr.append(ele)

print(f"The Selection Sort is: {SelectionSort(arr, n)}")
