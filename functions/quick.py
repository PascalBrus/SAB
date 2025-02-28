#Quick Sort
def sort(nums, info):
  def quickSort(nums, low, high, info):
    info.tickRecursion()
    def sortQuickPartition(nums, low, high):
      info.tickRecursion()
      pivot = nums[high]
      i = low
      for j in range(low, high):
          info.tickIteration()
          if nums[j] < pivot:
              info.tickAssignment()
              nums[i], nums[j] = nums[j], nums[i]
              i += 1
      info.tickAssignment()
      nums[i], nums[high] = nums[high], nums[i]
      return i
    if low < high:
        p = sortQuickPartition(nums, low, high)
        quickSort(nums, low, p - 1, info)
        quickSort(nums, p + 1, high, info)
    return nums
  return quickSort(nums, 0, len(nums)-1, info)