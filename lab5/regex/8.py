import re
text = "PpBestOfTheBest"
print(re.findall('[A-Z][^A-Z]*', text))