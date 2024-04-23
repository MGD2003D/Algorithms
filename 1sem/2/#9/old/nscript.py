n = 1024
with open("../resources/input.txt", "w") as f:
    f.write(f"{n}\n")
    for i in range(n):
        for j in range(1, n + 1):
            f.write(f"{i * n + j} ")
        f.write("\n")

    for i in range(n):
        for j in range(1, n + 1):
            f.write(f"{n * n + i * n + j} ")
        f.write("\n")

