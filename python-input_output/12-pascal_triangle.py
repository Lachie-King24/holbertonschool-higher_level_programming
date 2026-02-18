#!/usr/bin/python3
"""Function that returns a list of int"""


def pascal_triangle(n):
    triangle_list = []
    if n <= 0:
        return triangle_list
    else:
        for i in range(n):
            row = [1]

            if i > 0:
                prev_row = triangle_list[i - 1]

                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])

                row.append(1)

            triangle_list.append(row)

        return triangle_list
