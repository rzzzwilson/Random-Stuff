import os

#old_dir = '/Users/User/Desktop/MyFolder'
old_dir = './folder'

for f in os.listdir(old_dir):
    file_name, file_ext = os.path.splitext(f)
    file_name.split('-')

    split_file_name = file_name.split('-')

    new_dir = os.path.join(old_dir,
                           '-'.join(split_file_name[:3]),
                           split_file_name[5],
                           f)

    print(f"os.rename('{os.path.join(old_dir, f)}', '{new_dir}')")
#    os.rename(os.path.join(old_dir, f), new_dir)
