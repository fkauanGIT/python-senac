vetor1 = []
vetor2 = []

for i in range(10):
    vetor1.append(int(input("Digite os 10 primeiros números: ")))
for i in range(10):
    vetor2.append(int(input("Digite os 10 segundos números: ")))

vetor1.sort()
vetor2.sort()

vetor3 = []

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(vetor3)