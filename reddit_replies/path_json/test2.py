"""
Code to experiment converting a list of paths like:

    paths = ['/root/abc/xyz/1.ext',
             '/root/abc/pqr/2.ext',
            ]

into a list of structured dictionaries where each file/directory
in a path is represented by a dictionary with this structiure:

    {'name': <file/dir name>,
     'children': [{dict}, {dict}, ...}]
    }
"""

import json

test_paths = ['/root/abc/xyz/1.ext',
              '/root/abc/pqr/2.ext',
              '/root/abc/xyz/3.ext',
              '/root2/abc/xyz/3.ext',
              # add more here to test
             ]

def path2dictlist(path_list, curr_list):
    """Convert 'path_lis' to dictionaries in curr_list.
    
    path_list  list containing path names to process
    curr_list  list of dictionaries to update
    """

    # recursion base-case test
    if not path_list:
        return

    # get next name and remove from 'path_list'
    name = path_list[0]
    path_list = path_list[1:]

    # see if name already in current dir list
    for d in curr_list:
        if d['name'] == name:
            # found 'name', move to 'children' list for next name in path
            curr_list = d['children']
            break
    else:
        # didn't break, so 'name' not in current dir list, add it
        new_child_list = []
        curr_list.append({'name': name, 'children': new_child_list})
        curr_list = new_child_list

    # here we've added 'name' to the children list (or it was already there)
    # 'curr_list' now points to the children list for 'name'

    # do rest of names in path
    path2dictlist(path_list, curr_list)

result_list = []

for path in test_paths:
    path_list = path.split('/')[1:]
    path2dictlist(path_list, result_list)

json_result = json.dumps(result_list, sort_keys=True, indent=4)
print(json_result)
