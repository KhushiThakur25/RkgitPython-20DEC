def merge_sort(arr):
    if arr is None or len(arr) <= 1:
        return

    def merge(arr,low,mid,high):
        temp = arr.copy()
        i = low
        j = mid+1
        k = low
        while i <= mid and j <= high:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
            k += 1
        while i <= mid:
            arr[k] = temp[i]
            k += 1
            i += 1
    def merge_sort_div(arr,low,high):
        if low < high:
            mid = low + (high - low)//2
            merge_sort_div(arr,low,mid)
            merge_sort_div(arr,mid+1,high)
            merge(arr,low,mid,high)
    
    merge_sort_div(arr,0,len(arr)-1)

arr = [5,6,3,2,2,14,5,1]
merge_sort(arr)
print(arr)