#Quick Sort Iterative 2

def sort(nums, info):
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
    def quickSortIter2(arr, l, h, info):
        def quickSortPation(arr, l, h, info):
            info.tickRecursions()
            i = ( l - 1 )
            x = arr[h]
            for j in range(l, h):
                info.tickIteration()
                if   arr[j] <= x:
                    i = i + 1
                    info.tickAssignment()
                    arr[i], arr[j] = arr[j], arr[i]

            info.tickAssignment()
            arr[i + 1], arr[h] = arr[h], arr[i + 1]
            return (i + 1)
        size = h - l + 1
        stack = [0] * (size)
        top = -1
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = h
        while top >= 0:
            info.tickIteration()
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1
            p = quickSortPation( arr, l, h, info)
            if p-1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1
            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
        return arr
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
### CODE AUS INTERNET KOPIERT
    return quickSortIter2(nums, 0, len(nums)-1, info)   
