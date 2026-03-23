#!/usr/bin/env python3

def main():
    try:
        # Accepting user input with a newline character to match your format
        base_number = int(input("Enter a number\n"))
        
        # Looping from 0 up to 9
        for i in range(12):
            result = i * base_number
            print(f"{i} x {base_number} = {result}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()