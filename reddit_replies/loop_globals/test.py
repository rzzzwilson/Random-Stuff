#!/usr/bin/env python3

def more_work(val):
    print(f'more_work: val={val}')

def main():
    last_value = 0
    while True:
        val_str = input('Next number: ').strip()
        if not val_str:
            break
        try:
            val = int(val_str)
        except ValueError:
            print(f"Sorry, '{val_str}' isn't a valid number.")
            continue
        new_value = last_value + val
        print(f'Sum so far is {new_value}')
        last_value = new_value

        more_work(val)

main()
