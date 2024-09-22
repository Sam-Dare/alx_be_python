# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using a while loop
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    # Print a newline character after each row
    print()
    # Increment the row counter
    row += 1
