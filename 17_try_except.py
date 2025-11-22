try:
    t = int(input())
    for _ in range(t):
        try:
            a, b = map(int, input().split())
            print(a // b) 
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        except ValueError as e:
            print(f"Error Code: {e}")
except ValueError:
    print("Error Code: invalid literal for int() with base 10: '[input_value]'")