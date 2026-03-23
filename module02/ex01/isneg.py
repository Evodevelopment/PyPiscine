#!/usr/bin/env python3

def main():
    user_input = input("Enter a number: ")
    
    try:
        # Using float to handle both integers and decimal numbers
        number = float(user_input)
        
        if number < 0:
            print("This number is negative.")
        elif number > 0:
            print("This number is positive.")
        else:
            print("This number is both positive and negative.")
            
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")

if __name__ == "__main__":
    main()