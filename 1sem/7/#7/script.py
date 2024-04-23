import re


def match_pattern(pattern, string):
    regex_pattern = '^' + pattern.replace('?', '.').replace('*', '.*') + '$'

    if re.match(regex_pattern, string):
        return "YES"
    else:
        return "NO"


def read_input(filename):
    with open(filename, 'r') as file:
        pattern = file.readline().strip()
        string = file.readline().strip()
    return pattern, string


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(result)

@profile
def main():
    pattern, string = read_input("resources/input.txt")
    result = match_pattern(pattern, string)
    write_output("resources/output.txt", result)


main()
