#Write a Python program to read last n lines of a file.

def last_n_line(filename,n):
    with open(filename,"r") as file:
        lines=file.readlines()
        l_n_line=lines[-n:]
        for i in l_n_line:
            print(i)

last_n_line("file.txt",-1)

