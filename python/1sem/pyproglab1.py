import unittest

def sumoftwo(nums, target):
    try:
        c = True
        for n in range(len(nums)):
            n1 = nums[n]
            for nn in range(len(nums)):
                if nn == n:
                    pass
                else:
                    n2 = nums[nn]
                    if n1 + n2 == target:
                        return [n, nn]
        else:
            if c:
                return "Такой пары нет"

    except Exception as e:
        print("Error:", e)

class TestMath(unittest.TestCase):
    def test1(self):
        self.assertEqual(sumoftwo([3, 3], 6), [0, 1])

    def test2(self):
        self.assertEqual(sumoftwo([2,7,11,15], 9), [0, 1])

    def test3(self):
        self.assertEqual(sumoftwo([3,2,4], 6), [1, 2])

unittest.main(argv=[''], verbosity=2, exit=False)
