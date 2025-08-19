nums = [12, 45, 3, 67, 89, 23, 14, 56, 78, 90, 11, 5, 34, 66, 27]

max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print(max_num)