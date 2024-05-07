def quickSort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)

def partition(arr,low,high):
    pivot = arr[low]
    i = low+1
    j = high

    while i<=j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j

arr = [10,7,8,9,2,5]
n = len(arr)
quickSort(arr, 0 , n-1)
print(arr)
