def encrypt(message):
    result = ''
    ord_az = ord('a') + ord('z')
    ord_AZ = ord('A') + ord('Z')
    for c in message:
        nc = ord(c)
        if c > 'Z':   # if lowercase
            nr = ord_az - nc
        else:         # is uppercase
            nr = ord_AZ - nc
        result = result + chr(nr)
    return result

print(encrypt('AbcXyz'))
