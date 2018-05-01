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
from pprint import pprint

test_paths = ['/root/abc/xyz/1.ext',
              '/root/abc/pqr/2.ext',
              '/root/abc/xyz/3.ext',
              '/root2/abc/xyz/3.ext',
              # add more here to test
             ]

def paths2dictlist(paths):
    """Convert all paths in 'paths' to a list of dictionaries."""

    result = []     # accumulate data here

    for path in paths:
        path_names = path.split('/')
        curr_dir = result

        for name in path_names:
            if not name:
                continue    # ignore blank file/dir names

            # see if name already in current dir list
            for d in curr_dir:
                if d['name'] == name:
                    # found 'name', move to 'children' list for next name in path
                    curr_dir = d['children']
                    break
            else:
                # didn't break, so 'name' not in current dir list, add it
                new_child_list = []
                curr_dir.append({'name': name, 'children': new_child_list})
                curr_dir = new_child_list

    return result

result = paths2dictlist(test_paths)
json_result = json.dumps(result, sort_keys=True, indent=4)
print(json_result)
