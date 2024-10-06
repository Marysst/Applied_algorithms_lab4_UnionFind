# Реалізація структури даних UnionFind на основі якої реалізовано алгоритм Крускала
class UnionFind:
    def __init__(self):
        # Ініціалізуємо порожні словники для батьків та розмірів
        self.parent = {}
        self.size = {}

    def make_set(self, x):
        # Створюємо дерево з одного елементу
            self.parent[x] = x  # Кожен елемент стає сам собі батьком
            self.size[x] = 1    # Початковий розмір дерева — 1

    def find(self, x):
        # Знаходимо корінь дерева з оптимізацією шляху
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Компресія шляху
        return self.parent[x]

    def union(self, x, y):
        # Об'єднуємо дві множини за розміром
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Об'єднуємо менше дерево з більшим
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
            elif self.size[root_x] > self.size[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.size[root_y] += 1  # Збільшуємо розмір на 1

# Алгоритм Крускала
def kruskal(n, edges):
    """
    n: Список вершин у форматі (значення вершини1, значення вершини2, ...)
    edges: Список ребер у форматі (вага, вершина1, вершина2)
    """
    # Сортуємо ребра за зростанням ваги
    edges.sort(key=lambda edge: edge[0])

    # Ініціалізуємо UnionFind
    uf = UnionFind()

    # Створюємо множини для кожної вершини
    for i in n:
        uf.make_set(i)

    mst = []  # Для збереження ребер мінімального кістякового дерева
    mst_weight = 0  # Загальна вага MST

    for weight, u, v in edges:
        # Якщо вершини не в одному компоненті, додаємо ребро до MST
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((weight, u, v))
            mst_weight += weight

    return mst, mst_weight
