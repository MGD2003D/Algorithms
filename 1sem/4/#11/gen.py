n = 100000
m = 1000000000
a_i = 1000000

content = f"{n} {m}\n" + " ".join([str(a_i) for _ in range(n)])

with open("resources/input.txt", "w") as file:
    file.write(content)
