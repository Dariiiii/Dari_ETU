import math
import time


class TSP:
    '''
    Коструктор класса
    matrix_graph - граф, введенный из файла
    key_addition - массив дополнений для множества ключей, состоит из чисел от 2 до count (тип значений - tuple)
    min_path_table - словарь, для хранения минимальных путей для текущего шага, где ключ это множество, из которого
    ведется поиск минимального пути к вершинам, значение - массив кортежей длины 3 (вершина
    в которую идем, минимальный путь к этой вершине, длина этого пути)
    previous_min_path_table - словарь, для хранения таблицы для пердыдущего шага
    set_of_values - множество ключей графа, для текущего шага
    count - количество строк/столбцов графа
    '''
    def __init__(self):
        self.matrix_graph = []
        self.key_addition = []
        self.min_path_table = dict()
        self.previous_min_path_table = dict()
        self.set_of_values = []
        self.count = 0

    '''
    Метод для ввода графика из файла, также в ней задаются начальные парметры для 
    min_way_table, set_of_values, key_addition
    '''
    def input_graph(self, file_name):
        file = open(file_name)
        for line in file:
            line_matrix = []
            for i in line.split():
                if i == '-1' or i == 'inf' or i == '-' or int(i) >= 100000:
                    line_matrix.append(math.inf)
                else:
                    line_matrix.append(int(i))
            print(line_matrix)
            self.matrix_graph.append(line_matrix)
        file.close()
        self.count = len(self.matrix_graph[0])
        for i in range(2, self.count + 1):
            self.min_path_table[tuple([i])] = []
            for j in range(2, self.count + 1):
                if i != j:
                    self.min_path_table[tuple([i])].append(
                        (j, [1, i], self.matrix_graph[0][i - 1] + self.matrix_graph[i - 1][j - 1]))
            self.set_of_values.append(tuple([i]))
        self.key_addition = self.set_of_values.copy()

    '''
    Метод для поиска минимального пути из подмножества к вершинам 
    '''
    def min_set(self, set):
        subsets = []
        complementary_vertex = []
        final_vertex = []
        min_path_set = []
        set = list(set)
        for i in range(2, self.count + 1):
            if i in set:
                complementary_vertex.append(i)
                new_set = set.copy()
                new_set.remove(i)
                subsets.append(tuple(new_set))
            else:
                final_vertex.append(i)
        if not final_vertex:
            final_vertex.append(1)
        for v in final_vertex:
            path_length = []
            path = []
            for i in range(len(subsets)):
                for j in self.previous_min_path_table[subsets[i]]:
                    if j[0] == complementary_vertex[i]:
                        path_length.append(j[2] + self.matrix_graph[complementary_vertex[i] - 1][v - 1])
                        path.append(j)
            best_id = path_length.index(min(path_length))
            min_way = path[best_id][1].copy()
            min_way.append(path[best_id][0])
            min_path_set.append((v, min_way, min(path_length)))
        return min_path_set

    '''
    Метод для поиска минимального гамильтонова цикла
    '''
    def find_min_hamiltonian_path(self):
        if self.count == 1:
            print("[1, 1]", self.matrix_graph[0][0])
            return 0
        start = time.time()
        for step in range(2, self.count):
            previous_set_of_values = self.set_of_values.copy()
            self.previous_min_path_table = self.min_path_table.copy()
            self.min_path_table.clear()
            self.set_of_values.clear()
            for prev_set in previous_set_of_values:
                for key_addition in self.key_addition:
                    current_set = set(prev_set + key_addition)
                    current_set = list(current_set)
                    current_set.sort()
                    current_set = tuple(current_set)
                    if len(current_set) == step:
                        self.set_of_values.append(current_set)
            self.set_of_values = set(self.set_of_values)
            self.set_of_values = list(self.set_of_values)
            for i in self.set_of_values:
                self.min_path_table[i] = self.min_set(i)
        end = time.time() - start
        if self.min_path_table[self.set_of_values[0]][0][2] == math.inf:
            print("No way", end)
        else:
            self.min_path_table[self.set_of_values[0]][0][1].append(1)
            print(self.min_path_table[self.set_of_values[0]][0][1], self.min_path_table[self.set_of_values[0]][0][2],
                  end)


ts = TSP()
ts.input_graph('test4.txt')
ts.find_min_hamiltonian_path()
