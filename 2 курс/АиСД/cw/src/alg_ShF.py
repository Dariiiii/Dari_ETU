class Symbol_SF:
    def __init__(self, char, count):
        self.char = char
        self.count = count

    def __lt__(self, other):
        if isinstance(other, Symbol_SF):
            if self.count != other.count:
                return self.count > other.count


def count_Symbols(string):
    symbols_set = list(set(string))
    occ_in_str = [0] * len(symbols_set)
    for char in string:
        occ_in_str[symbols_set.index(char)] += 1
    symbols_s_c = []
    for char in range(len(symbols_set)):
        symbols_s_c.append(Symbol_SF(symbols_set[char], occ_in_str[char]))
    symbols_s_c = sorted(symbols_s_c)
    return symbols_s_c


def encode_ShF(symbols_s_c, sum, dictionary, code=''):
    if len(symbols_s_c) == 1:
        dictionary[symbols_s_c[0].char] = code
        return 0
    if len(symbols_s_c) == 2:
        dictionary[symbols_s_c[0].char] = code + '1'
        dictionary[symbols_s_c[1].char] = code + '0'
        return 0
    left_id, right_id = 0, len(symbols_s_c)
    left_Sum, right_Sum = 0, 0
    left, right = [], []
    while left_Sum < sum // 2:
        left.append(symbols_s_c[left_id])
        left_Sum += symbols_s_c[left_id].count
        left_id += 1
    for i in range(left_id, right_id):
        right.append(symbols_s_c[i])
        right_Sum += symbols_s_c[i].count
    encode_ShF(left, left_Sum, dictionary, code + '0')
    encode_ShF(right, right_Sum, dictionary, code + '1')



def encode_ShF_str(string, dictionary):
    symbols_s_c = count_Symbols(string)
    encode_ShF(symbols_s_c, len(string), dictionary)
    code_str = ''
    for char in string:
        code_str += dictionary[char]
    return code_str


if (__name__ == "__main__"):
    string = input()
    codes = dict()
    if len(count_Symbols(string)) <= 1:
        print(string[0] + ':', '0')
        print('0' * len(string), len(string))
    else:
        output = encode_ShF_str(string, codes)
        for char in codes.keys():
            print(f'{char}: {codes[char]}')
        print(output, len(output))
