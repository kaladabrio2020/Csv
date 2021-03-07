import PySimpleGUI as sg
import os
import time

def menu():
    sg.theme('DarkAmber')
    Parte1 = [
        [sg.Checkbox('Gerar numero de dados',key='PRI')],
        [sg.Checkbox('Abrir PlanMaker',key='TER')]
    ]
    layout = [
        [sg.Frame('Escolha a opcão',Parte1)],
        [sg.Ok(),sg.Cancel()]
    ]
    window = sg.Window('Janela 1',layout=layout)
    return window



def op1():
    sg.theme('DarkAmber')
    Parte2 = [
        [sg.Text('Quantos dados deseja gera ? ')],
        [sg.Input(key='Numero')],
        [sg.Ok(),sg.Button('Voltar')]
    ]
    window = sg.Window('Janela 2',layout=Parte2)
    return window

def op2():
    layout = [
        [sg.Text('Aperte "Ok"     para gerar. ')],
        [sg.Text('Aperte "Voltar" para o menu.')],
        [sg.Ok(),sg.Button('Voltar')]
    ]
    window = sg.Window('Janela 3',layout=layout)
    return window



