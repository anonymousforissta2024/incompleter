size = len(arr)
for i in range(size - 2):
    if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
        print(arr[i])