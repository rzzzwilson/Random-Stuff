Why write this?
===============

I wrote this when replying to the umpteenth "What language should I learn first?"
post.  My posts to that sort of question were inevitably long screeds, so I
wrote this document which will get referenced in any future replies of mine.

If I had posted something different to each "which language ..." question, each
post would just have been a collection of quick half-formed thoughts.  At least
this way I will finally have a collection of **considered** half-formed
thoughts!

Programming is not about the language, it's about you
-----------------------------------------------------

When I was at university trying to learn Computer Science it was clear
that there were three types of students:

1. Those who would never be good even though they studied hard
2. The average students who learned a bit but were still average [#]_
3. Those who were going to be good despite being at university

You need to be something like type 3 if you have any hope of learning to be a
programmer **by yourself**.  How do you become type 3?  I don't know.  Certainly
curiosity is part of a good programmer.  Patience or lack of patience, at the
appropriate time, is another.  Larry Wall has a great quote along these lines [#]_.

The type 3 students were the ones who worked late hours trying things out,
trying a different approach or algorithm.  Because there were other ways that
might be better.

To learn to be a programmer by yourself you have to become what I call a
"hacker".  The modern definition of hacker is rather negative.  This
`older definition <http://www.catb.org/jargon/html/H/hacker.html>`_
describes the good programmer personality.  I would add to that definition
the attributes of curiosity and inventiveness.  You should always try for an
acceptable on-time solution, but always be thinking about better solutions,
easier long-term maintenance, more adaptable code, etc.

A computer language is just the basic tool used to tell a computer what to do.
You have to know what to do first, before you tell the computer!  And that's
**really** what being a programmer is all about.

Paradigms, database, network, GUI, ...
--------------------------------------

There's a lot more to programming than the language you use.  Being able to use
a particular language well is just the very beginning, or rather, the *end* of
the problem-solving process.  If you want to solve problems (which is what a
computer is used for) then you need to get into a myriad other things, such as
databases, GUI libraries, data structures, etc.  While I don't agree with
everything said, `this overview <http://www.wikihow.com/Become-a-Programmer>`_
might be useful.

There are different paradigms in languages, such as procedural programming,
object-oriented programming, functional programming and logic programming.
There are many other words used, many marketing driven.  You should get exposed
to them all, or at least a large subset.  This is why I like Python for
beginners: it's simple to start but you can get into some really advanced usage
when you are ready.  Ruby is probably like that, but I haven't used it enough
to be sure.

Operating system
----------------

In the beginning it really doesn't matter what operating system you use.  Later,
though, it's important that you get exposed to the three big operating systems:
Windows, OSX and Linux.  OSX and Linux are sort of the same, but Windows is very
different.  If you can, start learning on both Windows and Linux.  If you don't
want to spend money, learn on what you have now.  You really need Apple hardware
to run OSX, but you don't need to *learn* on OSX, so leave that OS until you
need that platform.

If you don't have an operating system, choose any Linux distribution.  They are
free and have all the tools you will need to get started.

Resources
---------

You will use a lot of online resources while learning and when a working
programmer.  So an internet connection is required.  Not necessarily a reliable
connection while *learning*, but when working you need a reliable connection.
`Google <https://www.google.com>`_ is your friend!
Or `DuckDuckGo <https://duckduckgo.com/>`_, etc.

The user community associated with a language is very important.  It must be
welcoming, helpful and large enough.  Some languages (no names ...) have
communities with the reputation of being extremely pedantic and dismissive
of beginners, even hostile.  This doesn't help you; avoid these communities.

When you get some experience try to help others in your language or framework
of choice.  You don't really know something until you've tried to teach someone
else, and that's when your own learning accelerates!

GitHub
------

While I'm not a great fan of `GitHub <https://github.com/>`_,
you should create an account and develop any code you write in it.  For better
or worse it's a good place to show your portfolio of code.  People can look at
the quality and how often you update.  I know some recruiters use GitHub as a
place to find people with appropriate skills.  Plus it's a good way to backup
your code and get experience using a distributed version control system and an
issues tracker.  There are other, similar, repositories, but GitHub is the
`800 pound gorilla <https://en.wikipedia.org/wiki/800-pound_gorilla>`_
at the moment.  Other repositories can be as good as or even better than
GitHub [#]_ but may have less visibility.

Broadening experience
---------------------

When you know one language reasonably well you should try another, different,
language.  Even the best language constrains the way you think about and solve a
problem, so exposing yourself to a very different language helps to broaden your
view.  Languages like C, Python, Java, Forth or even an assembly language are
useful in this respect.  I would even go so far as to recommend installing
`Scheme <https://www.gnu.org/software/mit-scheme/>`_ and plowing through the
first few chapters of `SICP <https://mitpress.mit.edu/sicp/>`_.  The
`videos <http://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/>`_
are also good value.  You will be exposed to a very different approach to
problem solving.

A broad view of computer solutions is helpful as you really shouldn't be
thinking about the language you will eventually use while designing your
solution.  Rather, you should be thinking about algorithms and data structures
in the most abstract way.  When you come to put your solution into a computer
language you may have to change your approach in minor details.  Any major
hiccups in the actual implementation may mean you've chosen the wrong computer
language.

Side projects
-------------

You won't get anywhere if all you do is follow an online tutorial and do the
exercises.  Even if it's a really good tutorial.

You have to take a solution
(yours, or the tutorial one if given) and try to critique the code.  Is
that a good way?  Could it be more readable?  Would a different algorithm be
faster or more clear?  Try to solve a more generalised problem than that given
in the tutorial.

I have found the early
`Google Code Jam <https://code.google.com/codejam/contests.html>`_ problems to
be very good at making you think and sweat, particularly those that have time
and memory constraints.  There are other sites that have problems you can try
[#]_.

Even better, after getting your first solution try to solve the exercise again
in a different language.  That's a really good way to learn your second
language!

You must write code to learn to program, and then analyse the code, tear it
apart and rewrite it.  Get your hands dirty.  It also helps if you read other
people's code.  Be critical if the code can be improved, and steal ideas if
the code is better than you would have written.

There is no better way to learn than by solving your own problems.  iTunes
mangling your playlists?  Write some code that creates
playlists the way you want them.  It's time to change passwords for the hundreds
of web sites that you use?  Write a little program to generate strong memorable
and *pronouncable* passwords with configurable password lengths and character
sets used.

Solving your own personal problems makes your learning more interesting, you
get closer to real-world programming and you get pushed into areas you might
not have been before.

Communication
-------------

It's important that you can communicate freely and well.  Even if you are a
native English speaker you need to work on your presentation.  If you are not
a native speaker then you have to do even more work.

When you work with programming languages you have to be very precise, and this
carries over into the written English language.
`Eric Raymond <http://www.catb.org/esr/faqs/hacker-howto.html#skills4>`_
explains why good English is important.

For example, I wrote the first draught of this in vim into a text file.  But I
copied it into LibreOffice so I could spellcheck it before I committed it.  I
hope that all my mistakes were caught, but probably not [#]_.

This applies even to the code you write.  You spent a lot of time and effort on
your code, didn't you?  So why doesn't it look like it?  The preface to the
first edition of `SICP <https://mitpress.mit.edu/sicp/>`_ has this quote:

::

    Programs must be written for people to read,
    and only incidentally for machines to execute. 

Summary
-------

After all that, I haven't yet answered the original question:

::

    What language should I learn first?

I hope you can see now that your first language doesn't really matter as you
will go on to learn many others if you become a working programmer.  However,
the way to knowledge can be smoother if you choose a language that doesn't
clutter your path with initially unnecessary complications.  You are really
learning how to solve problems with a computer.  The language is incidental.

If you are going to learn by yourself look at the support communities for your
language of choice, on-line tutorials, etc.

Be sure to expose yourself to other languages later on.  If you don't get some
exposure to other ideas and approaches you can get a distorted view of what is
possible in any solution you write.  Paul Graham talked about this in his essay
`Beating the Averages <http://www.paulgraham.com/avg.html>`_ in the section
*The Blub Paradox*.

My Recommendation for a First Language
--------------------------------------

After saying above that the first language you learn doesn't really matter, I'm
going to go ahead and give you a recommendation for a first language.  Why would
I do that?

Some people just need a shove to get going.  They won't just pick a language and
start, so I recommend one that I think is useful as a training language but
won't limit advanced usage.

Most programmers of my era started with something like BASIC on an 8-bit
microcomputer.  This brain-damaging experience didn't seem to put many off then,
and that leads many to assume that Javascript (or Java, or C++) is fine to start
with now.  I disagree.

Modern computer languages are *much* more complicated now than they were.  I
remember taking
`Kernighan & Ritchie <https://en.wikipedia.org/wiki/C_(programming_language)#K.26R_C>`_
home one Friday night and starting to write moderately complicated production C
code on Monday.  That's a lot harder to do now when every language comes with
an `IDE <https://en.wikipedia.org/wiki/Integrated_development_environment>`_ 
and massive library.  Why burden beginners with all the minutiae of
modern languages *plus* a heavyweight IDE when they don't even know what a
*while* loop is?

And that means starting with a language with a
`REPL <https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop>`_.
It's simpler to do that than start talking about files and editors and make and
compilers and linkers and whatever.  Using an IDE like VisualStudio or Eclipse
means you don't have to know all that, but I believe it's overly demanding at
the beginning.  Yes, IDEs *help* the student but that's because the student
really needs help with the massive language structure.

Learning computing using a language with a REPL makes it easy to experiment
with small bits of code, see the results immediately and see the result of
errors.  I suspect that's why BASIC was successful back in the dawn of personal
computing, besides being just about the only language available.

It's better to start simple and progress into more complicated things later.
Start with procedural programming, learn about loops, functions and all that.
Then advanced data structures, external to the language if possible.  It's
better to write your own code to handle linked lists, for example, because when
you get to a language that has them built in or provided by a library you
actually know what is going on and why some things are slow and others are fast.

So my recommended starting language is: **Python**.  Yes, I am bigoted, but I
accept that other languages like Ruby may be just as good.

Many other beginner languages are recommended by others. Javascript, for
instance, is often recommended but I believe it unnecessarily hard for beginners
with too many special cases and
`wat! <https://www.destroyallsoftware.com/talks/wat>`_ moments, plus its
non-mainstream prototyping system.

Python is a relatively simple language to start with, but it is powerful.  Much
of that power is hidden away but is available when you need it.

Python has too many good data structures built-in to be a *really* good teaching
language [#]_.  To learn the bones of linked lists and hash tables you 
really should implement them in something like C or assembler.  You can
implement them in Python, of course, but most students aren't shown that because
the language has perfectly good built-in lists and dictionaries [#]_.

So Python is simple.  But that doesn't mean it's limiting like other simple
languages such as BASIC.  With Python you also have a pretty good
object-oriented environment, you just aren't forced to use it as you are with
Java.  Python also has limited functional programming features, though
other languages are better in this respect.

Once you can handle all that Python itself offers there is a large library of
built-in standard library modules that allow you to do just about anything you
want to do.  And after that there is the even larger library of modules in
`the CheeseShop <https://pypi.python.org/pypi>`_.

The other reason for choosing Python is the user community.  This is where you
can get questions answered, pick up ideas and generally wallow in the
experience!  You should start in
`/r/learnpython <https://www.reddit.com/r/learnpython>`_, of course.

Good luck!


Further Reading
---------------

http://norvig.com/21-days.html

http://www.catb.org/esr/faqs/hacker-howto.html

http://www.linuxjournal.com/article/3882

https://docs.python.org/2/tutorial/index.html

http://www.greenteapress.com/thinkpython/thinkpython.pdf

http://python.swaroopch.com/


.. [#] I'm not putting down the 'average' majority.  Despite almost 40 years of programming experience I still consider myself average.
.. [#] We will encourage you to develop the three great virtues of a programmer: *laziness*, *impatience*, and *hubris*.  `Larry Wall <http://c2.com/cgi/wiki?LazinessImpatienceHubris>`_, *Programming Perl* (1st edition), OreillyAndAssociates
.. [#] One I want to try is `GitLab <https://about.gitlab.com>`_.
.. [#] For instance, `/r/dailyprogrammer <https://www.reddit.com/r/dailyprogrammer>`_.
.. [#] Alas, after committing I found some grammar errors.  Grammar is hard.
.. [#] A good training language, like a good training aircraft, should be easy to use, but demanding to use well.  In the computer training language context, this means the beginner should be able to get started and make satisfying progress initially, without being constrained later on after progressing to more advanced usage.
.. [#] Maybe a good small python exercise would be to write code to create, use and destroy linked lists.  Revisit this subject later when touching on API design, unit testing and object-oriented classes.
