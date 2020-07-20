def busquedaLineal(dato):
    for x in range(len(lista)):
        if lista[x] == dato:
            return x
    return None
def buscar(dato):
    if busquedaLineal(dato) == None:
        return "El datos %d no se encontro"%(dato)
    else:
        return "El datos %d se encontro en el indice: %d"%(dato,busquedaLineal(dato))    
lista = [12,45,78,9,6,5,4,2,1,0,12,45,78,63,25,98]
for i in range(len(lista)):
    print("[%d] => [%d]"%(i,lista[i]))

print (buscar(0))