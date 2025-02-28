#Insertion Sort
def sort(nums, info):
    def insertionSort(nums, info):
        info.tickRecursion()
        for i in range(len(nums)):
            info.tickIteration()
            j = i
            while j > 0 and nums[j - 1] > nums[j]:
                info.tickIteration()
                info.tickAssignment()
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
        return nums
    return insertionSort(nums, info)