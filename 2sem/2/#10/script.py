def check_bst(node, min_val, max_val, tree):
    if node == 0:
        return True
    key, left, right = tree[node]
    if not (min_val < key < max_val):
        return False
    return check_bst(left, min_val, key, tree) and check_bst(right, key, max_val, tree)

def read_tree(input_file):
    with open(input_file, 'r') as file:
        n = int(file.readline())
        if n == 0:
            return []
        tree = [None]
        for _ in range(n):
            key, left, right = map(int, file.readline().split())
            tree.append((key, left, right))
    return tree

@profile
def write_result(output_file, result):
    with open(output_file, 'w') as file:
        file.write(result)


tree = read_tree("resources/input.txt")
if tree:
    is_bst = check_bst(1, float('-inf'), float('inf'), tree)
else:
    is_bst = True
write_result("resources/output.txt", "YES" if is_bst else "NO")