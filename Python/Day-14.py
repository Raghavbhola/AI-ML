#-----------------------[ N0v. 18, 2026 ]--------------------------------------


file = 'data/iris.csv'
# mode = "r"
# try:
#     with open(file,mode) as f:
#         print(f.read())
#         #f.close()
# except OSError as error:
#      print("Found error:-", error)


#file handling and related operations
#we will took the information from internet - extract, write snake game code - single user, multiuser, AI agent
#data - in form content -> file content -> ppts, pdf, word, tabular, code -> sequen.

#data/iris.csv
# file = 'demo6.csv'
# mode = "w+"
# try:
#     with open(file,mode) as f:
#         f.write("Writing in demo file!!\n")
#         #All our file operations must be covered under this body
#         f.close()
#     print("Creating file done")
#     #print(f.readlines())
# except OSError as error:
#     print("Found error:-", error)
#file = 'data/iris.csv'
# file_new = 'demo5.csv'
# mode = "r"
# try:
#     with open(file_new,mode) as f:
#         print(f.read())
#         f.close()
# except OSError as error:
#      print("Found error:-", error)

# Filee = "demo6.csv"
# mode = 'a'
# try:
#     with open(Filee, mode) as F:
#         F.write("This line is appended")
#     print("Operation done")
# except OSError as Error:
#     print("Error found:-", Error)

#clubbing of operations or read_lines of a file
# filename = "Emp.txt"
# try:
#     with open(filename, 'w') as file:
#         file.write("Asha\nDeepak\nRaju\nChota Bheem\n")
#     with open(filename, 'r') as file1:
#         for line in file1:
#             print(line.strip())
# except OSError as Error:
#     print("Error found:-", Error)
#fileN = 'course.txt'
#course_li = ['Python\n', 'SQL\n', 'Java\n', 'OS\n']
# try:
#     with open(fileN, 'w') as file:
#         file.writelines(course_li)
#     print("Operation done")
# except OSError as Error:
#     print("Error found:-", Error)


#file_ne = 'course.txt'
# mode = "r"
# try:
#     with open(fileN,mode) as f:
#         print(f.readlines())
#         f.close()
# except OSError as error:
#      print("Found error:-", error)
# source_textFile = 'source.txt'
# dest_textFile = 'dest.txt'
# try:
#     with open(source_textFile, 'w') as file:
#         file.writelines(course_li)
#     with open(source_textFile, 'r') as source:
#         content = source.read()
#     with open(dest_textFile, 'w') as target:
#         target.writelines(content)
#     print("Content pasted successfully")
# except OSError as error:
#      print("Found error:-", error)
