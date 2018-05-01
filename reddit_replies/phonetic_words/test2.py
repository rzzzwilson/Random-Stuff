#!/usr/bin/env python3

"""
Code investigating /r/learnpython question:

https://www.reddit.com/r/learnpython/comments/7t3jc3/question_on_sentences_and_lists/

This approach handles the NATO words as a stream and uses a trailing '.'
as a trigger to add the between-word ' '.

NOTE: We don't use .join() below.  While that is the 'proper' way to join
      strings, using '+' pasting is simpler for the beginner.
"""

nwords = ('Tango Hotel India Sierra. India Sierra. Alpha November. '
          'Echo X-ray Alpha Mike Papa Lima Echo.')

print(' input=%s' % nwords)
sentence = ''                   # final sentence grows here
nword_list = nwords.split()     # split into list of NATO words, trailing '.' means end of word

for nword in nword_list:        # for each NATO word:
    sentence += nword[0]    # save first letter
    if nword.endswith('.'): # if last char is '.' it's an end of word
        sentence += ' '     # add inter-word space
print('output=%s' % sentence)
