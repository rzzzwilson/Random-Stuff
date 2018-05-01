import string
# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

# create list of counters for all lower case letters
counters = [0 for x in string.ascii_lowercase]

# some random text
text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do '
        'eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim '
        'ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut '
        'aliquip ex ea commodo consequat. Duis aute irure dolor in '
        'eprehenderit in voluptate velit esse cillum dolore eu fugiat nulla '
        'pariatur. Excepteur sint occaecat cupidatat non proident, sunt in '
        'culpa qui officia deserunt mollit anim id est laborum.')

# count A-Z letters in 'text'
for ch in text:
    ch = ch.lower()
    if ch in string.ascii_lowercase:
        index = string.ascii_lowercase.find(ch)
        counters[index] += 1

print(counters)
