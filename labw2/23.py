thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)
thislist1.sort(reverse = True)
print(thislist1)


def myfunc(n):
  return abs(n - 50)
thislist2 = [100, 50, 65, 82, 23]
thislist2.sort(key = myfunc)
print(thislist2)

thislist3 = ["banana", "Orange", "Kiwi", "cherry"]
thislist3.sort(key = str.lower)
print(thislist3)

thislist4 = ["banana", "Orange", "Kiwi", "cherry"]
thislist4.reverse()
print(thislist4)