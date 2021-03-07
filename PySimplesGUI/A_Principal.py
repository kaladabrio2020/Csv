from PySimpleGUI.PySimpleGUI import Print
import PySimples   as pg
import PySimpleGUI as sg
import time
import random
from   random import randint
import os
import subprocess




def main():
    jan1 = pg.menu()
    jan2 = pg.op1()
    jan3 = pg.op2()

    event1 , valor1 = jan1.read()
    lista = list(valor1.values())


    while True:
        if event1 == 'Cancel' or event1 == sg.WIN_CLOSED:
            jan1.close()
            break

        if event1 == 'Ok':
            jan1.hide()
            
            
            if lista.count(False)>3:
                return main()


            elif lista.count(True)>1:
                return main()


            if valor1['PRI'] == True:
                event2 , valor2 = jan2.read()
                a = valor2['Numero']

                if event2 == "Voltar" or event2 == sg.WIN_CLOSED:
                    jan2.hide()
                    return main()

                valor2['Numero'] = 1
                if a == '' or a.isdecimal() == False:
                    jan2.hide()
                    sg.popup('Invalido',valor2)
                    return main()

                l = [event2,valor2,jan2]
                coloque(l)
                jan2.hide()

                if event2 == 'Ok':
                    j = timep(int(a))
                    for i in range(int(a)): 
                        time.sleep(j)
                        sg.OneLineProgressMeter('My Meter', i+1, int(a), 'key','Carregando')
                        subprocess.call('Gerador_Csv.py',shell=True)
                    sg.popup('','Pronto!')
                    return main()

            if valor1['TER'] == True:
                os.startfile('C:\Program Files (x86)\SoftMaker FreeOffice 2018\PlanMaker.exe')    
        event1 , valor1 = jan1.read()


def timep(a):
    if a == 1:
        return 1.5
    if a <8:
        return 1
    elif a >10 and a< 15:
        return 0.6
    elif a >15:
        return 0.12

        
def coloque(i):
    file = open('A_Abrir.txt','w')
    for e in range(len(i)):
        file.write(str(i[e])+'\n')
    file.close()


if __name__ == '__main__':
    main()