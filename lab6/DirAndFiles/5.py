vegetables=['Carrot','Potato','Tomato','Pepper']
f=open('items.txt','w')
for i in vegetables:
    f.write(i+"\n")
f.close()