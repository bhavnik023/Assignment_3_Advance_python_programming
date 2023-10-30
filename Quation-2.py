#Write a Python program to read an entire text file.

file=open("File.txt","w")
file.write("This is an article on reading text files in Python.")
file.close()

file=open("File.txt","r")
p=file.read()
print(p)
file.close()

