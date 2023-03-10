import os
p=r"C:\Users\ddosm\Desktop\Мои документы\my docs"
dir_list=os.listdir(p)
print("Only directories: ")
print([n for n in dir_list if os.path.isdir(os.path.join(p, n))])
print("\nOnly files: ")
print([n for n in dir_list if os.path.isfile(os.path.join(p, n))])
print("\nFiles and directories are: ")
print([ n for n in dir_list])