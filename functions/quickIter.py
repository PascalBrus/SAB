#Quick Sort Iterative
def sort(nums, info):
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
    def quickSortIter(arr, low, high, info):
        info.tickRecursion()
        def quickSortPartition( arr, low, high, info):
            info.tickRecursion()
            i = (low - 1)         
            pivot = arr[high]     
            for j in range(low, high):
                info.tickIteration()
                if arr[j] <= pivot:
                    i += 1
                    info.tickAssignment()
                    arr[i], arr[j] = arr[j], arr[i]
            info.tickAssignment()
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i + 1)
        if low < high:
            pi = quickSortPartition(arr, low, high, info)
            quickSortIter(arr, low, pi-1, info)
            quickSortIter(arr, pi + 1, high, info)
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
        return arr
    return quickSortIter(nums, 0, len(nums) - 1, info)
