myList = ['fire','fireman','fire truck', 'dalmatian','laddar']

import fnmatch
pattern = 'fire*'
matching = fnmatch.filter(myList,pattern)
print(f'matching={matching}')
