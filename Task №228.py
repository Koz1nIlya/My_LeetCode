nums = input()
nums_int = [int(i) for i in nums]
nums_int_copy = list.copy(nums_int)
error = 0

if len(nums) == 0:
    print()
elif len(nums) == 1:
    print(list(map(str, nums)))
else:
    compare_number = [nums_int[0]]
    answer = [nums_int[0], nums_int[0]]
    if nums_int[0] + 1 == nums_int[1]:
        for i in range(0, len(nums_int) - 1):
            if nums_int[i] + 1 == nums_int[i + 1]:
                if error >= 1:
                    answer.append(nums_int[i + 1])
                    compare_number[0] = nums_int[i + 1]
                    answer.insert(-1, '->')
                else:
                    answer[-1] = nums_int[i + 1]
                    compare_number[0] = nums_int[i + 1]
                error = 0
            else:
                answer.append(nums_int[i + 1])
                compare_number[0] = nums_int[i + 1]
                error += 1
        if answer[0] == answer[1]:
            answer.remove(answer[0])
        answer.insert(1, '->')
    else:
        for i in range(0, len(nums_int) - 1):
            if nums_int[i] + 1 == nums_int[i + 1]:
                if error >= 1:
                    answer.append(nums_int[i + 1])
                    compare_number[0] = nums_int[i + 1]
                    answer.insert(-1, '->')
                else:
                    answer[-1] = nums_int[i + 1]
                    compare_number[0] = nums_int[i + 1]
                error = 0
            else:
                answer.append(nums_int[i + 1])
                compare_number[0] = nums_int[i + 1]
                error += 1
        answer.append(nums_int[-1])
        if answer[0] == answer[1]:
            answer.remove(answer[0])

    final_answer = []
    if nums_int[0] + 1 != nums_int[1]:
        final_answer.append(str(answer[0]))
        for i in range(1, len(answer) - 1):
            if answer[i] == '->':
                final_answer.append(str(answer[i - 1]) + '->' + str(answer[i + 1]))
            elif answer[i + 1] != '->' and answer[i - 1] != '->':
                final_answer.append(str(answer[i]))
            else:
                continue
    elif nums_int[-2] + 1 != nums_int[-1]:
        for i in range(1, len(answer) - 1):
            if answer[i] == '->':
                final_answer.append(str(answer[i - 1]) + '->' + str(answer[i + 1]))
            elif answer[i + 1] != '->' and answer[i - 1] != '->':
                final_answer.append(str(answer[i]))
            else:
                continue
        final_answer.append(str(answer[-1]))
    elif nums_int[0] + 1 != nums_int[1] and nums_int[-2] + 1 != nums_int[-1]:
        final_answer.append(str(answer[0]))
        for i in range(1, len(answer) - 1):
            if answer[i] == '->':
                final_answer.append(str(answer[i - 1]) + '->' + str(answer[i + 1]))
            elif answer[i + 1] != '->' and answer[i - 1] != '->':
                final_answer.append(str(answer[i]))
            else:
                continue
        final_answer.append(str(answer[-1]))
    else:
        for i in range(1, len(answer) - 1):
            if answer[i] == '->':
                final_answer.append(str(answer[i - 1]) + '->' + str(answer[i + 1]))
            elif answer[i + 1] != '->' and answer[i - 1] != '->':
                final_answer.append(str(answer[i]))
            else:
                continue

    print(final_answer)
