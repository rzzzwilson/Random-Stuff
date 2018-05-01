import string

encrypt_dict = {k: v for (k, v) in zip(string.ascii_lowercase, string.ascii_lowercase[::-1])}
upper_encrypt = {k: v for (k, v) in zip(string.ascii_uppercase, string.ascii_uppercase[::-1])}
encrypt_dict.update(upper_encrypt)

def encrypt(message):
    result = []
    for c in message:
        result.append(encrypt_dict.get(c, c))
    return ''.join(result)

print(encrypt('AbcXyz'))
print(encrypt('Hello World!'))
