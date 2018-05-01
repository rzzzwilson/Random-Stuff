    # we define the lie data here.  we could have read this from a file like this:
    #   with open(<file>, 'r') as f:
    #       line_data = f.readlines()
    
    line_data = [
                 '15/04/09 T9999999999999999 fname, lname          12345678                650.00\n',
                 '15/04/09 T8888888888888888 fname2, lname2 D      23456789                445.00\n',
                 '15/04/09 777777777T7777777 fname3, lname3 J      34567890               1036.00\n'
                 #012345678901234567890123456789012345678901234567890123456789012345678901234567890
                ]
    
    # field columns
    field_columns = [(0, 8), (9, 26), (27, 41), (42, 43), (49, 57), (58, 80)]
    
    
    for line in line_data:
        line = line.strip('\n')     # get rid of trailing '\n'
        if not line:                # if an empty line, ignore
            continue 
    
        print(f'line="{line}"')
    
        fields = []
        for (left, right) in field_columns:
            print(f'({left},{right}), line[:]={line[left:right]}')
            fields.append(line[left:right]) # get field and add to result list
    
        print(f'fields={fields}\n')
