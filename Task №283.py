nums_zero = input()
nums = [int(x) for x in nums_zero]
if nums.count(0) != 0:
    zeros = []
    while nums.count(0) != 0:
        for i in range(1, nums.count(0) + 1):
            zeros.append(0)
            nums.remove(0)
    nums.extend(zeros)
    print(nums)
else:
    print(nums)