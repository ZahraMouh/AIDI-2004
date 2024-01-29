# Very Simple Math Program

def add_numbers(a, b):
    return a + b

def main():
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform addition
    result = add_numbers(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
