import os

file_path = r"C:\Users\ddosm\Desktop\2course\2sem\pp2\lab6\DirAndFiles\delete.txt"

if os.access(file_path, os.F_OK):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"{file_path} deleted successfully")
    else:
        print(f"{file_path} can't be deleted, permission denied")
else:
    print(f"{file_path} doesn't exist")

# deleted successfully