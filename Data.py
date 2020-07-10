# Função que escreve a data por extenso 


# Entrada
dict1 = {'01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril', '05': 'maio', '06': 'junho', '07': 'julho',
         '08': 'agosto', '09': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
data_num = input('Inform a date: ')
# Processamento
lista_data = data_num.split('/')
# Função
def transf_data(*lista_data):
    return lista_data

# Saída
print(data_num)
lista_data[1] = dict1.get(lista_data[1])
print(transf_data(f'{lista_data[0]} de {lista_data[1]} de {lista_data[2]}'))