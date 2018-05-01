"""
Try a simple strip/split approach.
"""

def read_data(lines):
    for (lnum, line) in enumerate(lines):
        (t, diclength) = line.strip().split()
        t_split = t.split(':')
        if len(t_split) == 3:
            (h, m, s) = t_split
        elif len(t_split) == 2:
            h = 0
            (m, s) = t_split
        elif len(t_split) == 1:
            (h, m) = (0, 0)
            s = t_split[0]
        else:
            raise ValueError(f'Bad time format on line {lnum+1}: "{line}"')
        h = int(h)
        m = int(m)
        s = int(s)
        print(f'dicstart={h:02d}:{m:02d}:{s:02d}, diclength={diclength}')

with open('times.txt', 'r') as t:
    lines = t.read().strip().splitlines()

read_data(lines)
