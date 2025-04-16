class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def __str__(self):
        return f'Tamanho do lado do quadrado: {self.tamanho_do_lado}'

    def mudar_valor_do_lado(self, novo_valor_do_lado):
        self.tamanho_do_lado = novo_valor_do_lado
        print(f"O novo valor é: {self.tamanho_do_lado}")

    def calcular_area(self):
        area = self.tamanho_do_lado * self.tamanho_do_lado
        print(f"Valor da área é: {area}")


quadrado = Quadrado(3)
print(quadrado)
quadrado.calcular_area()
quadrado.mudar_valor_do_lado(4)
quadrado.calcular_area()
