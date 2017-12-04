From:

https://www.reddit.com/r/learnpython/comments/7h6w8v/socket_questions_slow_results/

**test.py** is OP original code.

**test2.py** is my threaded code.

Results with and without timeout plus different numbers of threads:

| # threads |no timeout|with timeout|
+===========+==========+============+
|1 thread|1m43s|1m43s|
+-----------+----------+------------+
|250 threads|0m20s|0m01s|
+-----------+----------+------------+
