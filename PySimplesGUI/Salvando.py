import csv
from os import write

def geral_e(a):
    with open('X_Dados_Gerais_Exatas.csv','a',newline='') as file:
        write = csv.writer(file)
        write.writerow(a)
        file.close()
    

def geral_e_parte(a):
    lista = []
    lista.append(a[0])
    lista.append(a[2])
    lista.append(a[6])
    lista.append(a[7])

    with open('X_Dados_Importante_Exatas.csv','a',newline='') as file:
        write = csv.writer(file)
        write.writerow(lista)
        file.close()

def geral_h(a):
    with open('X_Dados_Gerais_Humanas.csv','a',newline='') as file:
        write = csv.writer(file)
        write.writerow(a)
        file.close()


def geral_h_parte(a):
    lista = []
    lista.append(a[0])
    lista.append(a[2])
    lista.append(a[6])
    lista.append(a[7])
    
    with open('X_Dados_Importantes_Humanas.csv','a',newline='') as file:
        write = csv.writer(file)
        write.writerow(lista)
        file.close()