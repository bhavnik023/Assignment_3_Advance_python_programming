#Write a Python program to read first n lines of a file

file=open("File.txt","r")
print("Print the first line")
print(file.readline())
file.close()


def first_n_line(filename,n):
    file=open(filename,"r")
    for i in range(n):
        line=file.readline()
        print(line)

first_n_line("file.txt",1)