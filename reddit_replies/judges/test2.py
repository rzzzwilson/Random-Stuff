#!/usr/bin/env python3

"""
Exploratory code used to help answer:

    https://www.reddit.com/r/learnpython/comments/7efv4q/beginner_trying_to_learn_python_basic_logic/

Uses random.choices() to "weight" the judge selection to make a judge with
less papers be more likely to be chosen.
"""

import random


# set size of lists
num_papers = 100
num_judges = 9
avg_papers = (num_papers * 2) // num_judges
print('num_papers=%d, num_judges=%d, avg_papers=%d' % (num_papers, num_judges, avg_papers))

# create lists
papers = ['paper_%03d' % i for i in range(num_papers)]
judges = ['judge_%02d' % i for i in range(num_judges)]

# create dict for judge allocated papers
judges_dict = {j:[] for j in judges}

# allocate papers
while papers:
    # get a paper
    paper = papers.pop()

    # select first judge
    weights = [(num_papers*2 - len(judges_dict[x])) // avg_papers for x in judges]
    print('j1: weights=%s' % str(weights))
    j1 = random.choices(judges, weights)[0]     # we only chose one, get it from list
    print('j1=%s' % j1)

    # make copy of judge list minus first chosen judge
    tmp_list = judges[:]    # copy judge list
    print('tmp_list=%s' % str(tmp_list))
    tmp_list.remove(j1)     # remove 'j1' in the copy
    
    # select second judge
    weights = [(num_papers*2 - len(judges_dict[x])) // avg_papers for x in tmp_list]
    print('j2: weights=%s' % str(weights))
    j2 = random.choices(tmp_list)[0]
    print('j2=%s' % j2)

    # allocate paper to both judges
    judges_dict[j1].append(paper)
    judges_dict[j2].append(paper)

# check number of papers allocated to each judge
for (k, v) in judges_dict.items():
    print('%s: num papers=%d' % (k, len(v)))
