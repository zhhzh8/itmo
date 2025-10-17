import unittest

# По фамилии был выбран 17 вар

def gen_bin_tree(height: int = 4, root: int = 17, left_branch = lambda x: (x - 4) ** 2, right_branch=lambda x: (x + 3) * 2) -> dict:
    """
    Нерекурсивно строит бинарное дерево заданной высоты с указанным корнем(Стандартно: height = 4, root = 17).
    Левый потомок(left_branch) вычисляется по заданной формуле(Стандартно: (root - 4) ** 2)
    Правый потомок(right_branch) вычисляется по заданной формуле(Стандарнто: (root + 3) * 2)
    """

    tree = {"value": root, "left": None, "right": None}
    
    queue = [(1, tree)]

    while queue:
        level, node = queue.pop(0)
        if level < height:
            left = {"value": left_branch(node['value']), "left": None, "right": None}
            right = {"value": right_branch(node['value']), "left": None, "right": None}
            node['left'] = left
            node['right'] = right
            queue.append((level + 1, left))
            queue.append((level + 1, right))
    return tree

class TestMath(unittest.TestCase):

    def test_task(self):
        self.assertEqual(gen_bin_tree(), ({'value': 17, 'left': {'value': 169, 'left': {'value': 27225, 'left': {'value': 740982841, 'left': None, 'right': None}, 'right': {'value': 54456, 'left': None, 'right': None}}, 'right': {'value': 344, 'left': {'value': 115600, 'left': None, 'right': None}, 'right': {'value': 694, 'left': None, 'right': None}}}, 'right': {'value': 40, 'left': {'value': 1296, 'left': {'value': 1669264, 'left': None, 'right': None}, 'right': {'value': 2598, 'left': None, 'right': None}}, 'right': {'value': 86, 'left': {'value': 6724, 'left': None, 'right': None}, 'right': {'value': 178, 'left': None, 'right': None}}}}))

    def test_root(self):
        self.assertEqual(gen_bin_tree(height=1), ({'value': 17, 'left': None, 'right': None}))

    def test_another_root(self):
        self.assertEqual(gen_bin_tree(root=1), ({'value': 1, 'left': {'value': 9, 'left': {'value': 25, 'left': {'value': 441, 'left': None, 'right': None}, 'right': {'value': 56, 'left': None, 'right': None}}, 'right': {'value': 24, 'left': {'value': 400, 'left': None, 'right': None}, 'right': {'value': 54, 'left': None, 'right': None}}}, 'right': {'value': 8, 'left': {'value': 16, 'left': {'value': 144, 'left': None, 'right': None}, 'right': {'value': 38, 'left': None, 'right': None}}, 'right': {'value': 22, 'left': {'value': 324, 'left': None, 'right': None}, 'right': {'value': 50, 'left': None, 'right': None}}}}))

        

unittest.main(argv=[''], verbosity=2, exit=False)      
