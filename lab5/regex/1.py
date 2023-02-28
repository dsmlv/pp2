import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'YES'
        else:
                return('NO')
print(text_match("acc"))
print(text_match("aba"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))