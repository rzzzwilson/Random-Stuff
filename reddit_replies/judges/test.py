#!/usr/bin/env python3

"""
Exploratory code used to help answer:

    https://www.reddit.com/r/learnpython/comments/7efv4q/beginner_trying_to_learn_python_basic_logic/

This solution just uses a naive random.choice() selection of judges.
This will distribute papers unevenly.  See test2.py for a perhaps better solution.
"""

import random


# set size of lists
num_papers = 100
num_judges = 9

# create lists
papers = ['paper_%03d' % i for i in range(num_papers)]
judges = ['judge_%02d' % i for i in range(num_judges)]

# create dict for judge allocated papers
judges_dict = {j:[] for j in judges}

# allocate papers
while papers:
    # get a paper
    paper = papers.pop()

    # select two judges
    j1 = random.choice(judges)
    tmp_list = judges[:]    # copy judge list
    tmp_list.remove(j1)     # remove 'j1' in the copy
    j2 = random.choice(tmp_list)

    # allocate paper to both judges
    judges_dict[j1].append(paper)
    judges_dict[j2].append(paper)

# check number of papers allocated to each judge
for (k, v) in judges_dict.items():
    print('%s: num papers=%d' % (k, len(v)))
