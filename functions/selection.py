#Selection Sort
def sort(nums):
   for i in range(len(nums)):
       smallest_idx = i
       for j in range(i + 1, len(nums)):
           if nums[j] < nums[smallest_idx]:
               smallest_idx = j
       nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
   return nums

