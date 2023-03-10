string = "Hello, World!"

upper_count = 0
lower_count = 0

for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(f"# of Uppercase letters: {upper_count}")
print(f"# of Lowercase letters: {lower_count}")