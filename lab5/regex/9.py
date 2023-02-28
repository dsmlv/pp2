import re
def capital_words_spaces(text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(capital_words_spaces("Pp"))
print(capital_words_spaces("PpBest"))
print(capital_words_spaces("PpBestOfTheBest"))