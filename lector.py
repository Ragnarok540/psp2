from os.path import join, dirname, realpath
from csv import reader
from lista import lista as ls

def leer_archivo(ruta):
    r = join(dirname(realpath(__file__)), ruta)
    result = []
    with open(r, newline='') as a:
        lector = reader(a, delimiter=';')
        for fila in lector:
            result.append(ls(*fila))
    return (result[0], result[1])

#print(leer_archivo("test.csv"))
