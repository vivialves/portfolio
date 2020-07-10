# Função que gera agenda de telefones

# Entrada


# Função
def criar_agenda():
    # Função que cria agenda telefônica
    with open(input('Informe um nome para o arquivo de telefones: '), 'w') as arquivo:
        arquivo.write('Telefones')
        arquivo.write('\n')
        while True:
            telefone = input('Infome o telefone: ')
            if telefone != '0':
                nome = input('Informe o nome: ')
                arquivo.write(nome)
                arquivo.write(':')
                arquivo.write(telefone)
                arquivo.write('\n')
            else:
                break

criar_agenda()
