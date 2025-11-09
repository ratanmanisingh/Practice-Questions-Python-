n = int(input("Enter your number:- "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# check which is odd and which is even 

x = int(input("Enter your number:"))
y = int(input("Enter your number:"))
if x % 2 == 0 and y % 2 == 0:
    print("Both numbers are Even")
if x % 2 == 0 and y % 2 != 0:
    print("x is even and y is odd")
if x % 2 != 0 and y % 2 != 0:
    print("Both numbers are Odd")
if x % 2 != 0 and y % 2 == 0:
    print("x is odd and y is even")

# By recursion