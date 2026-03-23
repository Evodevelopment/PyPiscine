#!/usr/bin/env python3

def main():
    try:
        # Accepting user input and casting to an integer
        user_input = int(input("Enter a number: "))
        
        if user_input > 25:
            # print() naturally appends a newline character in Python
            print("Error") 
        else:
            # Looping from the entered number up to and including 25
            for i in range(user_input, 26):
                print(f"Inside the loop, my variable is {i}")
                
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()