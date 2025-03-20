import sys


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
result = ''  # строка для записи минимального пути


# рекурсивная функция поиска кратайшего пути в графе
def greedy_alg(cur):
    global result
    result += str(cur)
    if cur == end:
        print(result)
        return True
    min_id = 0
    if len(graph.info[cur]) != 0:
        min_len = graph.info[cur][0][1]
        for i in range(len(graph.info[cur])):
            if graph.info[cur][i][1] < min_len:
                min_len = graph.info[cur][i][1]
                min_id = i
        cur = graph.info[cur].pop(min_id)[0]
        greedy_alg(cur)
    else:
        graph.info.pop(cur)
        cur = result[-2]
        result = result[:-2]
        greedy_alg(cur)
    return False


greedy_alg(start)
