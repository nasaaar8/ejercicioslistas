'''
Created on 1 dic. 2016

@author: najib
'''
try:
    def introducir_lista(l):
        '''
        Funcion que ,a partir de una lista vacia, incluye los elementos creando asi la propia lista.
        '''
        while True:
            pregunta=input("¿Desea añadir un elemento?Responda si o no:")#variable segunla que la lista continua o acaba#
            if pregunta=="si":
                elemento=input("¿Que elemento desea añadir?")#elemento a añadir#
                l.append(elemento)
                print(l)
            if pregunta!="si":
                print("La lista esta completada.")
                return l
                break
    def sacar_elementos(lista):
        '''
        Funcion que saca todos los elementos de la lista, englobandolas en tres variables que son devueltas.
        '''
        id_paciente=lista[0]
        fase_ensayo=lista[1]
        serie_temperaturas=lista[2:]
        return id_paciente,fase_ensayo,serie_temperaturas
    def flotantes(lista):
        '''
        Funcion que convierte las temperaturas (cadena de caracteres) en flotantes.
        '''
        for n in range(2,len(lista)):
            lista[n]=float(lista[n])
        return lista
    def anadir_elemento(lista):
        '''
        Funcion que añade un elemento.
        '''
        lista.append(37.2)
        for n in range(len(lista),len(lista)):
            lista[n]=float(lista[n])
        return lista
    def anadir_lista(lista1):
        '''
        Funcion que añade una sublista.
        '''
        lista2=[36.5,37.3]
        lista1.extend(lista2)
        for n in range(len(lista1)-1,len(lista1)):
            lista1[n]=float(lista1[n])
        return lista1
    def numero_temperaturas(lista2):
        '''
        Funcion que devuelve el numero de temperaturas de la lista
        '''
        numero_temperaturas=len(lista2)-2
        return numero_temperaturas
    def cadena_texto(lista2):
        '''
        Funcion que convierte las temperaturas en una cadena de texto.
        '''
        for n in range(2,len(lista2)):#convertirlos en cadena de texto#
            lista2[n]=str(lista2[n])
        elemento=lista[2]
        for n in range(3,len(lista2)):#sacar elementos y concatenar#
            elemento=elemento+", "+lista[n]
        temperaturas_string=elemento
        return temperaturas_string
    def ordenar_mayor_menor(lista2):
        '''
        Funcion que ordena las temperaturas de la lista de mayor a menor.
        '''
        for n1 in range(2,len(lista2)-1):#repetir el siguiente proceso#
            for n in range(2,len(lista2)-1):#numero menor el ultimo#
                if lista2[n]<lista2[n+1]:
                    lista2[n],lista2[n+1]=lista2[n+1],lista2[n]
        lista_ordenada=lista2
        return lista_ordenada
    def media_temperaturas(lista3):
        '''
        Funcion que realiza la media de las temperaturas.
        '''
        lista3=flotantes(lista3)#temperaturas en flotantes#
        elemento=lista[2]
        t=1
        for n in range(3,len(lista3)):
            t=t+1#numero de sumandos#
            elemento=elemento+lista[n]#suma total#
        media=elemento/t
        return media
    def numero_mayor_menor(lista3):
        '''
        Funcion que devuelve las temperaturas mayor y menor
        '''
        numero_mayor=lista[2]#numero mayor#
        numero_menor=lista[len(lista3)-1]#numero menor#
        return numero_mayor,numero_menor
    if __name__=="__main__":
        l=[]
        lista=introducir_lista(l)
        print(lista)
        id_paciente,fase_ensayo,serie_temperaturas=sacar_elementos(lista)
        print(id_paciente)
        print(fase_ensayo)
        print(serie_temperaturas)
        lista=flotantes(lista)
        print(lista)
        lista1=anadir_elemento(lista)
        print(lista1)
        lista2=anadir_lista(lista1)
        print(lista2)
        numero_temperaturas=numero_temperaturas(lista2)
        print("Hay %d"%numero_temperaturas,"temperaturas.")
        temperaturas_string_=cadena_texto(lista2)
        print("Las temperaturas son %s"%temperaturas_string_,".")
        lista3=ordenar_mayor_menor(lista2)
        print("La lista con las temperaturas ordenadas de mayor a menor es:")
        print(lista3)
        media_temperaturas=media_temperaturas(lista3)
        print("La media de las temperaturas es %f"%media_temperaturas,".")
        temperatura_mayor,temperatura_menor=numero_mayor_menor(lista3)
        print("La temperatura mayor es %f"%temperatura_mayor,"y la menor es %f"%temperatura_menor)
except:
    print("Ha hecho algo que no es adecuado.")