# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the square pattern using nested loops
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
