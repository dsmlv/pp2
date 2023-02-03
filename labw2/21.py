thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist1 = ["apple", "banana", "cherry"]
for i in range(len(thislist1)):
  print(thislist1[i])


thislist2 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist2):
  print(thislist2[i])
  i = i + 1


thislist3 = ["apple", "banana", "cherry"]
[print(x) for x in thislist3]