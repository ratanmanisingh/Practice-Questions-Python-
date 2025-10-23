# A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward

w = input("Enter anything:- ")
if w == w[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
    