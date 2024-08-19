aluno = {"nome": "willace", "idade": 14, "aprovação": True}

#muda os dados
aluno["nome"] = "cristiane"

#adiciona item novo e muda dados
aluno.update({'nome': "wollace", 'endereço': "rua 3"})




print (aluno)

# vai aparecer o nome
print (aluno["nome"])

#vai aparecer o endereço
print (aluno.get("endereço", "nao existe"))

#nao tem nota entao ele vai aparecer que nao existe
print (aluno.get("nota", "nao existe"))
