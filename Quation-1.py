#What is File function in python? What is keywords to create and write file.

file=open("data.txt","w")
file.write("Bhavnik mandali")
file.close()

file=open("data.txt","r")
print(file.read())
file.close()