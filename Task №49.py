import re

strs = list(input())
new_list = []
list_of_words = []
not_permanent_list = []
second_word = []
length = 0
answer = 0
none_list = []
for word in strs:
    if word != ',':
        new_list.append(word)
    else:
        length = len(new_list)
        break
strs = re.sub('[^A-Za-z0-9]+', '', ''.join(strs))
diapazon = len(strs) // length
for i in range(0, len(strs), length):
    print(i)
    if i != len(strs) - length:
        for word in range(i, length + i):
            if i != len(strs) - length:
                not_permanent_list.append(strs[word])
                if len(not_permanent_list) == length:
                    list_of_words.append(''.join(not_permanent_list))
                    not_permanent_list = []
    else:
        for word in range(i, length + i):
            not_permanent_list.append(strs[word])
            if len(not_permanent_list) == length:
                list_of_words.append(''.join(not_permanent_list))
                not_permanent_list = []
for i in list_of_words:
    for j in range(0, len(i)):
        not_permanent_list.append(i[j])
        
print(list_of_words)
print(not_permanent_list)