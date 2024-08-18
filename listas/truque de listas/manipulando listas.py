cdd1 = "sao paulo"
cdd2 = "rio de janeiro"
cdd3 = "manaus"


    #isso é uma lista
cidades = ["rio de janeiro", "sao paulo", "manaus", "salvador"] 
#                 0               1           2          3


    #.append adiciona um item na lista
cidades.append("santa catarina")


    #remove um item de uma lista
cidades.remove("sao paulo")


    #adiciona um item e pode adicionar na posição que voce colocar no inicio
cidades.insert (1, "santos")


    #tira o item pela posição
cidades.pop(0)


    #para aparecer um index especifico é so colocar a posição entre [] no print
print (cidades[0])

print (cidades)