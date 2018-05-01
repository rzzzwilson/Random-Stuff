firstfile = 'some_directory_1'
secondfile = 'some_directory_2'

with open(firstfile) as input_file:
    with open(secondfile, "w") as output_file:
        for line in input_file:
            output_file.write(line.strip())
