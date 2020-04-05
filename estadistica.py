from math import sqrt
from lista import sumar, largo, mapear, zipear, lista

def promedio(x):
    return sumar(x) / largo(x) if largo(x) > 0 else 0

def desviacion(x):
    if largo(x) < 2:
        return 0
    prom = promedio(x)
    restas = mapear(lambda y: y - prom, x)
    cuadrados = mapear(lambda y: y * y, restas)
    sumatoria = sumar(cuadrados)
    return sqrt(sumatoria / (largo(x) - 1))

def beta_1(x, y):
    multip = zipear(lambda z, w: z * w, x, y)
    sum_multip = sumar(multip)
    cuadrados = mapear(lambda z: z * z, x)
    sum_cuadrados = sumar(cuadrados)
    numerador = sum_multip - largo(x) * promedio(x) * promedio(y)
    denominador = sum_cuadrados - largo(x) * promedio(x) * promedio(x)
    return numerador / denominador

def beta_0(x, y):
    pass

def r_xy(x, y):
    pass

def r2(x, y):
    pass

def y_k():
    pass

ls1 = lista(130, 650, 99,  150, 128, 302, 95,  945,  368, 961)
ls2 = lista(186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
print(beta_1(ls1, ls2))
