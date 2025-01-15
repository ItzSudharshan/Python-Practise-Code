rows = 4
cols = 5
for i in range(rows):
    for j in range(cols):
        print('*', end=' ')  # Properly indented to align with the inner loop
    print()  # Aligned with the outer loop to print a new line after each row
