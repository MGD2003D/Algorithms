@profile
def main(input_path, output_path):
    with open(input_path, "r") as input_file:
        a, b = map(int, input_file.readline().split())

    result = a + b

    with open(output_path, "w") as output_file:
        output_file.write(str(result))


input_path = "resources/input.txt"
output_path = "resources/output.txt"

main(input_path, output_path)
