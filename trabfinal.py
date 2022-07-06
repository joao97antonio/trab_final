from asyncore import write
import pandas as pd
import numpy as np
import time
import os

pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
vet = []
def merge (A, aux, esquerda, meio, direita):
    for k in range(esquerda, direita+1):
        aux[k] = A[k]
    i = esquerda
    j = meio+1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1

def mergesort(A, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2
    mergesort(A, aux, esquerda, meio)
    mergesort(A, aux, meio + 1, direita)
    merge(A, aux, esquerda, meio, direita)

def arq_open():
    global vet
    for a in range(100):
        df = pd.read_fwf("matrizes/" + str(a+1) + ".txt",sep =" ",header=None)
        vet.append(df.to_numpy())

def arq_sort():
    global vet
    for a in range(100):
        for b in range(100):
            aux = [0] * len(vet[a][b])
            mergesort(vet[a][b], aux, 0, len(vet[a][b]) - 1)

def arq_write():
    global vet
    for a in range(100):
        for b in range(100):
            with open("output/"+ str(a) +"_output.txt","a") as arq:
                arq.write(str(vet[a][b]))

def arq_delete():
    if (len(os.listdir("output")) != 0):
        for a in range(100):
            os.remove("output/"+ str(a) + "_output.txt")

arq_delete()

start_time = time.time()

arq_open()
open_time = time.time() - start_time
arq_sort()
sort_time = time.time() - start_time
arq_write()
write_time = time.time() - start_time
print("Tempo Total de Abertura: " + str(open_time))
print("Tempo Total de ordenacao: " + str(sort_time))
print("Tempo Total de Escrita: " + str(write_time))
print("Tempo Total de Execução: " + str((time.time()-start_time)))