import unittest

# По фамилии был выбран 17 вар

def gen_bin_tree(height: int = 4, root: int = 17) -> dict:
    """
    Рекурсивно строит бинарное дерево заданной высоты с указанным корнем.
    Левый потомок вычисляется по формуле: (root - 4) ** 2
    Правый потомок вычисляется по формуле: (root + 3) * 2
    """

    if height <= 1:
        return {"value": root, "left": None, "right": None}

    left_value = (root - 4) ** 2
    right_value = (root + 3) * 2

    left_subtree = gen_bin_tree(height - 1, left_value)
    right_subtree = gen_bin_tree(height - 1, right_value)

    return {
        "value": root,
        "left": left_subtree,
        "right": right_subtree
    }


tree = gen_bin_tree(height=4, root=17)
print(tree)


class TestMath(unittest.TestCase):

    def test_root(self):
        self.assertEqual(gen_bin_tree(1, 5), ({'value': 5, 'left': None, 'right': None}))

    def test_mid(self):
        self.assertEqual(gen_bin_tree(3, 5), ({'value': 5, 'left': {'value': 1, 'left': {'value': 9, 'left': None, 'right': None}, 'right': {'value': 8, 'left': None, 'right': None}}, 'right': {'value': 16, 'left': {'value': 144, 'left': None, 'right': None}, 'right': {'value': 38, 'left': None, 'right': None}}}))

    def test_hard(self):
        self.assertEqual(gen_bin_tree(5, 5), ({'value': 5, 'left': {'value': 1, 'left': {'value': 9, 'left': {'value': 25, 'left': {'value': 441, 'left': None, 'right': None}, 'right': {'value': 56, 'left': None, 'right': None}}, 'right': {'value': 24, 'left': {'value': 400, 'left': None, 'right': None}, 'right': {'value': 54, 'left': None, 'right': None}}}, 'right': {'value': 8, 'left': {'value': 16, 'left': {'value': 144, 'left': None, 'right': None}, 'right': {'value': 38, 'left': None, 'right': None}}, 'right': {'value': 22, 'left': {'value': 324, 'left': None, 'right': None}, 'right': {'value': 50, 'left': None, 'right': None}}}}, 'right': {'value': 16, 'left': {'value': 144, 'left': {'value': 19600, 'left': {'value': 384003216, 'left': None, 'right': None}, 'right': {'value': 39206, 'left': None, 'right': None}}, 'right': {'value': 294, 'left': {'value': 84100, 'left': None, 'right': None}, 'right': {'value': 594, 'left': None, 'right': None}}}, 'right': {'value': 38, 'left': {'value': 1156, 'left': {'value': 1327104, 'left': None, 'right': None}, 'right': {'value': 2318, 'left': None, 'right': None}}, 'right': {'value': 82, 'left': {'value': 6084, 'left': None, 'right': None}, 'right': {'value': 170, 'left': None, 'right': None}}}}}))

unittest.main(argv=[''], verbosity=2, exit=False)        
