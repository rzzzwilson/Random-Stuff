# code investigating:
# https://ps.reddit.com/r/learnpython/comments/8eowne/python_help_with_protein_sequences/

datafile = 'NW-84.fungi.blastp'

with open(datafile, 'r') as f:
    lines = f.readlines()
print('lines[0]=%s' % lines[0])
print('len(lines)=%d' % len(lines))

#first_items = []
#for line in lines:
#    first_field = line.split('|')[0]
#    first_items.append(first_field)

first_items = [line.split('|')[0] for line in lines]
print('first_items=%s' % first_items)
print('len(first_items)=%d' % len(first_items))
