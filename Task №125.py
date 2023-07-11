import re
s = str(input())
s = re.sub('[^A-Za-z0-9]+', '', s)
s = s.lower()
s = ''.join(s.split())
print(bool(s == s[::-1]))