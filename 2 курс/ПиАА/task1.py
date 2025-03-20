class Vertex:
    '''
    Класс для хранения информации о вершине, входящей в бор
    parent - вершина-родитель текущей вершины
    symbol - символ, по которому был совершен переход из вершины-родителя в текущую
    transition - словарь, который содержит всевозможные пути из текущей вершины (ключ - символ, по которому совершается
    переход, значение - вершина, в которую переход был совершен)
    flag - маркер, того, что вершина является конечной для какого-либо образца
    suffix_link - суффиксная ссылка для данной вершины
    pattern_number - номер паттерна (записывается для вершин с фалагом True)
    '''
    def __init__(self, parent, symbol):
        self.parent = parent
        self.symbol = symbol
        self.transition = {}
        self.flag = False
        self.suffix_link = None
        self.pattern_number = None


class Trie:
    '''
    Класс для обработки и хранения бора
    trie - бор, список записи добавленных вершин
    patterns - образцы, которые необхоимо найти в тексте
    text - текст, в котором ведется множественный поиск образцов
    '''
    def __init__(self):
        self.trie = [Vertex(None, None)]
        self.patterns = []
        self.text = ''

    '''
    Метод для ввода данных о тексте и образцах
    '''
    def read_data(self):
        self.text = input()
        for i in range(int(input())):
            self.patterns.append(input())

    '''
    Метод для построения бора
    '''
    def make_trie(self):
        self.read_data()
        for pattern in self.patterns:
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
            vertex.pattern_number = self.patterns.index(pattern)

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
    Метод для корректного вывода результата
    '''
    def print_result(self, result):
        result.sort()
        for line in result:
            print(line[0], line[1])

    '''
    Метод, в котором реализуется алгоритм Ахо-Корасик. Сложность алгоритма описана в отчете.
    '''
    def algorithm_aho_corasick(self, vertex, result, index_in_text):
        if vertex.transition.get(self.text[index_in_text]) is not None:
            vertex = vertex.transition.get(self.text[index_in_text])
            if vertex.flag:
                result.append(
                    (index_in_text - len(self.patterns[vertex.pattern_number]) + 2, vertex.pattern_number + 1))
        elif vertex != self.trie[0]:
            vertex = self.get_suffix_link(vertex)
            return self.algorithm_aho_corasick(vertex, result, index_in_text)
        suffix_link = self.get_suffix_link(vertex)
        while suffix_link != self.trie[0]:
            if suffix_link.flag:
                result.append((index_in_text - len(self.patterns[suffix_link.pattern_number]) + 2,
                               suffix_link.pattern_number + 1))
            suffix_link = self.get_suffix_link(suffix_link)
        return vertex

    '''
    Метод для поиска образцов в тексте, с помощью алгоритма Ахо-Корасик
    '''
    def find_patterns(self):
        self.make_trie()
        result = []
        vertex = self.trie[0]
        for i in range(len(self.text)):
            vertex = self.algorithm_aho_corasick(vertex, result, i)
        self.print_result(result)


trie = Trie()
trie.find_patterns()
