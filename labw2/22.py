fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits1 if "a" in x]
newlist2 = [x for x in fruits if x != "apple"]
newlist3 = [x for x in fruits]
print(newlist1)
print(newlist2)
print(newlist3)


newlist4 = [x for x in range(10)]
print(newlist4)


newlist5 = [x for x in range(10) if x < 5]
print(newlist5)


fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist6 = [x.upper() for x in fruits2]
newlist7 = ['hello' for x in fruits2]
newlist8 = [x if x != "banana" else "orange" for x in fruits2]
print(newlist6)
print(newlist7)
print(newlist8)



