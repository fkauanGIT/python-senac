vetor = []

for i in range(10):
    vetor.append(int(input("Digite um número inteiro: ")))

vetor.sort()
decrescente = list(reversed(vetor))

print(decrescente)
print("Seus números:", len(vetor))