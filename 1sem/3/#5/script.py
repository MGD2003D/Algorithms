def calculate_h_index(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index

@profile
def main():
    with open('resources/input.txt', 'r') as file:
        content = file.read()
        citations = list(map(int, content.replace(',', ' ').split()))

    h_index = calculate_h_index(citations)

    with open('resources/output.txt', 'w') as file:
        file.write(str(h_index))

main()


