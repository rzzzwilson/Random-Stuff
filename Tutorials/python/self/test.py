class Test(object):

    def __init__(self):
        """Set instance .number to 0."""

        self.number = 0

    def inc_print(self, inc=1):
        """Increment the .number and then print it."""

        self.number += inc
        print('.number=%d' % self.number)

a = Test()
a.inc_print(2)
a.inc_print(3)
