#from test import step
from test2 import step
import unittest

Debug = False

class MyTest(unittest.TestCase):
    def test_basic_01(self):
        if Debug:
            print('test_basic_01')
        test = 'step(2,100,110)'
        expect = [101, 103]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_basic_02(self):
        if Debug:
            print('test_basic_02')
        test = 'step(4,100,110)'
        expect = [103, 107]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_basic_03(self):
        if Debug:
            print('test_basic_03')
        test = 'step(6,100,110)'
        expect = [101, 107]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_basic_04(self):
        if Debug:
            print('test_basic_04')
        test = 'step(8,300,400)'
        expect = [359, 367]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_basic_05(self):
        if Debug:
            print('test_basic_05')
        test = 'step(10,300,400)'
        expect = [307, 317]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_01(self):
        if Debug:
            print('test_1')
        test = 'step(2,100,110)'
        expect = [101, 103]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_02(self):
        if Debug:
            print('test_2')
        test = 'step(4,100,110)'
        expect = [103, 107]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_03(self):
        if Debug:
            print('test_3')
        test = 'step(6,100,110)'
        expect = [101, 107]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_04(self):
        if Debug:
            print('test_4')
        test = 'step(8,300,400)'
        expect = [359, 367]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_05(self):
        if Debug:
            print('test_5')
        test = 'step(10,300,400)'
        expect = [307, 317]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_06(self):
        if Debug:
            print('test_6')
        test = 'step(4,30000,100000)'
        expect = [30109, 30113]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_07(self):
        if Debug:
            print('test_7')
        test = 'step(6,30000,100000)'
        expect = [30091, 30097]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_08(self):
        if Debug:
            print('test_8')
        test = 'step(8,30000,100000)'
        expect = [30089, 30097]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_09(self):
        if Debug:
            print('test_9')
        test = 'step(11,30000,100000)'
        expect = None
        got = eval(test)
        self.assertEqual(got, expect)

    def test_10(self):
        if Debug:
            print('test_10')
        test = 'step(2,10000000,11000000)'
        expect = [10000139, 10000141]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_11(self):
        if Debug:
            print('test_11')
        test = 'step(52,1300,15000)'
        expect = [1321, 1373]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_12(self):
        if Debug:
            print('test_12')
        test = 'step(10,4900,5000)'
        expect = [4909, 4919]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_13(self):
        if Debug:
            print('test_13')
        test = 'step(30,4900,5000)'
        expect = [4903, 4933]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_14(self):
        if Debug:
            print('test_14')
        test = 'step(2,4900,5000)'
        expect = [4931, 4933]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_15(self):
        if Debug:
            print('test_15')
        test = 'step(2,104000,105000)'
        expect = [104087, 104089]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_16(self):
        if Debug:
            print('test_16')
        test = 'step(2,4900,4919)'
        expect = None
        got = eval(test)
        self.assertEqual(got, expect)

    def test_17(self):
        if Debug:
            print('test_17')
        test = 'step(7,4900,4919)'
        expect = None
        got = eval(test)
        self.assertEqual(got, expect)

    def test_18(self):
        if Debug:
            print('test_18')
        test = 'step(4,30115,100000)'
        expect = [30133, 30137]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_19(self):
        if Debug:
            print('test_19')
        test = 'step(4,30140,100000)'
        expect = [30319, 30323]
        got = eval(test)
        self.assertEqual(got, expect)

    def test_20(self):
        if Debug:
            print('test_20')
        test = 'step(4,30000,30325)'
        expect = [30109, 30113]
        got = eval(test)
        self.assertEqual(got, expect)


unittest.main()
