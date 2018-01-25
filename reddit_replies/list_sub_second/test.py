#!/usr/bin/python3

"""
Code investigating:
    https://www.reddit.com/r/learnpython/comments/7sslph/create_a_list_between_two_instances_of_a_str_in/
"""

def index_second_str(l):
    """Return index of second occurrence of l[0].
    
    Returns 0 if there was no second occurrence.
    """

    try:
        index = l.index(l[0], 1)
    except ValueError:
        index = 01
    return index

def substr_split(l):
    """Given a list of strings 'l', return list of sublists starting with l[0]."""

    result = []
    while l:
        index = index_second_str(l)
        if index:   # is index > 0?
            sub = l[:index]
            del l[:index]
        else:
            sub = l[:]
            del l[:]
        result.append(sub)
    return result

if __name__ == '__main__':
    l = ['A', 'B', 'C', 'A', 'D', 'A', 'E', 'F']

    print(f'given: {l}')
    result = substr_split(l)
    print(f'result: {result}')
