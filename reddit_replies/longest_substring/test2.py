"""
Code investigating:

https://old.reddit.com/r/learnpython/comments/8jtoxy/longest_alphabetical_substring_struggling_really/

This is O(N).
"""

def longest_sequence(s):
    """Finds the longest alphabetical sequence in a string.
    
    s  the string to find search in
    
    Returns the longest sequence found.
    """

    best_start = None
    best_length = 0

    last_ch = None

    maybe_start = 0
    maybe_length = 1

    for (i, ch) in enumerate(s):
        if last_ch and ch >= last_ch:
            maybe_length += 1
        else:
            if maybe_length > best_length:
                best_start = maybe_start
                best_length = maybe_length
            maybe_start = i
            maybe_length = 1
        last_ch = ch

    if maybe_length > best_length:
        best_start = maybe_start
        best_length = maybe_length

    return s[best_start:best_start+best_length]
