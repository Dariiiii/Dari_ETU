class Heap:

    def __init__(self, heap):
        self.heap = []
        for elem in heap:
            self.insert(elem)

    @staticmethod
    def get_parent(index):
        return (index - 1) // 2

    @staticmethod
    def get_left_child(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child(index):
        return 2 * index + 2

    def size(self):
        return len(self.heap)

    def insert(self, element):
        self.heap.append(element)
        self.sift_up(len(self.heap)-1)

    def extract_min(self):
        min_element = self.heap[0]
        self.heap[0]= self.heap[-1]
        del self.heap[-1]
        self.sift_down(0)
        return min_element

    def sift_up(self, index):
        if index < 0 or index >= len(self.heap):
            return
        parent = self.get_parent(index)
        while index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = self.get_parent(index)

    def sift_down(self, index):
        if index < 0 or index >= len(self.heap):
            return
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        if left >= self.size() and right >= self.size():
            return
        if right >= self.size():
            min_index = left if self.heap[left] < self.heap[index] else index
        else:
            min_index = left if self.heap[left] < self.heap[right] else right
            min_index = min_index if self.heap[min_index] < self.heap[index] else index
        if min_index != index:
            self.heap[min_index], self.heap[index] = self.heap[index], self.heap[min_index]
            self.sift_down(min_index)