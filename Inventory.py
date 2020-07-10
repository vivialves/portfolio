# Programa que faz inventário - an inventory program
#
# Secao 8 exercicio 7
#
print("Vamos fazer um inventário do laboratório de TI!")

# Entrada
contador = 0
cod = 0
defeito = -1
lista1 = []
lista2 = []
lista3 = []
lista4 = []

# Processamento

while defeito != 0:
    contador = contador + 1
    cod = int(input("Informe o código do equipamento: "))
    print("Informe o defeito do equipamento: ")
    print("1 - necessita de esfera \n"
          "2 - necessita de limpeza \n"
          "3 - necessita troca do cabo ou conector \n"
          "4 - quebrado ou inutilizado ")
    defeito = int(input(f"{contador}/{cod}: "))

    if defeito == 1:
        lista1.append(cod)
    elif defeito == 2:
        lista2.append(cod)
    elif defeito == 3:
        lista3.append(cod)
    elif defeito == 4:
        lista4.append(cod)
    elif defeito == 0:
        print("Programa finalizado!")
    else:
        print("Código inexistente, digite um código válido")
    
print(lista1)
print(lista2)
print(lista3)
print(lista4)

quant1 = len(lista1)
quant2 = len(lista2)
quant3 = len(lista3)
quant4 = len(lista4)
quantTotal = quant1 + quant2 + quant3 + quant4

perc_quant1 = (quant1/quantTotal) * 100
perc_quant2 = (quant2/quantTotal) * 100
perc_quant3 = (quant3/quantTotal) * 100
perc_quant4 = (quant4/quantTotal) * 100

# Saída

print(f"Quantidade de mouses: {quantTotal}")
print("Situação                                 Quantidade    Percentual")
print(f"1 - necessita de esfera                     {quant1}          {perc_quant1:.2f}%")
print(f"2 - necessita de limpeza                    {quant2}          {perc_quant2:.2f}%")
print(f"3 - necessita troca do cabo ou conector     {quant3}          {perc_quant3:.2f}%")
print(f"4 - quabrado ou inutilizado                 {quant4}          {perc_quant4:.2f}%")
