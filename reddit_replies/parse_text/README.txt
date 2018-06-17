Reply for:

https://old.reddit.com/r/Python/comments/8qqbwk/parsing_input_file_in_python/


The first problem boils down to converting a string (the first line of the
file) to something like a list of tuples.  Once you have that you can store
it.  So you want something like this:

    in_str = '(A1,19),(A2,4),(A3,2),(A4,1)'
    # some code producing "out_str" = [('A1',19),('A2',4),('A3',2),('A4',1)]

How do we do that?  We could split on the ',' characters, but that breaks
up the tuples.  We could handle that, but maybe it's cleaner f we replace
the `),(` substring with something that we can split easily on.  Like this:

    in_str = '(A1,19),(A2,4),(A3,2),(A4,1)'
    tmp = in_str.replace('),(', '|')
    tmp = tmp[1:-1].split('|')
    out_str = []
    for t in tmp:
        (a, b) = t.split(',')
        out_str.append((a, int(b)))
    # "out_str" = [('A1',19),('A2',4),('A3',2),('A4',1)]

Reading the following lines is done in much the same way, but simpler
because we don't have tuples and only have integers.
