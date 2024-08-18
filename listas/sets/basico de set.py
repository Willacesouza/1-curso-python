list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)   #o set deixa a ordem aleatoria e n da de usar os index 
num2 = set(list2)

print(num1 | num2)  #UNION  junta as 2 listas e tira os repetidos 
print(num1 - num2)  #difference     mostra todos da lista 1 quem nao tem na list2
print(num1 ^ num2)  #symmetric difference   mostra os nao repetidos de todas as listas
print(num1 & num2)  #And    mostra os iguais de todas as listas