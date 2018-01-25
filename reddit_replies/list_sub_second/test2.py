#!/usr/bin/python3

"""
Code investigating:
    https://www.reddit.com/r/learnpython/comments/7sslph/create_a_list_between_two_instances_of_a_str_in/

Non-destructive solution.
"""

def index_second_str(l, start):
    """Return index of second occurrence of l[start].
    
    Returns 0 if there was no second occurrence.
    """

    try:
        index = l.index(l[start], start+1)
    except ValueError:
        index = 0
    return index

def substr_split(l):
    """Given a list of strings 'l', return list of sublists starting with l[0]."""

    result = []
    start = 0
    while start < len(l):
        index = index_second_str(l, start)
        if index:   # is index > 0?
            sub = l[start:index]
            start = index
        else:
            sub = l[start:]
            index = len(l)
        result.append(sub)
        start = index
    return result

if __name__ == '__main__':
    l = ['A', 'B', 'C', 'A', 'D', 'A', 'E', 'F']

    print(f'Before, given: {l}')
    result = substr_split(l)
    print(f'After,  result: {result}')
    print(f'After,  given: {l}')
