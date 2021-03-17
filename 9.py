def binary_search(arr, low, high, x1):
    if high >= low:

        mid = (high + low) // 2
        if arr[mid] == x1:
            return mid
        elif arr[mid] > x1:
            return binary_search(arr, low, mid - 1, x1)
        else:
            return binary_search(arr, mid + 1, high, x1)

    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = int(input("enter the number: "))

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
