# import os

# with open("pyfile.txt", "a") as f:
#     file = f.write("My name is")
#     print(file)
# f.close()

# with open("filename.txt", "w") as f:
#     f.write("This is basant, \nI am from Odissa") 
#     f.write("I am learning python")
# with open("filename.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("python", "JAVA")
# print(new_data)

# with open("filename.txt", "w") as f:
#     f.write(new_data)
def file_op_sc():
    word = "gLearning"
    with open("filename.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("word Found")
        else:
            print("word not found")
file_op_sc()