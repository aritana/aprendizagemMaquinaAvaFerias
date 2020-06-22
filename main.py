from codigo import maior, soma,media,valores_iguais,indice_prim_valor_igual
if __name__ == "__main__":
    x = maior(8,6) #maior(a,b): Retorna o maior valor entre a e b)
    print(x)
    lista1 =[1,2,9,8]  
    lista2 =[0,2,39,8]   
    x = 1
    print (soma(lista1,x))#soma elementos da lista, e adiciona na soma valor de x caso possua.
    print (media(lista1)) #media da lista
    print (valores_iguais(lista1,lista2))#valores iguais entre duas listas
    print (indice_prim_valor_igual(lista1,lista2))#indice do primeiro valor da lista 1 igual a algum da lista 2
    
