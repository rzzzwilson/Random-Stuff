# fake the file read. same data as if we did:
# with open(<file>, r) as f:
#     line_data = f.readlines()
line_data = (
             '15/04/09 T9999999999999999 fname, lname 12345678 650.00\n',
             '15/04/09 T8888888888888888 fname2, lname2 D 23456789 445.00\n',
             '15/04/09 777777777T7777777 fname3, lname3 J 34567890 1036.00\n',
            )

for line in line_data:
    line = line.strip('\n')
    if not line:       # if an empty line (usually end)
        continue       # skip, try next

    print(f'    line="{line}"')

    new_line = line.replace(',', ' ')
    print(f'new_line="{new_line}"')

    fields = new_line.split()
    if len(fields) == 6:        # missing middle initial?
        fields.insert(4, '')    # insert empty string for MI

    print(f'fields={fields}\n')
