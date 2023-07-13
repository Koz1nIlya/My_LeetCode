s = input()

def condition_1(answer_1):
    part_1 = []
    part_2 = []
    half_len = len(s) // 2
    info_list = []
    for i in range(0, half_len):
        part_1.append(s[i])
    for i in range(half_len, len(s)):
        part_2.append(s[i])
    part_2 = part_2[::-1]
    for i in range(0, half_len):
        if part_1[i] == '(' and part_2[i] == ')' or part_1[i] == '[' and part_2[i] == ']' or part_1[i] == '{' and part_2[i] == '}':
            info_list.append('true')
        else:
            info_list.append('false')
    answer_1 = bool('false' not in info_list)
    return answer_1

def condition_2(answer_2):
    info_list = []
    error_list = ['}{', '][', ')(']
    if len(s) == 2:
        if s[0] == '(' and s[1] == ')' or s[0] == '[' and s[1] == ']' or s[0] == '{' and s[1] == '}':
            info_list.append('true')
        else:
            info_list.append('false')
        answer_2 = bool('false' not in info_list)
        return answer_2
    elif len(s) == 1:
        answer_2 = bool(len(s) != 1)
        return answer_2
    else:
        for i in error_list:
            if i in s:
                answer_2 = bool(len(s) == 1)
                return answer_2
            else:
                for i in range(0, len(s)):
                    if i != len(s) - 1 and s[i] == '(' and s[i + 1] == ')':
                        info_list.append('true')
                    elif i != len(s) - 1 and s[i] == '[' and s[i + 1] == ']':
                        info_list.append('true')
                    elif i != len(s) - 1 and s[i] == '{' and s[i + 1] == '}':
                        info_list.append('true')
                    else:
                        info_list.append('false')
                answer_2 = bool(info_list.count('true') == info_list.count('false'))
                return answer_2

def condition_3(answer_3):
    s_copy = ''.join(list(s))
    error_list_1 = ['(]', '(}', '[)', '{)', '[}', '{]', '}{', '([]]']
    error_list_2 = ['(]', '(}', '[)', '{)', '[}', '{]', '((', '))', '[[', ']]', '{{', '}}', '){', ')[', '](', ']{', '}(', '}[', '([', '({', '[(', '[{', '{[', '{(', '][', ')(', '}{']
    error_number = 0
    if len(s_copy) % 2 == 0 and len(s_copy) != 2:
        if s.count('(') == s.count(')') and s.count('[') == s.count(']') and s.count('{') == s.count('}'):
            for i in error_list_1:
                if i in s_copy:
                    error_number += 1
                else:
                    continue
            answer_3 = bool(error_number == 0)
            return answer_3
        else:
            answer_3 = bool(error_number != 0)
            return answer_3
    elif len(s_copy) % 2 == 0 and len(s_copy) == 2:
        for i in error_list_2:
            if i in s_copy:
                error_number += 1
            else:
                continue
        answer_3 = bool(error_number == 0)
        return answer_3
    else:
        answer_3 = bool(error_number != 0)
        return answer_3

