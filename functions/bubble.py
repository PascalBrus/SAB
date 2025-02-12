#Bubble sort
def sort(nums, info):
  def bubbleSort(nums, info):
    swapping = True
    end = len(nums)
    while swapping:
        info.tickIteration()
        swapping = False
        for i in range(1, end):
            info.tickIteration()
            if nums[i - 1] > nums[i]:
                info.tickAssignments()
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums
  bubbleSort(nums, info)

