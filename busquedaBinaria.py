def busqueda_binaria(dato):
    izquierda = 0
    derecha = len(lista)-1
    while izquierda<=derecha:
        medio =(izquierda + derecha)//2
        if dato ==  lista[medio]:
            return medio
        elif dato < lista[medio]:
             derecha = medio -1
        else:
            izquierda = medio +1
    return None    
         
def buscar(dato):
    if busqueda_binaria(dato) == None:
         return "El dato %d no se encuentra"
    else:
         return "El dato %d se encuentra en el indice: %d " %(dato, busqueda_binaria(dato))


lista = [5,12,15,30,50,65,70,87,88,96]
for i in range(len(lista)):
    print("[%d] => [%d]"%(i,lista[i]))
print(buscar(12))