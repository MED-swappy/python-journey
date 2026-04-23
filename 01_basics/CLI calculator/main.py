a = int(input("Enter the first number: "))
op = input("Enter the operation: ")
b = int(input("Enter the second number: "))
if (b != 0):
 match op:
    case "+":
        print(f"{a} + {b} = {a+b}")
    case "-":
        print(f"{a} - {b} = {a-b}")
    case "/":
        print(f"{a} / {b} = {a/b}")
    case "*" | "x":
        print(f"{a} x {b} = {a*b}")
    case _:
        print("Invalid operator!")
else:
   print("Division by zero!")