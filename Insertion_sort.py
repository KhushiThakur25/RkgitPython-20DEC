arr = [18 ,11,5, 3, 6,10]

for i in range(len(arr) - 1):
    j = i+1
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j -= 1
print(arr)