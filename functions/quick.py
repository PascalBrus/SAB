#Quick Sort
def sort(nums, low, high):
  def sortQuickPartition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
  if low < high:
      p = sortQuickPartition(nums, low, high)
      sort(nums, low, p - 1)
      sort(nums, p + 1, high)
  return nums

