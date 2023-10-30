#Write a python program to find the longest words.

file=open("file.txt","r")
x=(file.read())
print(x)
longest=max(x.split(), key=len)
print(longest)
print(len(longest))

file=open("data.txt","r")
x=(file.read())
print(x)
longest=max(x.split(), key=len)
print(longest)
print(len(longest))