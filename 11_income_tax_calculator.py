income = int(input("Enter your income: "))
if income <= 400000:
    tax = 0
    print("No tax")
elif 400000 < income <= 800000:
    tax = income * 0.05
    print(f"Your tax is {tax}")
elif 800000 < income <= 1200000:
    tax = income * 0.1
    print(f"Your tax is {tax}")
elif 1200000 < income <= 1600000:
    tax = income * 0.15
    print(f"Your tax is {tax}")
elif 1600000 < income <= 2000000:
    tax = income * 0.2
    print(f"Your tax is {tax}")
elif 2000000 < income <= 24000000:
    tax = income * 0.25
    print(f"Your tax is {tax}")
elif income > 24000000:
    tax = income * 0.3
    print(f"Your income is {tax}")