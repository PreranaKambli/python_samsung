def print_x_in_hollow_square(n):
    # Check if n is at least 3 to form a valid hollow square with an X
    if n < 3:
        print("Size of the square must be 3 or greater")
        return

    # Loop through rows
    for i in range(n):
        for j in range(n):
            # Print the X pattern
            if i == j or j == (n - i - 1):
                print('*', end=' ')
            else:
                # Leave the inside hollow
                print(' ', end=' ')
        print()  # Move to the next line after each row

# Input size for the square
n = int(input("Enter the size of the square (at least 3): "))
print_x_in_hollow_square(n)
