import Gerador_Txt as ge
import Gerador_Dados_Lista    as ran
import PySimples as pg
import Salvando_Csv  as sl
import PySimpleGUI as sg
import random
from   random import randint
import os
import sys
import subprocess




es = ['Mas','Fem']
ep = ['Hum','Exa']

def janela2(event2,valor2):

    if event2[0] == 'Voltar':
        sys.exit()

    x = valor2['Numero']
    x = int(x)

    if event2[0] == "Ok":
        for _ in range(x):
            dados = list()
            escolha = random.choice(es)

            if escolha == 'Mas':
                scolha_p = random.choice(ep)

                pri = ge.Abrindo_txt()
                nome  = pri.homens()
                sobre = pri.sobrenome()
                exat  = pri.exatas()
                huma  = pri.humanas()
                esta  = pri.estados()
                
                seg = ge.retirar()
                nome_r  = seg.retirando(nome)
                sobre_r = seg.retirando(sobre)
                exatas  = seg.retirando(exat)
                humans  = seg.retirando(huma)
                estado  = seg.retirando(esta)
                
                ter = ran.nome_c(nome_r,sobre_r)
                dados.append(ter)
                
                qua = ran.date_ida()
                dados.append(qua[0])
                dados.append(qua[1])
                
                sex = ran.email(ter)
                dados.append(sex)

                set = ran.codigo()
                dados.append(set)

                estado = random.choice(estado)
                dados.append(estado)

                oit = ran.trabalho(exatas,humans,scolha_p)
                dados.append(oit[0])
                dados.append(oit[1])

                a = random.randint(1,6)
                dados.append(a)

                if scolha_p == 'Exa':
                    sl.geral_e(dados)
                    sl.geral_e_parte(dados)

                else:
                    sl.geral_h(dados)
                    sl.geral_h_parte(dados)



            else:
                scolha_p = random.choice(ep)
                pri = ge.Abrindo_txt()
                nome  = pri.mulher()
                sobre = pri.sobrenome()
                exat  = pri.exatas()
                huma  = pri.humanas()
                esta  = pri.estados()
                
                seg = ge.retirar()
                nome_r  = seg.retirando(nome)
                sobre_r = seg.retirando(sobre)

                exatas = seg.retirando(exat)
                humans = seg.retirando(huma)
                estado = seg.retirando(esta)
                

                ter = ran.nome_c(nome_r,sobre_r)
                dados.append(ter)
                
                qua = ran.date_ida()
                dados.append(qua[0])
                dados.append(qua[1])

                sex = ran.email(ter)
                dados.append(sex)

                set = ran.codigo()
                dados.append(set)

                estado = random.choice(estado)
                dados.append(estado)

                oit = ran.trabalho(exatas,humans,scolha_p)
                dados.append(oit[0])
                dados.append(oit[1])

                a = random.randint(1,6)
                dados.append(a)

                if scolha_p == 'Exa':
                    sl.geral_e(dados)
                    sl.geral_e_parte(dados)

                else:
                    sl.geral_h(dados)
                    sl.geral_h_parte(dados)

    sys.exit()
file = open('Abrir.txt','r')
lista =  file.readlines()
file.close()

del lista[2]
leni = []

for i in range(len(lista)):
    stri = lista[i]
    stri = stri.replace('\n','')

    if '{' in stri and '}' in stri:
        stri = stri.replace('{','')
        stri = stri.replace('}','')
        stri = stri.replace("'",'')
    leni.append(stri)

dici = leni[1].split(':')
dici = (tuple(dici),('a',1))
dici = dict(dici)
print(leni[0]=='Ok')
janela2(leni,dici)