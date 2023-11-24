"""Template for exercise 1 of lab 8: Merge lists"""


def merge(l1, l2):
    '''
    This function will merge two lists into one, alternating elements from each list.
    For example if
    l1 = [1, 2, 3]
    l2 = ['A', 'B', 'C', 'D']
    it will output:
    [1, 'A', 2, 'B', 3, 'C', 'D']
    '''
    merged = []

    # Iterate over BOTH lists at the same time
    #   Add element 0 from list1
    #   Add element 0 from list2

    #   Add element 1 from list1
    #   Add element 1 from list2
    #   ...

    # Add elements from the longest list

    return merged


def main():

    # Some test cases

    # list1 and list2 same length
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c', 'd']
    print(merge(list1, list2))

    # list2 longer than list1
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c', 'd', 'e', 'f']

    print(merge(list1, list2))

    # list1 longer than list2
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = ['a', 'b', 'c']
    print(merge(list1, list2))


# Execution starts here
if __name__ == '__main__':
    main()
