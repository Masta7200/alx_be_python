num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        print(f"The result is: {num1 + num2}")
    case "-":
        print(f"The result is: {num1 - num2}")
    case "*":
        print(f"The result is: {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operation. Please choose +, -, *, or /.")