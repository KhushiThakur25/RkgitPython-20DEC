arr = [3,11,18,2,41,65]

for i in range(len(arr)):
    min_inx = i
    for j in range(i,len(arr)):
        if arr[min_inx] > arr[j]:
            min_inx = j
    arr[min_inx],arr[i] = arr[i],arr[min_inx]
print(arr)