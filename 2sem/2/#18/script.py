class Rope:
    def __init__(self, string):
        self.string = string

    def process_query(self, i, j, k):
        substring = self.string[i:j+1]
        remaining_string = self.string[:i] + self.string[j+1:]
        if k == 0:
            self.string = substring + remaining_string
        else:
            self.string = remaining_string[:k] + substring + remaining_string[k:]

@profile
def process_input_output(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.readlines()
    s = content[0].strip()
    n = int(content[1].strip())
    rope = Rope(s)
    for i in range(2, 2 + n):
        i, j, k = map(int, content[i].strip().split())
        rope.process_query(i, j, k)
    with open(output_file, 'w') as f:
        f.write(rope.string)

process_input_output('resources/input.txt', 'resources/output.txt')