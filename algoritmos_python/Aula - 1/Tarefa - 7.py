def area_quadrado(altura, largura):
    if altura == largura:
        area = altura * largura
        return area
    else:
        print("Isso não é um quadrado")
        return None



altura = float(input("Escreva a altura: "))
largura = float(input("Escreva a largura: "))

area = area_quadrado(altura, largura)

if area:
    print("Esse é a sua área do quadrado: ", area)
    print("Esse é a área dobrada: ", area * 2)
else:
    print("fim")


