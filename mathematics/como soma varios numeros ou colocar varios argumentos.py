    #colocar um * antes do parametro e pode colocar quantos argumentos quiser

def soma (*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2, 3, 4, 7)

print (x)

