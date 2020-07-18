def contar(dato, objetivo):
    n=0
    for item in dato:
        if item==objetivo:
            
            n+=1
    return n      

lista = ["a", "a", "c"]
cuenta = contar(lista, "a")
print("la cantidad es ",cuenta)