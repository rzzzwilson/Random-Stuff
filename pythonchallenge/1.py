text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
map_url = "/pc/def/map.html"
map_url = "map"

a2z = 'abcdefghijklmnopqrstuvwxyz'
translate = a2z[2:] + a2z[:2]

def tl(s):
    result = ''
    for ch in s:
        if ch in " .'():/":
            result += ch
        else:
            val = ord(ch) - ord('a')
            new_val = translate[val]
            result += new_val
    return result

result = tl(text)
print result

result = tl(map_url)
print result
