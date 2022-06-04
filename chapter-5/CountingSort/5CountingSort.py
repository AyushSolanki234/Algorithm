def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


arr = []
n = int(input("Enter the number of element in array"))
for i in range(0, n):
    ele = int(input(f"Enter the {i} element: "))
    arr.append(ele)

countingSort(arr)
print("\nSorted Array using Counting Sort: ", end = " ")
print(arr)