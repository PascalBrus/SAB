#Merge Sort
def sort(nums):
    def sortMergeHelp(first, second):
        final = []
        i = 0
        j = 0
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1
        while i < len(first):
            final.append(first[i])
            i += 1
        while j < len(second):
            final.append(second[j])
            j += 1
        return final
    if len(nums) < 2:
        return nums
    sorted_left_side = sort(nums[: len(nums) // 2])
    sorted_right_side = sort(nums[len(nums) // 2 :])
    return sortMergeHelp(sorted_left_side, sorted_right_side)

