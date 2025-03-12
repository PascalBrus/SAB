#Quick Sort
def sort(nums, info):
    def lt(x): 
        return lambda y: y < x

    #greater than or equals
    def gte(x):
        return lambda y: y >= x
    
    def filter2(nums, function):
        return [x for x in nums if function(x)]
    
    def quick_sort(nums):
        info.tickRecursion()  
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        info.tickAssignment()
        left = filter2(nums[1:], lt(pivot))
        right = filter2(nums[1:], gte(pivot))
        return quick_sort(left) + [pivot] + quick_sort(right)

    return quick_sort(nums)