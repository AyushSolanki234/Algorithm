def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    M = [0] * n2

    for i in range(0, n1):
        L[i] = arr[p + i]
    for j in range(0, n2):
        M[j] = arr[q + 1 + j]

    # int i, j, k;
    i = 0
    j = 0
    k = p


    while i < n1 and j < n2:
        if L[i] <= M[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = M[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = M[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def display(arr, size):
    for i in range(0, size):
        print(arr[i], end=" ")


arr = []
n = int(input("Enter the number of element in array"))
start = 0
end = n - 1
for i in range(0, n):
    ele = int(input(f"Enter the {i} element: "))
    arr.append(ele)

mergeSort(arr, start, end)
print(f"The Merge Sort is: ")
display(arr, n)
