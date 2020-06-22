def maior(a,b):
    c = a
    if b > a:
        c = b
    return c

def soma( lista, x=0):
    soma = 0
    for valor in lista:
        soma += valor
    return soma + x

def media(lista):
    return (soma(lista)/len(lista))

def valores_iguais(lista1,lista2):
    lista3 = []
    for valorLista1 in lista1:
        for valorLista2 in lista2:
            if valorLista1 == valorLista2:
                lista3.append(valorLista1)
    return lista3

def indice_prim_valor_igual(lista1,lista2):
    for valorLista2 in lista2:
        for i,valorLista1 in enumerate(lista1):
            if valorLista2 == valorLista1:
                return i  
