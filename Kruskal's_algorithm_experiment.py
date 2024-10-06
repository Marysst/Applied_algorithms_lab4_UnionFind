import random
import time
import matplotlib.pyplot as plt

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

# Алгоритм Крускала з модифікацією для експеременту
# Винесино сортування ребер за функцію, як передобчислення перед запуском експеременту
def kruskal_modification_for_the_experiment(n, edges):
    """
    n: Список вершин у форматі (значення вершини1, значення вершини2, ...)
    edges: Список ребер у форматі (вага, вершина1, вершина2)
    """
    # Сортуємо ребра за зростанням ваги
    # Не порбно, проводиться як передобчислення, перед запуском експеременту

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

# Функція для проведення експерименту
def run_experiment():
    results = []  # Список для збереження результатів

    # Виконуємо експерименти для різної кількості вершин
    for n in range(100, 901, 200):  # Від 100 до 900 з кроком 200
        vertices = list(range(n))  # Список вершин (0, 1, 2, ..., n-1)
        total_time = 0  # Загальний час для усереднення

        # Виконуємо 1000 експериментів для кожної кількості вершин
        for _ in range(1000):
            edges = []  # Список для збереження ребер
            edge_set = set()  # Використовуємо множину для уникнення повторних ребер

            # Генерація випадкових ребер
            for _ in range(n * (n - 1) // 2):  # Максимум ребер для повного графа
                u = random.choice(vertices)  # Випадкова вершина
                v = random.choice(vertices)  # Випадкова вершина

                if u != v:  # Уникаємо самопідключень
                    edge = (min(u, v), max(u, v))  # Упорядковуємо вершини в ребрі
                    if edge not in edge_set:  # Перевіряємо, чи вже існує це ребро
                        weight = random.randint(1, 10)  # Випадкова вага для ребра
                        edges.append((weight, u, v))  # Додаємо ребро до списку
                        edge_set.add(edge)  # Додаємо ребро до множини

            # Перед обчислення (прибрано з алгоритму Крускала, аби не включати в оцінку)
            # Сортуємо ребра за зростанням ваги
            edges.sort(key=lambda edge: edge[0])

            # Вимірювання часу виконання алгоритму Крускала
            start_time = time.time()  # Записуємо початковий час
            kruskal_modification_for_the_experiment(vertices, edges)  # Запускаємо алгоритм Крускала
            end_time = time.time()  # Записуємо кінцевий час

            elapsed_time = end_time - start_time  # Розрахунок часу виконання
            total_time += elapsed_time  # Додаємо час цього експерименту до загального часу

        # Обчислюємо середній час для 1000 експериментів
        avg_time = total_time / 1000
        results.append((n, avg_time))  # Зберігаємо кількість вершин та середній час

    return results  # Повертаємо результати експерименту


# Запуск експерименту
experiment_results = run_experiment()

# Візуалізація результатів
n_values = [result[0] for result in experiment_results]  # Кількість вершин
time_values = [result[1] for result in experiment_results]  # Час виконання

# Створюємо графік
plt.plot(n_values, time_values, marker='o')
plt.xlabel('Кількість вершин (n)')  # Підпис для осі X
plt.ylabel('Середній час виконання (seconds)')  # Підпис для осі Y
plt.title('Середній час виконання алгоритму Крускала')  # Заголовок графіка
plt.grid()  # Додаємо сітку
plt.show()  # Відображаємо графік
