class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.altura += 0.05

    def engordar(self, quantidade):
        self.peso += quantidade

    def emagrecer(self, quantidade):
        self.peso -= quantidade

    def crescer(self, quantidade):
        self.altura += quantidade

    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Altura: {self.altura:.2f} m")
        print(f"Peso: {self.peso:.2f} kg")


p1 = Pessoa("João", 18, 1.75, 70)

while True:
    print("Escolha uma ação:")
    print("1 - Envelhecer")
    print("2 - Engordar")
    print("3 - Emagrecer")
    print("4 - Crescer")
    print("5 - Mostrar informações")
    print("0 - Sair")

    opcao = input("Digite o número da ação: ")

    if opcao == "1":
        p1.envelhecer()
        print("Pessoa envelheceu 1 ano e aumentou 0,5 cm.")
    elif opcao == "2":
        qtd = float(input("Quanto deseja engordar (kg)? "))
        p1.engordar(qtd)
    elif opcao == "3":
        qtd = float(input("Quanto deseja emagrecer (kg)? "))
        p1.emagrecer(qtd)
    elif opcao == "4":
        qtd = float(input("Quanto deseja crescer (m)? "))
        p1.crescer(qtd)
    elif opcao == "5":
        p1.mostrar_info()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
