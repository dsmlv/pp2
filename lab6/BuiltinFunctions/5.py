def all_true(t):
    return all(t)

t1 = (True, True, True)
t2 = (True, False, True)

print(all_true(t1))  
print(all_true(t2))