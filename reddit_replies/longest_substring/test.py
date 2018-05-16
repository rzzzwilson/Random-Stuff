"""
Code inverstigating:

https://old.reddit.com/r/learnpython/comments/8jtoxy/longest_alphabetical_substring_struggling_really/

This should be O(N).
"""

def longest_sequence(s):
    """Returns the longest alphabetical sequence in 's'."""

    black = 0
    result_start = 0
    result_length = 0

    for (white, (white_char, white_right)) in enumerate(zip(s[:-1], s[1:])):
        if white_char > white_right:
            # sequence ends here
            new_start = black
            new_len = white - black + 1
            black = white + 1
            if new_len > result_length:
                # new result, update
                result_start = new_start
                result_length = new_len

    # haven't checked last subsequence, must check if longer
    new_start = black
    new_len = len(s[black:])
    if new_len > result_length:
        # new result, update
        result_start = new_start
        result_length = new_len

    return s[result_start:result_start+result_length]
