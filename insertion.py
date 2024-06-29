def insertionSort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key

    print(x)

insertionSort([9, 5, 1, 4, 3])