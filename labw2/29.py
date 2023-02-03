thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))
thisset.add("orange")
print(thisset)


thisset1 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset1)


thisset2 = {"apple", "banana", "cherry"}
for x in thisset2:
  print(x)
print("banana" in thisset2)


thisset3 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset3.update(tropical)
print(thisset3)


thisset4 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset4.update(mylist)
print(thisset4)