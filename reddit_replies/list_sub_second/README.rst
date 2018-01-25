Code to investigate:

https://www.reddit.com/r/learnpython/comments/7sslph/create_a_list_between_two_instances_of_a_str_in/

REPLY BELOW --------------------------------------

We want to find the occurrence (if any) of the *second* occurrence of the first
string in the list.  Once we have found the index into the list of this second
occurrence, we can remove the front of the given list up to but not including
the second occurrence and append this sub-list into a result list.

Now look at the original list after doing the above.  It must start with the
string we are splitting on since we *didn't* remove this string above.  So we
could probably write an iterative solution that looks a bit like this in pseudo
python :

    # starting with a list 'l'
    result = []
    while not finished:
        x = index of second occurrence of l[0]
        result.append(l[:x])
        delete the [:x] bit of l

After that `result` should contain what you want.

There are two things we have to think about and solve.  We need a function that
will take a list of strings and return the index in the list of the second
occurrence of l[0].  The python [list.index()[(https://docs.python.org/3.6/tutorial/datastructures.html#more-on-lists)
method is probably what you want for this.  You will have to handle the case
when there is no second occurrence of the first string.

The other problem is how to get/append/delete the substring once you have found
it.

The pseudo code above destroys the input list 'l'.  This isn't nice.  Once you
have a destructive solution working try to change it to preserve the input list.
You would do that by keeping track within 'l' of where you got up to and
searching for second strings from that point.
