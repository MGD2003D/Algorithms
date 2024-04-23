@profile
def encode_string(s):
    n = len(s)
    if n == 0:
        return ""

    result = []
    i = 0
    while i < n:
        max_len = 0
        best_repeat = 1
        best_substr = s[i]
        for length in range(1, n - i + 1):
            substring = s[i:i + length]
            repeat = 1
            while i + repeat * length <= n and substring == s[i + repeat * length: i + (repeat + 1) * length]:
                repeat += 1
            if repeat > 1 and (length * (repeat - 1) > max_len):
                max_len = length * (repeat - 1)
                best_repeat = repeat
                best_substr = substring

        if best_repeat > 1:
            if len(result) > 0:
                result.append("+")
            result.append(best_substr)
            if best_repeat > 1:
                result.append("*")
                result.append(str(best_repeat))
            i += len(best_substr) * best_repeat
        else:
            if len(result) > 0:
                result.append("+")
            result.append(s[i])
            i += 1

    encoded_string = ''.join(result)
    return encoded_string if len(encoded_string) < len(s) else s

@profile
def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        input_string = file.read().strip()

    output_string = encode_string(input_string)

    with open(output_filename, 'w') as file:
        file.write(output_string)


process_file('resources/input.txt', 'resources/output.txt')