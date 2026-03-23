#!/usr/bin/env python3

def main():
    # The required password variable
    password = "Python is awesome"
    
    # Prompting the user for input
    user_input = input("Enter a password: ")
    
    # Checking the input against the stored password
    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()