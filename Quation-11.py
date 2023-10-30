#Write a Python program to write a list to a file. 

list=["Bhavnik","Mandali","python","php"]
file=open("data.txt","w")
for i in list:
    file.write(i+"\n")
file.close()


file=open("data.txt","r")
print(file.read())
file.close()

