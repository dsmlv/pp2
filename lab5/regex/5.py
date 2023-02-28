import re
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'YES'
        else:
                return('NO')

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))