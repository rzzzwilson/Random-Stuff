#!/usr/bin/env python3

"""
Code investigating /r/learnpython question:

https://www.reddit.com/r/learnpython/comments/7t3jc3/question_on_sentences_and_lists/

This approach splits the NATO words on '.' first to get words.  Then process
words to get characters.  This was the first approach that I thought of, but
see test2.py!
"""

nwords = ('Tango Hotel India Sierra. India Sierra. Alpha November. '
          'Echo X-ray Alpha Mike Papa Lima Echo.')

print(' input=%s' % nwords)
sentence_list = []              # gather final words here
word_list = nwords.split('.')   # split on '.', get list of NATO words making one final word
for word in word_list:          # for each word
    if word:                                # if word is not empty
        nchar_list = word.split()           # split into NATO character words
        word_ch_list = []
        for ch in nchar_list:               # save start letter into 'word_list'
            word_ch_list.append(ch[0])
        final_word = ''.join(word_ch_list)  # gather initial chars into final word
        sentence_list.append(final_word)    # save final word in 'word_list'
sentence = ' '.join(sentence_list)          # make sentence with spaces between words
print('output=%s' % sentence)
