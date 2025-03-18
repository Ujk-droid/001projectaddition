import __main__

def main():
    print("This program adds two numbers.")

    num1 = input("Enter first number: ")
    num1 = int(num1)  # Convert the input to an integer
    num2 = input("Enter second number: ")
    num2 = int(num2)  # Convert the input to an integer

    Total = num1 + num2
    print("The total is " + str(Total) + ".")

# Ensure this block is only executed if the script is run directly
if __name__ == '__main__':
    main()
