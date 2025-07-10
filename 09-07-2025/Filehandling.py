#File Handling

# f = open("file.txt","w+")
# print("readlines",f.readlines())
# f.write("hello likhitha\n")
# f.write("hello poojitha")
# list1 = ['how are you pojjitha\n',"i am fine likhitha,about you\n","i am good"]
# f.writelines(list1)
# print("file name is",f.name)
# print("done")
# f.close()


# f = open("file.txt","w+")
# print("readline",f.readline())
# f.write("hello likhitha\n")
# f.write("hello poojitha")
# list1 = ['how are you pojjitha\n',"i am fine likhitha,about you\n","i am good"]
# f.writelines(list1)
# print("file name is",f.name)
# print("done")
# f.close()


# f = open("file.txt","w+")
# print("read(n)",f.read())
# f.write("hello likhitha\n")
# f.write("hello poojitha")
# list1 = ['how are you pojjitha\n',"i am fine likhitha,about you\n","i am good"]
# f.writelines(list1)
# print("file name is",f.name)
# print("done")
# f.close()

# f = open("file.txt","r+")
# print("read(n)",f.read(10))
# f.write("hello likhitha\n")
# f.write("hello poojitha")
# list1 = ['how are you pojjitha\n' , "i am fine likhitha,about you\n" , "i am good"]
# f.writelines(list1)
# print("file name is",f.name)
# print("done")
# f.close()


# with open as we dont need to close the file and creates new file

# with open("file1.txt" , "w+") as f:
    # list1 = ['how are you pojjitha\n',"i am fine likhitha,about you\n","i am good"]
    # f.writelines(list1)

# with open("file1.txt" , "r") as f:
#     print(f.read(10))
#     print(f.tell())
#     print(f.seek(2))
#     print(f.read(10))

# with open("file1.txt",'a') as f:
#     f.write("this is appended")
    

#Exceptional handling

# a = 10
# b = 0
# try:
#     result = a / b
# except:
#     print(f"{a}/{b} is error")

# a = 10
# b = 0
# try:
#     result = a / b
#     print(result)
# except Exception as e:
#     print(f"{a}/{b} is {e}")

# try:
#   print(x)
# except Exception as e:
#   print(e)
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("file4.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong while writing") #given read mode
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")  #no file

# Modules

# import math
# print(dir(math))
# print(math.sqrt(25))
# print(math.pow(2,4))

# from random import *
# print(random()) #lessthan 1
# print(randint(1,5)) #5 included
# print(randrange(1,3)) #3 not included
# print(uniform(1,5)) #inrange
# l = ["python" , "AI" , "Java" , "JS"]
# print(choice(l))

# import module
# print(module.pid)
# print(module.add(1,2))
# print(module.sub(2,1))

# from module import *
# print(pid)
# print(add(1,2))
# print(sub(2,1))

# from module import pid as id , add as a , sub as s
# print(id)
# print(a(1,2))
# print(s(2,1))

# import module
# import module
# import module
# import module
# from importlib import *
# reload(module)
# reload(module)


# CLI (Command Line Interface): navigation, scripting 

# import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C:/Users/USER/Desktop")
# print(os.getcwd())
# print(os.listdir())

# import os
# os.mkdir("created.txt")
# os.makedirs("one/one1")

# import os
# os.rmdir("created.txt")
# os.removedirs("one/one1")

# import os
# os.mkdir("created")
# os.rename("created","done")
# os.rmdir("done")

# import os
# os.makedirs("one/one1")
# os.renames("one/one1","two/two2")
# os.removedirs("two/two2")

# import os
# for dirpath , dirnames , filenames in os.walk("C:/Users/USER/Desktop/Hexa/09-07-2025"):
#     print("current directroy path",dirpath)
#     print("dir name", dirnames)
#     print("filenames",filenames)

# import os
# print(os.environ.get("Hexa"))
# print(os.path.exists("C:/Users/USER/Desktop/Hexa/09-07-2025"))
# print(os.path.exists("C:/Users/USER/Desktop/Hexa/kjnjksd"))
# print(os.path.isfile("C:/Users/USER/Desktop/Hexa/09-07-2025"))
# print(os.path.isdir("C:/Users/USER/Desktop"))
# print(os.path.splitext("/Users/USER/Desktop/Hexa/09-07-2025.txt"))











