#Write a Python program to append text to a file and display the text.

file=open("File.txt","a")

x=["\nPython is a dynamic type language","\nPython is a popular programing language"]

for i in x:
    file.write(i)
file.close()

#File is read
file=open("File.txt","r")
print(file.read())
file.close()
