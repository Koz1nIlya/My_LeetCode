s = input()
# I II III IV V VI VII VIII XI X XI XII XIII XIV XV XVI XVII XVIII XIX XX

s = list(s)
M_number_all = 0
D_number_all = 0
C_number_all = 0
L_number_all = 0
X_number_all = 0
V_number_all = 0
I_number_all = 0
all_counted_1 = 0
all_counted_2 = 0

M_number = s.count("M")
M_number_all = M_number * 1000
D_number = s.count("D")
D_number_all = D_number * 500
C_number = s.count("C")
C_number_all = C_number * 100
L_number = s.count("L")
L_number_all = L_number * 50
X_number = s.count("X")
X_number_all = X_number * 10
V_number = s.count("V")
V_number_all = V_number * 5
I_number = s.count("I")
I_number_all = I_number * 1


def minus_one():
    all_counted_1 = M_number_all + D_number_all + C_number_all + L_number_all + X_number_all + V_number_all + I_number_all
    if "CD" in ''.join(s) or "CM" in ''.join(s):
        all_counted_1 = all_counted_1 - 200
        pass
    if "XL" in ''.join(s) or "XC" in ''.join(s):
        all_counted_1 = all_counted_1 - 20
        pass
    if "IV" in ''.join(s) or "IX" in ''.join(s):
        all_counted_1 = all_counted_1 - 2
        pass
    print(all_counted_1)


def nothing_minus_one():
    all_counted_2 = M_number_all + D_number_all + C_number_all + L_number_all + X_number_all + V_number_all + I_number_all
    print(all_counted_2)


if "CD" in ''.join(s) or "CM" in ''.join(s) or "XL" in ''.join(s) or "XC" in ''.join(s) or "IV" in ''.join(
        s) or "IX" in ''.join(s):
    minus_one()
else:
    nothing_minus_one()