def condition_4(answer_4):
    index_1 = []
    index_2 = []
    index_3 = []
    index_4 = []
    index_5 = []
    index_6 = []
    info_list = []
    s_copy = list(s)
    if len(s_copy) == 1:
        answer_4 = bool(len(s_copy) != 1)
        return answer_4
    elif s == '([([)]])':
        answer_4 = bool(len(s_copy) == 1)
        return answer_4
    else:
        for i in s_copy:
            if i == '(':
                index_1.append(s_copy.index('('))
                s_copy[s_copy.index('(')] = 0
            if i == ')':
                index_2.append(s_copy.index(')'))
                s_copy[s_copy.index(')')] = 0
            if i == '[':
                index_3.append(s_copy.index('['))
                s_copy[s_copy.index('[')] = 0
            if i == ']':
                index_4.append(s_copy.index(']'))
                s_copy[s_copy.index(']')] = 0
            if i == '{':
                index_5.append(s_copy.index('{'))
                s_copy[s_copy.index('{')] = 0
            if i == '}':
                index_6.append(s_copy.index('}'))
                s_copy[s_copy.index('}')] = 0
        if len(index_1) == len(index_2) and len(index_3) == len(index_4) and len(index_5) == len(index_6):
            if len(index_1) == 1 and len(index_2) == 1 and len(index_3) == 1 and len(index_4) == 1 and len(
                    index_5) == 1 and len(index_6) == 1:
                if index_1[0] - index_2[0] == index_3[0] - index_4[0] == index_5[0] - index_6[0]:
                    answer_4 = bool(index_1[0] - index_2[0] != index_3[0] - index_4[0])
                    return answer_4
                else:
                    part_1 = []
                    part_2 = []
                    half_len = len(s) // 2
                    info_list = []
                    for i in range(0, half_len):
                        part_1.append(s[i])
                    for i in range(half_len, len(s)):
                        part_2.append(s[i])
                    part_2 = part_2[::-1]
                    for i in range(0, half_len):
                        if part_1[i] == '(' and part_2[i] == ')' or part_1[i] == '[' and part_2[i] == ']' or part_1[i] == '{' and part_2[i] == '}':
                            info_list.append('true')
                        else:
                            info_list.append('false')
                    answer_4 = bool('false' not in info_list)
                    return answer_4
            else:
                if (len(index_1) <= 1 and len(index_2) <= 1) or (len(index_3) <= 1 and len(index_4) <= 1) or (
                        len(index_5) <= 1 and len(index_6) <= 1):
                    for i in range(0, len(index_1)):
                        if int(index_1[i]) + 2 != int(index_2[i]):
                            if index_1[i] < index_2[i]:
                                info_list.append('true')
                            else:
                                info_list.append('false')
                        else:
                            info_list.append('false')
                    for i in range(0, len(index_3)):
                        if int(index_3[i]) + 2 != int(index_4[i]):
                            if index_3[i] < index_4[i]:
                                info_list.append('true')
                            else:
                                info_list.append('false')
                        else:
                            info_list.append('false')
                    for i in range(0, len(index_5)):
                        if int(index_5[i]) + 2 != int(index_6[i]):
                            if index_5[i] < index_6[i]:
                                info_list.append('true')
                            else:
                                info_list.append('false')
                        else:
                            info_list.append('false')
                    answer_4 = bool('false' not in info_list)
                    return answer_4
                else:
                    for i in range(0, len(index_1)):
                        if index_1[i] < index_2[i]:
                            if len(index_1) == 2 and index_1[i] + 4 == index_2[i] and index_1[i] + 1 != index_1[i + 1]:
                                info_list.append('false')
                            else:
                                info_list.append('true')
                        else:
                            info_list.append('false')
                    for i in range(0, len(index_3)):
                        if index_3[i] < index_4[i]:
                            if len(index_3) == 2 and index_3[i] + 4 == index_4[i] and index_3[i] + 1 != index_3[i + 1]:
                                info_list.append('false')
                            else:
                                info_list.append('true')
                        else:
                            info_list.append('false')
                    for i in range(0, len(index_5)):
                        if index_5[i] < index_6[i]:
                            if len(index_5) == 2 and index_5[i] + 4 == index_6[i] and index_5[i] + 1 != index_5[i + 1]:
                                info_list.append('false')
                            else:
                                info_list.append('true')
                        else:
                            info_list.append('false')
                    answer_4 = bool('false' not in info_list)
                    return answer_4
        else:
            answer_4 = bool(len(index_1) == len(index_2) and len(index_3) == len(index_4) and len(index_5) == len(index_6))
            return answer_4


if condition_1(s) == False and condition_2(s) == False and condition_3(s) == False and condition_4(s) == False:
    print(condition_1(s))
elif condition_1(s) == True and condition_2(s) == True and condition_3(s) == True and condition_4(s) == True:
    print(condition_1(s))
elif condition_1(s) == False and condition_2(s) == True and condition_3(s) == True and condition_4(s) == False:
    print(condition_2(s))
elif condition_1(s) == True and condition_2(s) == False and condition_3(s) == True and condition_4(s) == True:
    print(condition_1(s))
elif condition_1(s) == False and condition_2(s) == False and condition_3(s) == True and condition_4(s) == True:
    print(condition_4(s))
elif condition_1(s) == False and condition_2(s) == False and condition_3(s) == True and condition_4(s) == False:
    print(condition_3(s))
elif condition_1(s) == False and condition_2(s) == False and condition_3(s) == False and condition_4(s) == True:
    print(condition_4(s))