#!/usr/bin/env python3

def main():
    try:
        # Prompting the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calculating the product
        result = num1 * num2
        
        # Determining the sign of the result
        if result > 0:
            print("The result is positive.")
        elif result < 0:
            print("The result is negative.")
        else:
            print("The result is zero.")
            
        # Displaying the final calculation
        print(f"The result of the multiplication is: {result}")
        
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    main()