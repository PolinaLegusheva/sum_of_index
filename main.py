def enumeration(arr, sum):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                return i, j


m = [1, 18, 6, -3, 4]
sum = 7
result = enumeration(m, sum)
print(result)
