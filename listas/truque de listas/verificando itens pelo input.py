cores = ["verde", "azul", "amarelo", "verde"]
#           0       1         2         3

digite_cor = input("digite a cor: ")

if digite_cor.lower() in cores:
    print("true")
else:
    print("false")