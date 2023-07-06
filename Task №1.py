nums = [3, 3]
target = 6
j = 0
final = []
for i in range(-1, len(nums) - 1):
    i += 1
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            final.append(i)
            final.append(j)
print(final)
