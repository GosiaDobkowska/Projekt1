
def reading(sciezka):
    """
    Odczytuje słownik z pliku tekstowego.
    """
    z= eval(open(sciezka, 'r').read())
    return z
    
import numpy as np
def lista_trackow(sciezka, sciezka2):
    """
    Tworzy listę tracków na podstawie pliku song.txt.
    """
    import numpy as np
    lista = open(sciezka, 'r')
    lista=lista.readlines()
    for l in range(0, len(lista)):
        lista[l]=lista[l][0:2]
    z1=[]
    for l in lista:
        z1=np.append(z1, sciezka2+'track'+l+'.txt')
    return z1

def lista_sampli(lista_trakow):
    """
    Na podstawie listy tracków tworzy listę sampli.
    """
    lista_sampli=[]
    for z in lista_trakow:
        lista = open(z, 'r')
        lista=lista.readlines()
        lista_sampli=np.append(lista_sampli, lista)
        lista_sampli2=[]
        j = 0
        for i in lista_sampli:
            lista_sampli2=np.append(lista_sampli2,i.split(" ", 4))
        for j in range(0, len(lista_sampli2)):
            if lista_sampli2[j].find("\n")!=-1:
                lista_sampli2[j]=lista_sampli2[j][0:lista_sampli2[j].find("\n")]
    return lista_sampli2