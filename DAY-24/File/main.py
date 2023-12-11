# file = open("/home/jibril/Documents/Python/DAY-24/File/myfile.txt")
# with open("/home/jibril/Documents/Python/DAY-24/File/myfile.txt") as file:
#     contents = file.read()
#     print(contents)
# file.close()if we open with the "with" keyword we woludnot worry close the file
# mode="w" to write only by default mode is read mode="a" to append
with open("/home/jibril/Documents/Python/DAY-24/File/myfile.txt", mode="a") as file:
    file.write("\nHello jimma")
