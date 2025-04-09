def area(raio):
    area = (raio * raio) * 3.14
    return area


raio = float(input("Escreva o número: "))
result = area(raio)
print("A área do círculo é: ", result)

