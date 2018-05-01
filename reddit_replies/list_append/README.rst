Python is not quite like other languages you may know.  A python variable
consists of two parts: a name and a reference (pointer, if you like) to
a python object.  So this code:

    a = [0, 1, 2, 3]

first creates a python list `[0, 1, 2, 3]` and then puts the reference to that
list into a variable with name `a`.  We can make a little picture:

    +---+         +---+---+---+---+
    | a |-------> | 0 | 1 | 2 | 3 |
    +---+         +---+---+---+---+

**Now**, when you do:

    b = a

you first *evaluate* the expression on the right hand side `a`.  Evaluating
a python variable returns the refernce the variable contains.  The reference
is then put into a new variable called `b`.  Note that only a reference is
assigned to `b`.  So we now have:

    +---+         +---+---+---+---+
    | a |-------> | 0 | 1 | 2 | 3 |
    +---+         +---+---+---+---+
                    ^
    +---+           |
    | b |-----------+
    +---+

The `a` and `b` variables reference the **same** object.  So when we do

    b.append(4)

we append a new python object (the `4` integer object) to the list that `b`
is referencing:

    +---+         +---+---+---+---+---+
    | a |-------> | 0 | 1 | 2 | 3 | 4 |
    +---+         +---+---+---+---+---+
                    ^
    +---+           |
    | b |-----------+
    +---+

Note that the object `a` is referencing has the `4` appended because `a` and `b`
reference the **same object**.

If you want `b` to reference its own copy of the original list then you
have to assign a copy of `[0, 1, 2, 3]` to `b`:

    a = [0, 1, 2, 3]
    b = list(a)   # make a copy of 'a'
    b.append(4)
    print('a:', a)
    print('b:', b)
