from collections import Counter

def create_palindrome(s):
    count = Counter(s)
    middle = ''
    halves = []
    for char, freq in sorted(count.items()):
        if freq % 2 == 1 and middle == '':
            middle = char
        halves.extend(char * (freq // 2))
    first_half = ''.join(sorted(halves))
    palindrome = first_half + middle + first_half[::-1]
    return palindrome

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    letters = file.readline().strip()

palindrome = create_palindrome(letters)

with open('output.txt', 'w') as file:
    file.write(palindrome)
