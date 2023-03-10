import os
print("Test a path exists or not:")
path = r'C:\Users\ddosm\Desktop\vremenno\vremenno.docx'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))