    def encrypt(message):
        result = ''
        for c in message:
            if c > 'Z':     # if lowercase
                enc_offset = ord('z') - ord(c)
                enc_c = chr(ord('a') + enc_offset)
            else:           # is uppercase
                enc_offset = ord('Z') - ord(c)
                enc_c = chr(ord('A') + enc_offset)
            result = result + enc_c
        return result
    
    print(encrypt('AbcXyz'))
