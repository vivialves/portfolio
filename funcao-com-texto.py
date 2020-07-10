# Exercicio 14


import datetime




# Entrada
# # Função

def receber_data_nascimento():
    # Função que recebe arquivo de texto com a data de nascimento
    with open(input('Informe um nome para o arquivo: '), 'w') as arquivo:
        arquivo.write('Nomes e data de nascimento: ')
        arquivo.write('\n')
        while True:
            nome = input('Informe o nome: ')
            if nome != 'sair':
                d_nascimento = (input('Informe a data de nascimento: '))
                arquivo.write(nome)
                arquivo.write(':')
                arquivo.write(d_nascimento)
                arquivo.write('\n')
            else:
                break

receber_data_nascimento()


def idade():
    # Função que retorna a idade informada no arquivo de texto
    with open('nascimento.txt', 'r') as arquivo:
        texto = arquivo.readlines()
        data = datetime.datetime.now()
        ano = data.year
        lista = [texto[i].split(':') for i in range(1, len(texto))]
        lista_sep_barra = [lista[i][1].split('/') for i in range(0, len(lista))]
        dicionario = {lista[i][0]: int(lista_sep_barra[i][2]) for i in range(0, len(lista))}
        with open('idade.txt', 'w') as arquivo:
            arquivo.write('Nomes e idades:')
            arquivo.write('\n')
            for chave, valor in dicionario.items():
                arquivo.write(chave)
                arquivo.write(':')
                idade = ano - valor
                idades = str(idade)
                arquivo.write(idades)
                arquivo.write('\n')
                print(f'{chave}:{idade}')

idade()
