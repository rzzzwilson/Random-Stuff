# test code answering reddit post:
# https://www.reddit.com/r/learnpython/comments/8cu9qg/what_do_you_do_if_the_list_of_values_of_a_key_in/

def command_add(date, data, calendar):
    new_list = calendar.get(date, [])
    new_list.append(data)
    calendar[date] = new_list


def command_delete(date, entry_number, calendar):
    """ (str, int, dict) -> str
    
    Delete the entry at calendar[date][entry_number]
    
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    
    date: A string date formatted as "YYYY-MM-DD"
    entry_number: An integer indicating the entry in calendar[date] to delete
    calendar: The calendar database
    
    return: a string indicating any errors, "" for no errors
    """

    if date in calendar:
        if calendar[date]:
            # list not empty
            if entry_number >= len(calendar[date]):
                return f'There is no entry {entry_number} on the date {date} in the calendar'
            del calendar[date][entry_number]
        else:
            # list is empty
            del calendar[date]
    # if date not in calendar we do nothing, according to requirements

    return ''

calendar = {}
x = command_add("2017-03-11", "CSCA08 test 2", calendar)
x = command_add("2017-03-11", "go out with friends after test", calendar)
result = command_delete("2017-03-11", 3, calendar)
print(f'result={result}')
