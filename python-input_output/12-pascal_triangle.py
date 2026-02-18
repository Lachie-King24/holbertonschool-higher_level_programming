#!/usr/bin/python3
"""Function that returns a list of int"""


def pascal_triangle(n):
    """Pascal triangle"""
    # create an empty list
    triangle_list = []

    # if n is less or equal to zero
    if n <= 0:
        # print empty list
        return triangle_list
    else:
        # create a loop for row increments
        for i in range(n):
            # row will always start with 1
            row = [1]

            # if i is higher than 0
            if i > 0:
                # last row is i (current row) - 1
                prev_row = triangle_list[i - 1]

                # set j loop for index in row
                for j in range(1, i):
                    # append the calculation to the row
                    row.append(prev_row[j - 1] + prev_row[j])

                # add the final 1
                row.append(1)

            # append the completed row to the triangle list
            triangle_list.append(row)

        # print the list
        return triangle_list
