telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788']
#print(telefones[2])

#Acrescentar um elemento ao final da lista
telefones.append("5555-5555")
#print(telefones)

#Acrescentar um elemento em um índice escolhido na lista
telefones.insert(0,"333-333")
#print(telefones)

#Remover um elemento da lista
telefones.remove("333-333")
#print(telefones)

#Remover um elemento da lista pelo índice
telefones.pop(1)
#print(telefones)

#Lista composta por Tupla
contato = ("Manji","324-5678")

telefones2 = []
telefones2.append(contato)
print(telefones2)

telefones3 = [("Magatsu","2345-6789"),("Anotsu","3344-5566"),("Abayama","7777-8989")]
print(telefones3)
print(telefones3[0][1])



