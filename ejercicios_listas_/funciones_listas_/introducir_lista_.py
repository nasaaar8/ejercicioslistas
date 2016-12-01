'''
Created on 1 dic. 2016

@author: najib
'''
def introducir_lista(l):
    while True:
        pregunta=input("¿Desea añadir un elemento?Responda si o no:")
        if pregunta=="si":
            elemento=input("¿Que elemento desea añadir?")
            l.append(elemento)
            print(l)
        if pregunta=="no":
            print("La lista esta completada.")
            return l
            break
if __name__=="__main__":
    l=[]
    lista=introducir_lista(l)
    print(lista)