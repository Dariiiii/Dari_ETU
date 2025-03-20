class Vertex:
    '''
    Класс для хранения информации о вершине, входящей в бор
    parent - вершина-родитель текущей вершины
    symbol - символ, по которому был совершен переход из вершины-родителя в текущую
    transition - словарь, который содержит всевозможные пути из текущей вершины (ключ - символ, по которому совершается
    переход, значение - вершина, в которую переход был совершен)
    flag - маркер, того, что вершина является конечной для какого-либо образца
    suffix_link - суффиксная ссылка для данной вершины
    pattern_number - массив с номерами паттерна (записывается для вершин с фалагом True).
    '''
    def __init__(self, parent, symbol):
        self.parent = parent
        self.symbol = symbol
        self.transition = {}
        self.flag = False
        self.suffix_link = None
        self.pattern_number = []


class Trie:
    '''
    Класс для обработки и хранения бора
    trie - бор, список записи добавленных вершин
    patterns - образцы для поиска, на которые разбивается string_pattern по символу joker
    length_joker - массив, содержащий количество символов-джокеров в строке
    string_pattern - строка-образец с джокерами
    joker - символ-джокер для введенной строки
    text - текст, в котором ведется множественный поиск образцов
    result - массив, в котором находится результат выполнения алгоритма Ахо-Корасика
    '''
    def __init__(self):
        self.trie = [Vertex(None, None)]
        self.patterns = []
        self.length_joker = [0]
        self.string_pattern = ''
        self.joker = ''
        self.text = ''
        self.result = None

    '''
    Метод для ввода данных о тексте и образце с джокерами и для разбиения string_pattern по символу joker
    '''
    def read_data(self):
        self.text = input()
        self.string_pattern = input()
        self.joker = input()
        self.patterns = self.string_pattern.split(self.joker)
        for pattern in self.patterns:
            if pattern == '':
                self.length_joker[-1] += 1
            else:
                self.length_joker.append(1)
        self.length_joker[-1] -= 1
        self.patterns = list(filter(None, self.patterns))
        self.result = [[] for i in range(len(self.patterns))]

    '''
    Метод для построения бора
    '''
    def make_trie(self):
        self.read_data()
        for i in range(len(self.patterns)):
            pattern = self.patterns[i]
            vertex = self.trie[0]
            for symbol in pattern:
                if vertex.transition.get(symbol) is not None:
                    vertex = vertex.transition.get(symbol)
                else:
                    last_vertex = Vertex(vertex, symbol)
                    self.trie.append(last_vertex)
                    vertex.transition.setdefault(symbol, last_vertex)
                    vertex = last_vertex
            vertex.flag = True
            vertex.pattern_number.append(i)

    '''
    Метод для поиска суффиксной ссылки, если она не определена
    '''
    def find_suffix_link(self, parent, symbol):
        parent_link = self.get_suffix_link(parent)
        if parent_link == self.trie[0] and parent_link.transition.get(symbol) is None:
            return self.trie[0]
        else:
            if parent_link.transition.get(symbol) is not None:
                return parent_link.transition[symbol]
            return self.find_suffix_link(parent_link, symbol)

    '''
    Метод для получения суффиксной ссылки
    '''
    def get_suffix_link(self, vertex):
        if vertex.suffix_link is None:
            if vertex.parent == self.trie[0] or vertex == self.trie[0]:
                vertex.suffix_link = self.trie[0]
            else:
                vertex.suffix_link = self.find_suffix_link(vertex.parent, vertex.symbol)
        return vertex.suffix_link

    '''
    Метод, в котором реализуется алгоритм Ахо-Корасик. Сложность алгоритма описана в отчете.
    '''
    def algorithm_aho_corasick(self, vertex, index_in_text):
        if vertex.transition.get(self.text[index_in_text]) is not None:
            vertex = vertex.transition.get(self.text[index_in_text])
            if vertex.flag:
                for pattern_number in vertex.pattern_number:
                    self.result[pattern_number].append(
                        (pattern_number, index_in_text - len(self.patterns[pattern_number]) + 1))
        elif vertex != self.trie[0]:
            vertex = self.get_suffix_link(vertex)
            return self.algorithm_aho_corasick(vertex, index_in_text)
        suffix_link = self.get_suffix_link(vertex)
        while suffix_link != self.trie[0]:
            if suffix_link.flag:
                for pattern_number in suffix_link.pattern_number:
                    self.result[pattern_number].append(
                        (pattern_number, index_in_text - len(self.patterns[pattern_number]) + 1))
            suffix_link = self.get_suffix_link(suffix_link)
        return vertex

    '''
    Метод для поиска образцов в тексте, с помощью алгоритма Ахо-Корасик
    '''
    def find_patterns(self):
        self.make_trie()
        vertex = self.trie[0]
        for i in range(len(self.text)):
            vertex = self.algorithm_aho_corasick(vertex, i)
        self.find_string_pattern_with_joker()

    '''
    Метод для множественного поиска строки-образца с джокерами, использующий данные, полученные в алгоритме Ахо-Корасик
    '''
    def find_string_pattern_with_joker(self):
        final_result = []
        length_array = []
        for i in self.result:
            length_array.append(len(i))
        index_of_minimum_array = length_array.index(min(length_array))
        length_up_to_the_current_pattern = 0
        for i in range(index_of_minimum_array):
            length_up_to_the_current_pattern += self.length_joker[i] + len(self.patterns[i])
        length_up_to_the_current_pattern += self.length_joker[index_of_minimum_array]
        for current_index in self.result[index_of_minimum_array]:
            start_index = current_index[1] - length_up_to_the_current_pattern
            if start_index >= 0:
                if self.check_the_occurrence(start_index, 0):
                    final_result.append(start_index + 1)
        for i in final_result:
            print(i)

    '''
    Метод для проверки целостности и корректности вхождения строки-образца с джокерами
    '''
    def check_the_occurrence(self, index, current_number_pattern):
        if current_number_pattern != len(self.patterns):
            if (current_number_pattern, index + self.length_joker[current_number_pattern]) in self.result[current_number_pattern]:
                return self.check_the_occurrence(index + self.length_joker[current_number_pattern] +
                                                 len(self.patterns[current_number_pattern]), current_number_pattern + 1)
            else:
                return False
        elif index + self.length_joker[current_number_pattern] <= len(self.text):
            return True


trie = Trie()
trie.find_patterns()
