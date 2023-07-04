s = input()
Roman_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
Roman_2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
counted = s.count('I') * 1 + s.count('V') * 5 + s.count('X') * 10 + s.count('L') * 50 + s.count('C') * 100 + s.count(
    'D') * 500 + s.count('M') * 1000
for key in Roman_2:
    if key in ''.join(s):
        if key == 'IV':
            counted -= 2
        elif key == 'IX':
            counted -= 2
        elif key == 'XL':
            counted -= 20
        elif key == 'XC':
            counted -= 20
        elif key == 'CD':
            counted -= 200
        elif key == 'CM':
            counted -= 200
    else:
        counted = counted
print(counted)
