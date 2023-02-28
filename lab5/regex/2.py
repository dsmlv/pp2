import re
def text_match(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'YES'
        else:
                return('NO')
print(text_match("ab"))
print(text_match("aabbbbbc"))