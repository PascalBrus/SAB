#Merge Sort
def sort(nums, info):

    def mergeSort(nums, info):
        info.tickRecursion()
        def mergeSortHelp(first, second):
            info.tickRecursion()
            final = []
            i = 0
            j = 0
            while i < len(first) and j < len(second):
                info.tickIteration()
                if first[i] <= second[j]:
                    info.tickAssignment()
                    final.append(first[i])
                    i += 1
                else:
                    info.tickAssignment()
                    final.append(second[j])
                    j += 1
            while i < len(first):
                info.tickIteration()
                info.tickAssignment()
                final.append(first[i])
                i += 1
            while j < len(second):
                info.tickIteration()
                info.tickAssignment()
                final.append(second[j])
                j += 1
            return final
        if len(nums) < 2:
            return nums
        sorted_left_side = mergeSort(nums[: len(nums) // 2], info)
        sorted_right_side = mergeSort(nums[len(nums) // 2 :], info)
        return mergeSortHelp(sorted_left_side, sorted_right_side)
    return mergeSort(nums, info)