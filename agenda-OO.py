# Programa que gera uma agenda, utilizando a programação orientada a objeto.


# Exercicio 2

class Agenda:


    @classmethod
    def armazenar_pessoa(cls) -> None:
        with open('agenda.txt', 'w') as arquivo:
            arquivo.write('Agenda')
            arquivo.write('\n')
            for i in range(0, 10):
                nome = input('Informe o nome: ')
                idade = input('Informe a idade: ')
                altura = input('Informe a altura: ')
                arquivo.write(nome)
                arquivo.write(':')
                arquivo.write(idade)
                arquivo.write(' ---> ')
                arquivo.write(altura)
                arquivo.write('\n')


    @classmethod
    def remover_pessoa(cls) -> None:
        with open('agenda.txt', 'r+') as arquivo:
            texto = arquivo.readlines()
            listasep = [texto[i].split('\n') for i in range(1, len(texto))]
            lista = [listasep[i][0].split(':') for i in range(0, len(listasep))]
            dicionario = {lista[i][0]: lista[i][1] for i in range(0, len(lista))}
            nome = input('Informe qual pessoa deseja remover: ')
            dicionario.pop(nome)
            dicionariostr = str(dicionario)
            aj_dicionariostr = dicionariostr[1:len(dicionariostr)]
            bj_dicionariostr = aj_dicionariostr[0:len(dicionariostr)-2]
            print(bj_dicionariostr)
            listanova = bj_dicionariostr.split(',')
            print(listanova)
        with open('agenda.txt', 'w') as arquivo:
            arquivo.write('Agenda')
            arquivo.write('\n')
            for i in range(0, len(listanova)):
                arquivo.write(listanova[i])
                arquivo.write('\n')


    @classmethod
    def buscar_pessoa(cls) -> int:
        with open('agenda.txt', 'r') as arquivo:
            texto = arquivo.readlines()
            listasep = [texto[i].split('\n') for i in range(1, len(texto))]
            lista = [listasep[i][0].split(':') for i in range(0, len(listasep))]
            dicionario = {lista[i][0]: lista[i][1] for i in range(0, len(lista))}
            nome = input('Informe qual pessoa deseja buscar: ')
            temp = list(dicionario.items())
            busca = [indice for indice, chave in enumerate(temp) if chave[0] == nome]
            print(f'{nome} está na posição {busca[0] + 1}')
        return busca[0]

    @classmethod
    def imprimir_agenda(cls) -> None:
        with open('agenda.txt', 'r') as arquivo:
            texto = arquivo.read()
            print(texto)

    @classmethod
    def imprimir_pessoa(cls) -> None:
        with open('agenda.txt', 'r') as arquivo:
            texto = arquivo.readlines()
            listasep = [texto[i].split('\n') for i in range(1, len(texto))]
            lista = [listasep[i][0].split(':') for i in range(0, len(listasep))]
            dicionario = {lista[i][0]: lista[i][1] for i in range(0, len(lista))}
            numero = int(input('Informe qual posição deseja buscar: '))
            temp = list(dicionario.items())
            busca = [chave for indice, chave in enumerate(temp) if indice == numero]
            print(busca)


# Saída
Agenda.armazenar_pessoa()
Agenda.remover_pessoa()
Agenda.buscar_pessoa()
Agenda.imprimir_agenda()
Agenda.imprimir_pessoa()
