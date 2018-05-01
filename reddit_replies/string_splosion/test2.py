# my solution

def string_splosion(string):
    result = [string[:index+1] for index in range(len(string))]
    return ''.join(result)

s = ''
print(f"string_splosion('{s}')='{string_splosion(s)}'")

s = 'X'
print(f"string_splosion('{s}')='{string_splosion(s)}'")

s = 'abcdef'
print(f"string_splosion('{s}')='{string_splosion(s)}'")
