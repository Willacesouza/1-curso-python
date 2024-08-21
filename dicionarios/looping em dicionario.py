aluno = {"nome": "willace", "idade": 14, "aprovação": True}

#imprime so as chaves
for x in aluno.keys():
    print(x)

#imprime valor
for y in aluno.values():
    print(y)


#imprime chave e valor como tuplas(entre parenteses)
for x in aluno.items():
    print(x)


#imprime chave e valor um do lado do outro
for x, y in aluno.items():
    print(x, y)