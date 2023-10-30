# '''Write python program that user to enter only odd numbers, else will raise an exception'''

try:
     number=int(input("Enter  Your Number: "))
     if number %2==0:
          raise ValueError("This is not odd number")
     else:
          print(f"Enter your odd number:{number}")

except ValueError as e:
     print(e)