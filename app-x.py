# This is the modified source file for feature-x branch
def feature_x():
    print("This is feature-x branch")
    print("This is a new feature added in feature-x branch")
    print("Feature X: This is a simple calculator program")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")

if __name__ == "__main__":
    feature_x()
