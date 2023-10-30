#Write a Python program to count the number of lines in a text file.

with open("data.txt","r") as dt:
    lines=len(dt.readlines())
    print("Total number of lines :",lines)



file=open("data.txt","r")

x=file.readlines()
print("print of number of lines")
print(len(x))