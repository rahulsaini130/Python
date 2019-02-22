def sort(nums):
    for x in range(len(nums)-1):
        for y in range(x, len(nums)-1,1):
            temp = 0
            if nums[y] > nums[y+1]:
                temp = nums[y]
                nums[y] = nums[y+1]
                nums[y+1] = temp
    return nums


nums = [12,2,45,5,6,25]
sort(nums)

print(nums)