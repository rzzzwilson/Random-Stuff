def parse_args(strn):
    result = []
    quote_words = []        # tmp: holds quoted words
    state = 'outside quotes'
    for word in strn.split():
        if state == 'inside quotes':
            # inside a quote
            if word.startswith('"'):
                raise ValueError(f'{word}: open quote but already quoting?')
            if word.endswith('"'):
                quote_words.append(word[:-1])
                result.append(f"{' '.join(quote_words)}")
                quote_words = []
                state = 'outside quotes'
            else:
                quote_words.append(word)
        else:
            # outside any quotes
            if word.endswith('"'):
                raise ValueError(f'{word}: close quote without open?')
            if word.startswith('"'):
                state = 'inside quotes'
                quote_words.append(word[1:])
            else:
                result.append(word)
    # if still inside quote, error
    if state == 'inside quotes':
        raise ValueError('Unclosed quote?')
    return result

test = 'one two three four five six seven eight'
print(f'test={test}')
result = parse_args(test)
print(f'result={result}')
print()

test = 'one two "three four" five "six seven" eight'
print(f'test={test}')
result = parse_args(test)
print(f'result={result}')
print()

test = 'one two "three four" five six seven" eight'
try:
    print(f'test={test}')
    result = parse_args(test)
    print(f'result={result}')
except ValueError as e:
    print(f'Expected: {e}')
print()

test = 'one two "three four five "six seven eight'
try:
    print(f'test={test}')
    result = parse_args(test)
    print(f'result={result}')
except ValueError as e:
    print(f'Expected: {e}')
print()

test = 'one two "three four" five "six seven eight'
try:
    print(f'test={test}')
    result = parse_args(test)
    print(f'result={result}')
except ValueError as e:
    print(f'Expected: {e}')
print()
