import Heap

class Symbol_stH:
    def __init__(self, char, count, left=None, right=None):
        self.char = char
        self.count = count
        self.left, self.right = left, right

    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        else:
            return self.char < other.char

    def __gt__(self, other):
        if self.count != other.count:
            return self.count > other.count
        else:
            return self.char > other.char


def count_Symbols(string):
    symbols_set = list(set(string))
    occ_in_str = [0] * len(symbols_set)
    for char in string:
        occ_in_str[symbols_set.index(char)] += 1
    symbols_s_c = []
    for char in range(len(symbols_set)):
        symbols_s_c.append(Symbol_stH(symbols_set[char], occ_in_str[char]))
    return symbols_s_c


def st_Huffman_Tree(symbols_s_c):
    heap = Heap.Heap(symbols_s_c)
    while heap.size() > 1:
        left = heap.extract_min()
        right = heap.extract_min()
        sum_count_lr = left.count + right.count
        heap.insert(Symbol_stH('', sum_count_lr, left, right))
    return heap.extract_min()


def encode_stH(hf_tree, dictionary, code=''):
    cur = hf_tree
    right, left = cur.right, cur.left
    if right != None:
        encode_stH(right, dictionary, code + '1')
    if left != None:
        encode_stH(left, dictionary, code + '0')
    if cur.char != '':
        dictionary[cur.char] = code


def encode_stH_str(string, dictionary):
    hf_tree = st_Huffman_Tree(count_Symbols(string))
    encode_stH(hf_tree, dictionary)
    code_str = ''
    for char in string:
        code_str += dictionary[char]
    return code_str


if (__name__ == "__main__"):
    string = input()
    if len(count_Symbols(string)) <= 1:
        print(string[0] + ':', '0')
        print('0' * len(string), len(string))
    else:
        codes = dict()
        output = encode_stH_str(string, codes)
        for ch in codes.keys():
            print(f'{ch}: {codes[ch]}')
        print(output, len(output))
