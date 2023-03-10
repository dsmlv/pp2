with open("copy.txt",'r') as copy:
    with open("paste.txt",'w') as paste:
        for line in copy:
            paste.write(line)