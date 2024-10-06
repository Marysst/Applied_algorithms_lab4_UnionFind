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
