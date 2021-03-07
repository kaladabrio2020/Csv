from ast import Num
import time
import datetime
import random 
from   random import randint

alfabeto = [
    'a','b','c','e','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]
escolha = ['Hum','Exa']


def nome_c(a,b):
    nome  = random.choice(a)
    sobre = random.choice(b)
    completo = nome + ' ' + sobre
    return completo










def date_ida():

    ano = random.randint(1969,2002)
    mes = random.randint(1,12)

    if mes == 2:
        dia = random.randint(1,28)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 10:
        dia = random.randint(1,30)
    else:
        dia = random.randint(1,31)

    data_nas = datetime.date(ano,mes,dia)
    atual_dt = datetime.datetime.now()
    idade    = atual_dt.year - ano
    lista    = [data_nas,idade]
    return lista







def email(name):
    name = name.lower()
    name = name.replace(' ','')
    num = random.randint(1,4)

    string = ''

    for i in range(num):
        char = random.choice(alfabeto)
        string = string + char

    numero = random.randint(12,303)
    numero = str(numero)

    x = random.randint(1,3)

    if x == 1:
        email = name +'.'+ string + numero+'@gmail.com'
    if x == 2:
        email = name + string +numero +'.'+'@gmail.com'
    else:
        email = name +'.'+numero +string+'@gmail.com'    
        
    return email
    








def codigo():
    x = random.choice(alfabeto)
    num = random.uniform(1233.1221,4564.3221)
    num = round(num,3)
    num = str(num)
    num = num.replace('.',x)
    

    y = random.randint(5,9)
    string = ''

    for i in range(y):
        a = random.choice(alfabeto)
        p = ['s','m']
        z = random.choice(p)

        if z == 's':
            string = string + a

        if z == 'm':
            a = a.upper()
            string = string + a
        
    codido = string + num
    return codido





def trabalho(exatas,humas,h):
    x = h
    if x =='Hum':
        trabalho = random.choice(humas)
        salario  = random.uniform(1500.00,5000.00)
        salario  = round(salario,2) 
        lista = [trabalho,salario]
        return lista

    elif x == 'Exa':
        trabalho = random.choice(exatas)
        salario  = random.uniform(2000.00,9000.00)
        salario  = round(salario,2)
        lista = [trabalho,salario]
        return lista