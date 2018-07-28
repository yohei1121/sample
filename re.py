#正規表現

import re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)
print(len(matches))

matches = re.findall("beautiful", l, re.IGNORECASE)
print(matches)

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a goog
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

