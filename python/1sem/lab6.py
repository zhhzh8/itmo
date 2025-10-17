import timeit
import matplotlib.pyplot as plt

numeros = list(range(1, 15))

def benchmark(fn, n, number, repeat):
    """Возвращает среднее время выполнения func(n)"""
    print(n)
    times = timeit.repeat(lambda: fn(n), number=number, repeat=repeat)
    return min(times)

# По фамилии был выбран 17 вар

def build_tree_recursive(height: int = 4, root: int = 17, left_branch = lambda x: (x - 4) ** 2, right_branch=lambda x: (x + 3) * 2) -> dict:
    """
    Рекурсивно строит бинарное дерево заданной высоты с указанным корнем(Стандартно: height = 4, root = 17).
    Левый потомок(left_branch) вычисляется по заданной формуле(Стандартно: (root - 4) ** 2)
    Правый потомок(right_branch) вычисляется по заданной формуле(Стандарнто: (root + 3) * 2)
    """

    if height <= 1:
        return {"value": root, "left": None, "right": None}

    left_value = left_branch(root)
    right_value = right_branch(root)

    left_subtree = build_tree_recursive(height - 1, left_value)
    right_subtree = build_tree_recursive(height - 1, right_value)

    return {
        "value": root,
        "left": left_subtree,
        "right": right_subtree
    }

def build_tree_iterative(height: int = 4, root: int = 17, left_branch = lambda x: (x - 4) ** 2, right_branch=lambda x: (x + 3) * 2) -> dict:
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

res_recursive = []
res_iterative = []

for n in numeros:
      res_recursive.append(benchmark(build_tree_recursive, n, repeat=5, number=1000))
      res_iterative.append(benchmark(build_tree_iterative, n, repeat=5, number=1000))

# Визуализация
plt.plot(numeros, res_recursive, label="Рекурсивный")
plt.plot(numeros, res_iterative, label="Итеративный")
plt.xlabel("Высота")
plt.ylabel("Время (сек)")
plt.title("Сравнение рекурсивного и итеративного метода генерации бинарного дерева")
plt.grid(True)
plt.legend()
plt.show()

print('end')