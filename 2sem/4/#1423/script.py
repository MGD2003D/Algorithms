@profile
def main():
    with open("resources/input.txt", "r") as file:
        n = int(file.readline().strip())
        s = file.readline().strip()
        t = file.readline().strip()

    double_s = s + s
    position = double_s.find(t)

    with open("resources/output.txt", "w") as file:
        if position == -1 or position >= n:
            file.write("-1\n")
        else:
            x = n - position
            file.write(str(x) + "\n")

main()
