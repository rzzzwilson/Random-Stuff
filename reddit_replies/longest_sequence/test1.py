def longest_ordered(s):
    """Find longest ordered subsequence is string 's'.

    Returns the longest subsequence if found, else returns None.
    """

    # use a finite state machine approach
    curr_ndx = 0        # index of start of current sequence
    curr_len = 0        # length of current sequence
    
    ans_ndx = None      # index of start of answer sequence
    ans_len = 0         # length of answer sequence
    
    last_ord = 0        # ord() value of last character
    
    # step through each character of string, with index
    for (i, ch) in enumerate(s):
        if ord(ch) == last_ord + 1:
            # we have another char that is in alphabetical sequence
            # 'curr_ndx' should already be set
            curr_len += 1       # add one to length
            last_ord += 1       # remember this for next check
        else:
            # not in sequence, prepare for new sequence
            if curr_len > ans_len:
                # current sequence is new answer
                ans_ndx = curr_ndx
                ans_len = curr_len

            # current char could be start of new sequence
            curr_len = 1
            curr_ndx = i
            last_ord = ord(ch)
   
    # check if we were tracking a longer sequence than latest answer
    if curr_len > ans_len:
        ans_ndx = curr_ndx
        ans_len = curr_len

    # if we have an answer, return subsequence
    if ans_ndx is not None:
        return s[ans_ndx:ans_ndx + ans_len]

    # else return None
    return None
   
test_cases = [
              'zyx',
              'xabcdefghijy',
              'xabcdefghij',
              'abcdefghijx',
              'abcdefghij',
              'anaghjshb sbgdfbsnshssghstjsjyyasabcdefggreageragaergareg',
              'hagsfdabcdefasdasdabcqweqwerstuvwxyzqweabcqwe'
             ]

for s in test_cases:
    print(f"#### testing: '{s}'")
    result = longest_ordered(s)
    if result:
        print(f"longest ordered sequence is {len(result)} chars: '{result}'")
    else:
        print('no ordered sequence found')
