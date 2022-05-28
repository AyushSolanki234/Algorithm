def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]

        while arr[i-1] > temp and i>0:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i = i-1

    # for i in range(0,len(arr))
    #     print(arr)
    print(arr)

arr = []
n = int(input("Enter the number of element in array"))
for i in range(0,n):
    ele = int(input(f"Enter the {i} element: "))
    arr.append(ele)

print("The Insertion sort array is: ",end=" ")
insertionSort(arr)