#チャレンジ17章

import re

string = "zoo is good"

matches = re.findall(".*o.", string, re.IGNORECASE)
print(matches)
