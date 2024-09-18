# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print()  # Move to the next line after completing a row
    row += 1