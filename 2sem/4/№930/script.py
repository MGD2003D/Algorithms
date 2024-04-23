@profile
def main():
    with open("resources/input.txt", "r") as file:
        parent1_name = file.readline().strip()
        parent2_name = file.readline().strip()

    index_map1 = {}
    index_map2 = {}

    for i in range(len(parent1_name)):
        if parent1_name[i] in index_map1:
            index_map1[parent1_name[i]].append(i)
        else:
            index_map1[parent1_name[i]] = [i]
    for i in range(len(parent2_name)):
        if parent2_name[i] in index_map2:
            index_map2[parent2_name[i]].append(i)
        else:
            index_map2[parent2_name[i]] = [i]

    last_index1 = -1
    last_index2 = -1
    result_name = ''

    for char_code in range(122, 96, -1):
        char = chr(char_code)
        if char not in index_map1 or char not in index_map2:
            continue

        pos1, pos2 = -1, -1
        for j in range(len(index_map1[char])):
            if index_map1[char][j] > last_index1:
                pos1 = j
                break
        for j in range(len(index_map2[char])):
            if index_map2[char][j] > last_index2:
                pos2 = j
                break
        if pos1 != -1 and pos2 != -1:
            max_usable = min(len(index_map1[char]) - pos1, len(index_map2[char]) - pos2)
            last_index1 = index_map1[char][pos1 + max_usable - 1]
            last_index2 = index_map2[char][pos2 + max_usable - 1]
            result_name += max_usable * char

    with open("resources/output.txt", "w") as file:
        file.write(result_name)


main()