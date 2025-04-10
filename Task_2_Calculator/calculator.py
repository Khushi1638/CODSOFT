
def main():
    # To check if the value is valid or not; if not, ask again
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Please enter a valid number...")

    # Prompting operation
    while True:
        operation = input("Enter the operation (+, -, *, /, %): ")
        match operation:
            case "+":
                answer = add(num1, num2)
            case "-":
                answer = subtract(num1, num2)
            case "*":
                answer = multiply(num1, num2)
            case "/":
                answer = divide(num1, num2)
            case "%":
                answer = remainder(num1, num2)
            case _:
                print(f"'{operation}' is not a valid mathematical operation.")
                continue  # go back to ask again
        break  # valid operation was performed

    print(f"{num1} {operation} {num2} = {answer}")


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

def remainder(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."


if __name__ == "__main__":
    main()
