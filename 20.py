def find3Numbers(arr):
    result = []
    arr_size = len(arr)
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):

        # Fix the second element as A[j]
        for j in range(i + 1, arr_size - 1):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                temp = []
                if arr[i] + arr[j] + arr[k] == 0:
                    print("Triplet is", arr[i],
                          ", ", arr[j], ", ", arr[k])
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
                    result.append(temp)

    return result


arr = [-25, -10, -7, -3, 2, 4, 8, 10]

arr_size = len(arr)
print(find3Numbers(arr))
