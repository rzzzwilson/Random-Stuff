import time

with open('times.txt', 'r') as t:
    lines = t.read().strip().splitlines()

for (lnum, line) in enumerate(lines):
    (t, diclength) = line.strip().split()

    try:
        start_time = time.strptime(t, '%H:%M:%S')      # normal format
    except ValueError:
        try:
            start_time = time.strptime(t, '%M:%S')     # try for just minutes/seconds
        except ValueError:
            try:
                start_time = time.strptime(t, '%S')    # or just seconds
            except ValueError:
                raise RuntimeError(f'Bad format on line {lnum+1}: "{line}"')

    dicstart = time.strftime('%H:%M:%S', start_time)
    print(dicstart, diclength)
