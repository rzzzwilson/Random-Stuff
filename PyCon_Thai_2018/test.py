import unittest

def compress(a):
    """Compress string 'a' using RLE."""

    lastch = None
    count = 0
    result = ''

    for ch in a:
        if ch != lastch:
            if count > 1:
                result += str(count)
            count = 1
            result += ch
            lastch = ch
        else:
            count += 1
    if count > 1:
        result += str(count)

    return result

class MyTest(unittest.TestCase):
    def test1(self):
        a = 'abbccc'
        expected = 'ab2c3'
        result = compress(a)
        self.assertEqual(expected, result)

    def test2(self):
        a = 'abbcccd'
        expected = 'ab2c3d'
        result = compress(a)
        self.assertEqual(expected, result)

    def test3(self):
        a = 'abbcdd'
        expected = 'ab2cd2'
        result = compress(a)
        self.assertEqual(expected, result)

    def test4(self):
        a = 'abbcdeed'
        expected = 'ab2cde2d'
        result = compress(a)
        self.assertEqual(expected, result)

    def test5(self):
        a = 'abcdcdee'
        expected = 'abcdcde2'
        result = compress(a)
        self.assertEqual(expected, result)

    def test6(self):
        a = 'abcdcdccjweeeeeee'
        expected = 'abcdcdc2jwe7'
        result = compress(a)
        self.assertEqual(expected, result)

#unittest.main()

a = 'seeevvvvvzzzzzzzzooollpqqgggggggggbbbbbbbaaaaaawwwwwwwccccccccjwwwwwwwwwlllceeeeeebbbbbbbbbbttttssssssssslllllsssssssssfffffff'
result = compress(a)
print('result =', result)
