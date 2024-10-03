#!/usr/bin/python3
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle as an empty list
    triangle = []

    # Generate each row of Pascal's triangle
    for i in range(n):
        # Create a row filled with 1s (length of row is i + 1)
        row = [1] * (i + 1)

        # Calculate the values for the current row (except for the first and last elements)
        for j in range(1, i):
            # Each value is the sum of the two values above it from the previous row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the constructed row to the triangle
        triangle.append(row)

    # Return the completed triangle
    return triangle
