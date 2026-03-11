#Dicionário - chaves únicas (par chave-valor. Exemplo: Nome: Telefone)
telefones3 = [("Magatsu","2345-6789"),("Anotsu","3344-5566"),("Abayama","7777-8989")]
#print(telefones3)

telefones3_dict = dict(telefones3)
#print(telefones3_dict)

#Chave
print(telefones3_dict["Magatsu"])

#Adicionar
telefones3_dict["Shira"] = "666-666"
print(telefones3_dict)

#Remover
telefones3_dict.pop("Shira")
print(telefones3_dict)

