class Test(object):

    def __init__(self):
        """Set instance .number to 0."""

        self.number = 0

    def bump_print(self, bump):
        """Bump the .number and then print it."""

        self.number += bump
        print('.number=%d' % self.number)

a = Test()
a.bump_print(2)
a.bump_print(3)
