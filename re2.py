import re

string = "Two too."
m = re.findall("t[wo]o", string, re.IGNORECASE)
print(m)

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)
