#defaut e non_defaut, definir o valor da variavel por ultimo e nao precisa colocar argumento se o parametro for defaut (definido ja no parametro)

def boas_vindas(nome, quantidade = 5):  #aqui é o parametro
    print (f"ola {nome}")
    print (f"temos {quantidade} celulares em estoque")

boas_vindas("will") #aqui o argumento