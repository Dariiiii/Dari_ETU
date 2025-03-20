from din_tree import Din_tree


def encode_dinH_str(string, codes):
    tree = Din_tree()
    tree.insert(string[0])
    for i in range(1,len(string)):
        if string[i] in string[:i]:
            tree.add_count(string[i])
        else:
            tree.insert(string[i])
    tree.encode_dinH(codes)
    code = ''
    for char in string:
        code += codes[char]
    return code


if (__name__ == "__main__"):
    string = input()
    codes = dict()
    output = encode_dinH_str(string, codes)
    for ch in codes.keys():
        print(f'{ch}: {codes[ch]}')
    print(output, len(output))