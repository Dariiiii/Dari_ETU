class Symbol_dinH:
    def __init__(self, char="", left=None, right=None, parent=None):
        self.char = char
        self.count = 0
        self.left = left
        self.right = right
        self.parent = parent

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


class Din_tree:
    def __init__(self):
        self.arr = [Symbol_dinH()]

    def insert(self, element):
        element = Symbol_dinH(element)
        null_el = self.arr.pop()
        node = Symbol_dinH("", element, null_el)
        if null_el.parent:
            null_el.parent.left = node
            node.parent = null_el.parent
        element.parent, null_el.parent = node, node
        node.right, node.left = element, null_el
        self.arr.extend([node, element, null_el])
        self.rebuild(element)

    def add_count(self, element):
        for i in self.arr:
            if i.char == element:
                element = i
                break
        self.rebuild(element)

    def rebuild(self, element):
        cur = element
        while True:
            if not cur:
                break
            parents, childs = [self.arr[0]], []
            end = False
            while not end:
                for symbol_dh in parents:
                    if symbol_dh.left:
                        childs.append(symbol_dh.left)
                    if symbol_dh.right:
                        childs.append(symbol_dh.right)
                    if symbol_dh == cur:
                        end = True
                        break
                    if symbol_dh.count == cur.count:
                        if cur.char and not symbol_dh.char:
                            continue
                        if symbol_dh.parent and symbol_dh.parent.right == symbol_dh:
                            symbol_dh.parent.right = cur
                        elif symbol_dh.parent:
                            symbol_dh.parent.left = cur
                        if cur.parent.right == cur:
                            cur.parent.right = symbol_dh
                        else:
                            cur.parent.left = symbol_dh
                        cur.parent, symbol_dh.parent = symbol_dh.parent, cur.parent
                        end = True
                        break
                parents = childs
                childs = []
            cur.count += 1
            cur = cur.parent


    def encode_dinH(self, dictionary, top=None, code=''):
        if top:
            cur = top
        else:
            cur = self.arr[0]
        right, left = cur.right, cur.left
        if right and right.count != 0:
            self.encode_dinH(dictionary, right, code + '0')
        if left and left.count != 0:
            self.encode_dinH(dictionary, left, code + '1')
        if cur.char != '':
            if cur.parent.left and not cur.parent.left.count:
                dictionary[cur.char] = code[:-1]
            else:
                dictionary[cur.char] = code
