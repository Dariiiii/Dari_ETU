import sys
import math


class Graph:
    # поле класса - словарь, в котором ключом является какая-то вершина-родитель графа,
    # а в качестве значения выступает массив, состоящих из кортежей (пара: вершина-ребенок и вес ребра)
    def __init__(self):
        self.info = {}

    # метод для добавления новых элементов в граф
    def insert(self, parent, child, len_way):
        if not (parent in self.info.keys()):
            self.info[parent] = [(child, len_way)]
        else:
            self.info[parent].append((child, len_way))
        if not (child in self.info.keys()):
            self.info[child] = []


graph = Graph()  # объект класса Graph
start, end = input().split()  # начальная и конечная вершины пути


# функция считывания графа из стандартного потока ввода
def input_graph():
    graph.info[start] = []
    graph.info[end] = []
    for line in sys.stdin:
        try:
            parent, child, len_way = line.split()
        except:
            break
        graph.insert(parent, child, int(float(len_way)))


input_graph()


# функция эвристической оценки
def heuristic_evaluation(cur):
    return abs(ord(end) - ord(cur))


queue = []


# функция для поиска вершины из массива нужных вершин с наименьшим значением функции func
def find_min_func(func, Q):
    min_f = math.inf
    for edges in Q:
        if func[edges][0] <= min_f:
            min_f = func[edges][0]
            min_edge = edges
    return min_edge


# функция поиска кратчайшего пути в графе
def alg_A_star():
    global start, end
    queue.append(start)
    func = {start: (0, start)}
    min_path = {start: 0}
    while len(queue) != 0:
        cur = find_min_func(func, queue)
        if cur == end:
            print(func[end][1])
            return True
        queue.remove(cur)
        for node in graph.info[cur]:
            tmp = min_path[cur] + node[1]
            if node[0] not in min_path.keys() or tmp < min_path[node[0]]:
                min_path[node[0]] = tmp
                func[node[0]] = (min_path[node[0]] + heuristic_evaluation(node[0]), func[cur][1] + node[0])
                if node[0] not in queue:
                    queue.append(node[0])
    return False


alg_A_star()
