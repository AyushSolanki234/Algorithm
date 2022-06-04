def partition(arr, low, high):
    i = (low - 1)
    piv = arr[high]

    for j in range(low, high):
        if arr[j] <= piv:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = []
n = int(input("Enter the number of element in array"))
for i in range(0, n):
    ele = int(input(f"Enter the {i} element: "))
    arr.append(ele)

quickSort(arr,0,n-1)
print("\nSorted array using QuickSort: ",end=" ")
for i in range(n):
    print(arr[i],end=" ")
