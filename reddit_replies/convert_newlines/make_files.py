"""
Write small text files with newlines:
    * \n
    * \r
    * \r\n
"""

with open('file_n.txt', 'w', newline='\n') as f:
    f.write('alpha\n')
    f.write('beta\n')
    f.write('gamma\n')

with open('file_r.txt', 'w', newline='\r') as f:
    f.write('alpha\n')
    f.write('beta\n')
    f.write('gamma\n')

with open('file_rn.txt', 'w', newline='\r\n') as f:
    f.write('alpha\n')
    f.write('beta\n')
    f.write('gamma\n')


