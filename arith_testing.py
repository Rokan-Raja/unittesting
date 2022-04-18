import arithmetic
import unittest

class testcase(unittest.TestCase):

    def test_add(self):
        add=arithmetic.add(10,6)
        self.assertEqual(add,16)

    def test_sub(self):
        sub=arithmetic.subtract(10,6)
        self.assertEqual(sub,4)

    def test_mul(self):
        mul=arithmetic.mul(10,6)
        self.assertEqual(mul,60)

    def test_div(self):
        div=arithmetic.div(10,4)
        self.assertEqual(div,2.5)


if __name__ == '__main__':
    unittest.main()