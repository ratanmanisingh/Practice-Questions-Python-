# Square of star

# n = int(input("Enter any Number: "))
# for _ in range(n):
    # print("* " * n)
    # print("*" * n, end =" ")


# Right angle triangle of star

# for i in range(1,n+1):
    # print("*" * i)

# Inverted Right angle triangle

# for i in range(n):
#     print("*" * (n-i))

# def inverted(n):
#     for i in range(n):
#         print("*" * (n-i))
# # inverted(4)
# def inverted1(n):
#     for i in range(n,1,-1):
#         print("*" * i)
# inverted1(7)

# Left side Right angle triangle
# def left(n):
#     for i in range(1,n+1):
#         print(" " * (n-i), end="")
#         print("*" * (i))
# left(5)

# Inverted Right side Right angle Triangle
# def right(n):
#     for i in range(n):
#         print(" " * i, end = "")
#         print("*" * (n-i))
# right(5)

# Piramid or equilateral triangle
def piramid(n):
    for i in range(1,n+1):
        print(" " * (n-i), end="")
        print("*" * (2*i-1))
piramid(5)