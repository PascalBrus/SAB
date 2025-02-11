#Quick Sort Iterative
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
def sort(arr, low, high):
    def quickSortPartition( arr, low, high):
        i = (low - 1)         
        pivot = arr[high]     
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i + 1)
    if low < high:
        pi = quickSortPartition(arr, low, high)
        sort(arr, low, pi-1)
        sort(arr, pi + 1, high)
    return arr
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
