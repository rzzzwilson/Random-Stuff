# OP's solution

def string_splosion(str):
    result = ' '
    for char in range(len(str)):
        result = result + str[:char+1]
    return result

s = 'abcdef'
print(f"s='{s}', string_splosion('{s}')='{string_splosion(s)}'")
