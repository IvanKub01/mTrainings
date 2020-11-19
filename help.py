import re

print(".....")
colors = '  red   ggg  '
colors = re.sub("^\\s+|\\s+$", "", colors, flags=re.UNICODE)

print(colors)
print(".....")