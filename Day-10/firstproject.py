import os

folders = input("Please enter folder name with the space: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
       print("please enter a valide folder name: ")
       break
       print(" ===== files in the foler - " + folder)
    for file in files:
        print(file)
