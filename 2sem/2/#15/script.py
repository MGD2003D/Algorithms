class Node:
    def __init__(self, id, key, left=None, right=None):
        self.id = id
        self.key = key
        self.left = left if left is not None else Leaf()
        self.right = right if right is not None else Leaf()

    @property
    def height(self):
        return 1 + max(self.left.height, self.right.height)

    @property
    def balance(self):
        return self.right.height - self.left.height

    @property
    def size(self):
        return 1 + self.left.size + self.right.size

    @profile
    def delete(self, key):
        if key < self.key:
            self.left = self.left.delete(key)
        elif key > self.key:
            self.right = self.right.delete(key)
        else:
            if isinstance(self.left, Leaf):
                return self.right
            rightmost = self.left.rightmost_child()
            self.key = rightmost.key
            self.left = self.left.delete(rightmost.key)
        return self.rebalance()

    def rebalance(self):
        if self.balance == 2:
            if self.right.balance < 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()
        elif self.balance == -2:
            if self.left.balance > 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()
        return self

    def rotate_left(self):
        right = self.right
        self.right = right.left
        right.left = self
        return right

    def rotate_right(self):
        left = self.left
        self.left = left.right
        left.right = self
        return left

    def rightmost_child(self):
        if isinstance(self.right, Leaf):
            return self
        return self.right.rightmost_child()


class Leaf:
    def __init__(self):
        self.id = 0
        self.height = -1
        self.size = 0

    def delete(self, key):
        return self

    def rebalance(self):
        return self


def make_tree(nodes, i):
    if i >= 0:
        k, l, r = nodes[i]
        return Node(i + 1, k, make_tree(nodes, l), make_tree(nodes, r))
    return Leaf()


def read_tree(input_lines):
    n = int(input_lines[0])
    nodes = [(int(k), int(l) - 1, int(r) - 1) for k, l, r in (line.split() for line in input_lines[1:n+1])]
    return make_tree(nodes, 0), int(input_lines[-1])


def print_tree(tree, out, indices=None, index=1):
    if indices is None:
        indices = {0: 0}

    nodes_list = []

    def traverse_and_collect(tree, index):
        if isinstance(tree, Node):
            indices[tree.id] = index
            index += 1
            index = traverse_and_collect(tree.left, index)
            index = traverse_and_collect(tree.right, index)
            nodes_list.append((tree.id, f"{tree.key} {indices[tree.left.id]} {indices[tree.right.id]}"))
            return index
        return index

    traverse_and_collect(tree, 1)
    nodes_list.sort(key=lambda x: x[0])
    out.append(str(len(nodes_list)))
    for _, node_str in nodes_list:
        out.append(node_str)

def read_tree_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    n = int(lines[0])
    nodes = [(int(k), int(l) - 1, int(r) - 1) for k, l, r in (line.split() for line in lines[1:n+1])]
    return make_tree(nodes, 0), int(lines[-1].strip())

def save_tree_to_file(tree, filename):
    output_lines = []
    print_tree(tree, output_lines)
    with open(filename, 'w') as file:
        file.write('\n'.join(output_lines) + '\n')

tree, x = read_tree_from_file('resources/input.txt')

updated_tree = tree.delete(x)
save_tree_to_file(updated_tree, 'resources/output.txt')

