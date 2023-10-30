#Write a Python program to copy the contents of a file to another file.

file=open("file.txt","r")
a=file.read()
print(a)
file.close()

file=open("data.txt","w")
file.write(a)
print("File content is copy successfuly")
file.close()