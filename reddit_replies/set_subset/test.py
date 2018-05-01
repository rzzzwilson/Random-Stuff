input_data = [[0],[1,2],[1,3],[1,2,3],[4,5],[4,5]]
expected = [[0],[1,2,3],[4,5]]

result = []

for i_elt in input_data:
    i_set = set(i_elt)
    # check if the 'i_set' set has any common elements with any result set
#    handled = False      # assume we didn't merge this set
    for (i, r_set) in enumerate(result):
        if i_set & set(r_set):
            # i_set and r_set have something in common
            print(f'common sets: i_set={i_set}, r_set={r_set}')
            # merge i_set and r_set and make it the *new* r_set
            result[i] = i_set | set(r_set)
#            handled = True
            break
    else:
        # if we get here we didn't merge i_elt, make a new result set
        result.append(set(i_elt))

print(f'expected={expected}, got={result}')
