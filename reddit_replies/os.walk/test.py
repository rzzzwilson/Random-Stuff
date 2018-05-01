import os
user_input = raw_input("Enter the path of your file: ") 
for (root, directories, filenames) in os.walk(user_input):
    print('root=%s' % root)
    print('directories=%s' % directories)
    print('filenames=%s' % filenames)
    print('----------------------------------')
