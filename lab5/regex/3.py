import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'YES'
        else:
                return('NO')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))