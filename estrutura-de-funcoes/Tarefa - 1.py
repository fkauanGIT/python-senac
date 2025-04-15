def print_pattern(number):
    for i in range(1, number + 1):
        line = (str(i) + ' ') * i
        print(line.strip())


n = int(input("Enter a number: "))
print_pattern(n)
