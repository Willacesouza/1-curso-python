#Set é similar as listas mas evita itens duplicados e nao usa index

list1 = set([1, 2, 3, 4, 5, 6]) #assim transforma uma lista em set


s1 = {1, 2, 3, 4, 5, 6}    #ou so colocar em chaves que ja vira um set

s1.add(1)   #pra colocar so um numero
s1.update([10,11])  #assim pra adicionar mais numero

s1.remove(1)    #gera erro se o numero nao tiver na lista
s1.discard(100) #se nao tiver na lista ele nao gera erro

print(s1)