import os

name = input("Please enter folder name with space: ").split()
for i in name:
    try:
       files = os.listdir(i)
    except FileNotFoundError:
        print("Please enter valid folder name")
        break
    except PermissionError:
        print("User don't have enough permissions to excute the program")
    for file in files:
        print(file)