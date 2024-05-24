nomes = ['Marcos', 'Rambo', 'Magayver', 'John', 'Stalone', 'Misael']

# Usuário informa o indice que deseja alterar

indice = int(input('Informe o índice que deseja alterar: '))

# Coverter a posiçao 0 em 1 para o usuário
indice -= 1

nomes[indice] = input('Informe o novo nome: ')

for nome in nomes:
    print(nome)