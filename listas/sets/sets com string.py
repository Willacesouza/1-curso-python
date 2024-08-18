s1 = {'a', 'b', 'c'}
s2 = {'a', 'b', 'd'}
s3 = {'c', 'd', 'f'}

#mostra so os que nao repete da lista 1
s4 = s1.difference(s2)

#mostra todos os que nao repetem e tira so os repetentes
s5 = s2.union(s3)

#tira todos os repetidos dos 2 sets
s6 = s1.symmetric_difference(s3)    

#mostra so 1 dos que repetem 
s7 = s3.intersection(s2)    


print (s4)
print (s5)
print (s6)
print (s7)