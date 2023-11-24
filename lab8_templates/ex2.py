"""Template for exercise 2 of lab 8: Neighbor average"""


def print_table(table):
    for row in table:
        for element in row:
            print(element, end=" ")
        print()
    print()


def neighbor_average(table, rowIdx, columnIdx):
    '''
    In this function, we compute the average of the neighbors.

    For example, if we receive as indexes rowIdx=2 and columnIdx=3 the neighbors are:

        0   1   2   3   4   5
    0   -   -   -   -   -   -
    1   -   -   *   *   *   -
    2   -   -   *   X   *   -
    3   -   -   *   *   *   -
    4   -   -   -   -   -   -

    The indexes of the neighbors are:
              1,2  1,3  1,4
              2,2       2,4
              3,2  3,3  3,4

    '''

    # We will use this variables to keep track of the total and the count
    total = 0
    count = 0

    # 1 - Get the indices of the neighbors
    # 2 - Check if each index is valid (for example a negative index is not valid)
    # 3 - If the index is valid,
    #     - get the corresponding element from the table and add it to total
    #     - increment the count

    # 4 - Get the average by dividing the total by the count
    avg = total / count
    return avg


def create_zero_table(rows, columns):
    zero_table = []

    for _ in range(rows):
        zero_table.append([0] * columns)

    return zero_table


def main():

    # A test case table

    table = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 6],
             [4, 5, 6, 7]]

    print_table(table)

    # create a new table of the same size, filled with zeros, to make things easier
    n_table = create_zero_table(len(table), len(table[0]))

    print_table(n_table)

    # iterate over the table and compute the average of the neighbors for each element
    for rowIdx in range(len(table)):
        for colIdx in range(len(table[rowIdx])):
            n_table[rowIdx][colIdx] = neighbor_average(table, rowIdx, colIdx)

    print_table(n_table)


# Execution starts here
if __name__ == '__main__':
    main()
