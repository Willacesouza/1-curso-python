    #serve pra operações pra usar menos armazenamento

from array import array

let = ["a", "b", "c"]
num1 = [1, 2, 3]
num2 = [10, 20, 30]


print(let)
print(num1)
print(num2)
print(" ")

let = array("u", ['a', 'b', 'c'])
num1 = array('i', [1, 2, 3])
num2 = array('f', [10.1 , 20.2 , 30.3])

let.remove("a")
print(let)
print(num1)
print(num2)