fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


thistuple1 = ("apple", "banana", "cherry")
for x in thistuple1:
  print(x)


thistuple2 = ("apple", "banana", "cherry")
for i in range(len(thistuple2)):
  print(thistuple2[i])


thistuple3 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple3):
  print(thistuple3[i])
  i = i + 1