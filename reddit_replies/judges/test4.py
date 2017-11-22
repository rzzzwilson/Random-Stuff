#!/usr/bin/env python3

"""
Exploratory code used to help answer:

    https://www.reddit.com/r/learnpython/comments/7efv4q/beginner_trying_to_learn_python_basic_logic/

Assigns papers in a way such that the 'sharing' is spread out evenly.  We do this
by keeping a 'peers' list for each judge and when a paper is given to a judge we
allocate the second paper to the next in the 'peers' list on a round-robin basis.

We introduce an object for each Judge.  This object contains:
    . the judge name
    . the papers allocated to the judge
    . a list of peers (ie, all judges minus this one)
    . an index into the list of peers
"""

import random


class Judge:
    def __init__(self, name, jlist):
        """Initialize a Judge."""

        self.name = name
        self.peers = jlist[:]       # copy judge list
        self.peers.remove(name)     # remove this judge in the copy
        random.shuffle(self.peers)  # randomize the peers
        self.index = 0              # index into self.peers
        self.papers = []            # allocated papers

    def next_peer(self):
        """Get the next peer for this judge."""

        # get next index, bump and wrap-around
        index = self.index
        self.index += 1
        if self.index >= len(self.peers):
            self.index = 0
        return self.peers[index]

    def allocate_paper(self, paper):
        """Allocate a paper to this judge."""

        self.papers.append(paper)

    def num_papers(self):
        """Get number of papers for this judge."""

        return len(self.papers)

    def get_papers(self):
        """Get papers allocated to this judge."""

        return self.papers

    def __repr__(self):
        return f'Judge<{self.name}, {self.peers}, {self.index}, {self.papers}>'

# set size of lists
num_papers = 100
num_judges = 9

# create lists
papers = ['paper_%03d' % i for i in range(num_papers)]
judges = ['judge_%02d' % i for i in range(num_judges)]

# create dict for Judge objects
judges_dict = {j:Judge(j, judges) for j in judges}

# index into 'judges' for next judge to select
next_judge = 0

# allocate papers
while papers:
    # get a paper
    paper = papers.pop()

    # select first judge, allocate paper
    j1 = judges[next_judge]
    next_judge += 1
    if next_judge >= len(judges):
        next_judge = 0
    j1_obj = judges_dict[j1]
    j1_obj.allocate_paper(paper)

    # select second judge, round-robin in the j1 'peers'
    next_peer = j1_obj.next_peer()
    j2_obj = judges_dict[next_peer]
    j2_obj.allocate_paper(paper)

# check number of papers allocated to each judge
for (k, v) in judges_dict.items():
    print(f'{k}: num papers={v.num_papers()}')
