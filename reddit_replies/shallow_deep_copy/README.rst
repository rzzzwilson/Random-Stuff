Aliasing, Shallow and Deep Copy, and all that
=============================================

Shallow and deep copy seem to be confusing to some.  Here we will
discuss different copy methods and compare them to assignment.

Assignment
----------

We're comfortable with assignment::

    x = [1, [2, 3]]
    print(f'x={x}')
    >>>x=[1, [2, 3]]

where the line(s) prefixed with `>>>` are the output from the preceding
line(s).

So far, so familiar.  But do we *really* understand exactly what python
assignment does?  It looks like `x` is set to a list `[1, [2, 3]]`, right?

No, not in python!  Let's draw a picture::

    x = [1, [2, 3]]

        <x> ----> «[1, [2, 3]]»

where the `<>` delimit the name of a variable, and the `«»` delimit an object.
The `---->` means 'references'.  So we say that the variable `x` references the
object `[1, [2, 3]]`.

Aliasing
--------

Let's look at a slightly more complicated example::

    x = [1, [2, 3]]
    y = x
    print(f'x={x}')
    print(f'y={y}')
    >>>x=[1, [2, 3]]
    >>>y=[1, [2, 3]]

It *looks* like `y` gets the same value as `y`, doesn't it?  But that's not what
actually happens.  Remember that we said a variable references an object?  The
statement `y = x` actually evaluates `x` and gets the reference that `x` contains
and puts it into `y`.  Here's a picture::

    x = [1, [2, 3]]

        <x> ---> «[1, [2, 3]]»

After the line `x = [1, [2, 3]]` the variable `x` refers (or points) to the
object [1, [2, 3]]. ::

    y = x

        <x> ---> «[1, [2, 3]]»
                 ^
                 |
                /
               /
            <y>

After the line `y = x` the variable `y` contains the **same reference**
that `x` contains, so `y` contains a reference to the same object
that `x` refers to: [1, [2, 3]].  So when we print `x` and `y` we see the
same result.  We call this 'aliasing'.  The `y` variable aliases the `x`
variable.

We can show that `x` and `y` refer to the same object by using the `id()`
builtin function::

    id(object)

    Returns the "identity" of an object. This is an integer which is guaranteed
    to be unique and constant for this object during its lifetime. Two objects
    with non-overlapping lifetimes may have the same id() value.

The documentation goes on to say that in cpython the `id()` function returns the
address in memory of an object.  Let's change our example code a little bit:

    x = [1, [2, 3]]
    y = x
    print(f'x={x}, id(x)={id(x)}')
    print(f'y={y}, id(y)={id(y)}')
    >>>x=[1, [2, 3]], id(x)=4321738952
    >>>y=[1, [2, 3]], id(y)=4321738952

Note that the integer values returned by the `id()` function are the same. 
**That means that the `x` and `y` variables point to the same object!.**

Let's try something slightly different::

    x = [1, [2, 3]]
    y = [1, [2, 3]]
    print(f'x={x}, id(x)={id(x)}')
    print(f'y={y}, id(y)={id(y)}')
    >>>x=[1, [2, 3]], id(x)=4339564744
    >>>y=[1, [2, 3]], id(y)=4339539848

Here we assign `x` and `y` to the same list expression.  The two variables now
point to *different* objects, though the objects have the same value.  A 
picture::

    x = [1, [2, 3]]

        <x> ---> «[1, [2, 3]]»
    
    y = x

        <x> ---> «[1, [2, 3]]»
        <y> ---> «[1, [2, 3]]»      # note, different object!

In this case `y` doesn't alias `x`.

Shallow Copy
------------

Let's try using the *copy* module::

    import copy
    x = [1, [2, 3]]
    y = copy.copy(x)      # copy x to y
    print(f'x={x}, id(x)={id(x)}')
    print(f'y={y}, id(y)={id(y)}')
    >>>x=[1, [2, 3]], id(x)=4322873224
    >>>y=[1, [2, 3]], id(y)=4322899720

Looks good, right?  We have different objects referenced by `x` and `y`.
But let's look inside those objects using `id()`::

    import copy
    x = [1, [2, 3]]
    y = copy.copy(x)
    print(f'x={x}, id(x)={id(x)}')
    print(f'y={y}, id(y)={id(y)}')
    print(f'x[0]={x[0]}, id(x[0])={id(x[0])}')
    print(f'y[0]={y[0]}, id(y[0])={id(y[0])}')
    >>>x=[1, [2, 3]], id(x)=4331261832
    >>>y=[1, [2, 3]], id(y)=4331288328
    >>>x[0]=1, id(x[0])=4297636896
    >>>y[0]=1, id(y[0])=4297636896

This shows something unexpected: `x` and `y` refer to different objects
**but** `x[0]` and `y[0]` refer to the same object!  Here's a (slightly
inaccurate) picture showing the state after the code has run::

    <x> ---> «[<>, [<>, <>]]»
                |    |   |
                |    |   |
                v    v   v
               «1»  «2» «3»
                ^    ^   ^
                |    |   |
                |    |   |
    <y> ---> «[<>, [<>, <>]]»

The `<>` symbol means an unnamed reference.

This *shallow copy* is defined in the *copy.copy()* documentation::

    A shallow copy constructs a new compound object and then
    (to the extent possible) inserts references into it to the
    objects found in the original.

Deep Copy
---------

Suppose we didn't want this, but wanted two completely separate objects?
We use a *deep copy* to achieve this::


