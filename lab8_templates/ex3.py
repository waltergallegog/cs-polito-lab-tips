"""Template for exercise 3 of lab 8: Magic square"""


def print_table(table):
    for row in table:
        for element in row:
            print(element, end=" ")
        print()
    print()


def read_table(n):
    '''
    Read a table of size n x n from the keyboard
    '''
    table = []
    for i in range(n):

        # Create a new row
        for j in range(n):
            # Read an element from input and add it to the row
            element = int(input(f"Enter element {i},{j}: "))

        # When the row is ready, add it to the table

    return table


def check_if_magic(table):
    '''
    Check if the table is a magic square by checking the numbers, rows, columns, and diagonals
    '''

    # Just a reference to compare all the rest
    target_sum = 0  # You need to replace this. What is the target sum for a magic square?

    is_magic = (
        check_all_numbers(table) and
        check_rows(table, target_sum) and
        check_columns(table, target_sum) and
        check_diagonals(table, target_sum))

    return is_magic


def check_all_numbers(table):
    '''
    Check if the table contains all the numbers from 1 to n x n
    '''
    check = False

    print("All numbers present:", check)
    return check


def check_rows(table, target):
    '''
    Check if all the rows sum to the target value
    '''
    check = False

    print("All rows sum to target:", check)
    return check


def check_columns(table, target):
    '''
    Check if all the columns sum to the target value
    '''
    check = False

    print("All columns sum to target:", check)
    return check


def check_diagonals(table, target):
    '''
    Check if both diagonals sum to the target value
    '''
    check = False

    print("Both diagonals sum to target:", check)
    return check


def main():
    n = 4
    table = read_table(n)
    print_table(table)

    if check_if_magic(table):
        print("It's magic!")
    else:
        print("It's not magic!")


# Execution starts here
if __name__ == '__main__':
    main()
