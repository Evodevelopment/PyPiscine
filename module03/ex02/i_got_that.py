#!/usr/bin/env python3

def main():
    # The initial prompt outside the loop
    user_input = input("What you gotta say? : ")
    
    # The loop continues as long as the input is strictly NOT "STOP"
    while user_input != "STOP":
        user_input = input("I got that! Anything else? : ")

if __name__ == "__main__":
    main()