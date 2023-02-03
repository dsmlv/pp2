list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


listA = ["a", "b" , "c"]
listB = [1, 2, 3]
for x in listB:
  listA.append(x)
print(listA)


list11 = ["a", "b" , "c"]
list22 = [1, 2, 3]

list11.extend(list22)
print(list11)