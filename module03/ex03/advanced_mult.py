#!/usr/bin/env python3

def main():
    # Looping through the base numbers 0 to 10
    for i in range(11):
        # Generating the row of multiplied values as a single string
        row_values = " ".join(str(i * j) for j in range(11))
        
        # Displaying the formatted output
        print(f"Table of {i}: {row_values}")

if __name__ == "__main__":
    main()
    