import unittest

def get_list_common_prefix(a, b):
    """Get number of common prefix elements of two lists."""

    result = 0
    for (a_elt, b_elt) in zip(a, b):
        if a_elt != b_elt:
            break
        result += 1
    return result


class SimpleTest(unittest.TestCase):
    def test1(self):
        a = [1, 2, 3]
        b = [1, 2, 4]
        expected = 2
        result = get_list_common_prefix(a, b)
        msg = f'get_list_common_prefix({a}, {b})={result}, expected {expected}'
        self.assertEqual(expected, result, msg)

    def test2(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        expected = 3
        result = get_list_common_prefix(a, b)
        msg = f'get_list_common_prefix({a}, {b})={result}, expected {expected}'
        self.assertEqual(expected, result, msg)

    def test3(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        expected = 0
        result = get_list_common_prefix(a, b)
        msg = f'get_list_common_prefix({a}, {b})={result}, expected {expected}'
        self.assertEqual(expected, result, msg)

    def test4(self):
        a = [1, 2, 3]
        b = [4, 2, 3]
        expected = 0
        result = get_list_common_prefix(a, b)
        msg = f'get_list_common_prefix({a}, {b})={result}, expected {expected}'
        self.assertEqual(expected, result, msg)

unittest.main()
