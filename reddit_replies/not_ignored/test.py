import sys
filename = 'tmp.txt'
with open(filename, 'w') as f:
    f.write('abc\n')
    f.write('xyz\n')
with open(filename, 'r') as f:
    if 'abc' in f:
        print("'abc' is in file")
    else:
        print("'abc' NOT in file")

postsRepliedTo = ['abc', 'xyz', 'rst']
with open('X'+filename, 'w') as f:
    for postId in postsRepliedTo:
        if not(postId in f):
            f.write(postId + "\n")        
