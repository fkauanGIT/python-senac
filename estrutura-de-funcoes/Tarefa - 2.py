def print_pattern(number):
    for i in range(1, number + 1):
        line = ''
        for j in range(1, i + 1):
            line += str(j) + ' '
        print(line.strip())


n = int(input("Digite um número: "))
print_pattern(n)
