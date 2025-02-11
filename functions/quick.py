#Quick Sort
def sort(nums, info):

  def quickSort(nums, high, low, info):
    info.tick()
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
        quickSort(nums, low, p - 1, info)
        quickSort(nums, p + 1, high, info)
    return nums
  quickSort(nums, info)


# #Quick Sort
# def sort(nums, metrics):
#   metrics.start()
#   def sortQuickPartition(nums, low, high):
#     metrics.tick()
#     pivot = nums[high]
#     i = low
#     for j in range(low, high):
#         if nums[j] < pivot:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#     nums[i], nums[high] = nums[high], nums[i]
#     return i
#   if low < high:
#       p = sortQuickPartition(nums, low, high)
#       sort(nums, low, p - 1)
#       sort(nums, p + 1, high)
#   metrics.end()
#   return nums

# metricCopy = metrics.copy()
# import.sort(nums, metricCopy)
# print.table(metricCopy, nameOfSort)