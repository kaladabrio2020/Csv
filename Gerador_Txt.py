


class Abrindo_txt:
    def homens(self):
        file  = open('X_Nomes_Maculino.txt','r')
        lista = file.readlines()
        file.close()
        return lista

    def mulher(self):
        file  = open('X_Nomes_Feminino.txt','r')
        lista = file.readlines()
        file.close()
        return lista

    def sobrenome(self):
        file  = open('X_Sobrenomes.txt','r')
        lista = file.readlines()
        file.close()
        return lista
    

    def estados(self):
        file  = open('X_Estados.txt','r')
        lista = file.readlines()
        file.close()
        return lista


    def exatas(self):
        file  = open('X_Trabalho_Exatas.txt','r')
        lista = file.readlines()
        file.close()
        return lista

    def humanas(self):
        file  = open('X_Trabalhos_Humanas.txt','r')
        lista = file.readlines()
        file.close()
        return lista
    
    
class retirar:
    def retirando(self,a):
        lista = list()
        for i in range(len(a)):
            string = a[i]
            string = string.replace('\n','')
            string = string.split('\t')
            lista.extend(string)
        return lista
    
