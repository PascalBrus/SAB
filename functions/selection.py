#Selection Sort
def sort(nums, info):
    def selectionSort(nums, info):
        info.tickRecursion()
        for i in range(len(nums)):
            info.tickIteration()
            smallest_idx = i
            for j in range(i + 1, len(nums)):
                info.tickIteration()
                if nums[j] < nums[smallest_idx]:
                    smallest_idx = j
            info.tickAssignment()
            nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
        return nums
    return selectionSort(nums, info)

