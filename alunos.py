# 1. Criar lista de alunos
alunos = ["Kaneda", "Doua", "Tetsuo", "Vegeta"]
print("Lista inicial: ", alunos)
# 2. Adicionar novos alunos
alunos.append("Goku")
alunos.append("Bulma")
alunos.append("Logen Nove Dedos")
print("Após adicionar: ", alunos)
# 3. Remover um aluno
alunos.remove("Vegeta")
print("Após remover Vegeta: ", alunos)
# 4. Usar dicionário para pesquisar
# Vamos criar um dicionário onde a CHAVE é o nome e o VALOR é o status
alunos_dict = {aluno: "Ativo" for aluno in alunos}

# Agora a pesquisa funciona!
nome_pesquisa = "Bulma"
print(f"Status de {nome_pesquisa}: {alunos_dict[nome_pesquisa]}")