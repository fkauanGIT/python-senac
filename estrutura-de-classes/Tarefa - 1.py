class Bola:
    def __init__(self, color, circumference, material):
        self.color = color
        self.circumference = circumference
        self.material = material

    def __str__(self):
        return f'Cor: {self.color}, Circunferência: {self.circumference}, Material: {self.material}'

    def change_color(self, new_color):
        self.color = new_color
        print("A cor mudou para: " + new_color)

    def show_color(self):
        print("Sua cor é: " + self.color)


bola_vermelha = Bola("Vermelho", 10, "Couro")
print(bola_vermelha)
bola_vermelha.show_color()
bola_vermelha.change_color("Azul")
bola_vermelha.show_color()