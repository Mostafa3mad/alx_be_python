num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

def cal(num1, num2, operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return "error"
            else:
                return num1 / num2


out=cal(num1,num2,operation)
if out=="error":
    print("Cannot divide by zero.")
else:
    print(f"The result is {out}.")