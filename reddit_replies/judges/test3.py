#!/usr/bin/env python3

"""
Exploratory code used to help answer:

    https://www.reddit.com/r/learnpython/comments/7efv4q/beginner_trying_to_learn_python_basic_logic/

Assigns papers to judges on a round-robin basis.  The papers "overlap",
that is, judge 0 gets paper 0, judge 1 gets 0,
         judge 1 gets paper 1, judge 2 gets 1,
         etc
"""

# set size of lists
num_papers = 100
num_judges = 9

# create lists
papers = ['paper_%03d' % i for i in range(num_papers)]
judges = ['judge_%02d' % i for i in range(num_judges)]

# create dict for judge allocated papers
judges_dict = {j:[] for j in judges}

# index into 'judges' for next judge to select
next_judge = 0

# allocate papers
while papers:
    # get a paper
    paper = papers.pop()

    # select first judge, bump index to second judge
    # wrap next_judge around if necessary
    j1 = judges[next_judge]
    next_judge += 1
    if next_judge >= len(judges):
        next_judge = 0

    # select second judge
    j2 = judges[next_judge]

    # allocate paper to both judges
    judges_dict[j1].append(paper)
    judges_dict[j2].append(paper)

# check number of papers allocated to each judge
for (k, v) in judges_dict.items():
    print('%s: num papers=%d' % (k, len(v)))
#print(str(judges_dict))
