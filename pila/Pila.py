class Pila():
    
 def __init__(self, size):
     self.lista = []
     self.tope = 0
     self.size = size
     
def empty(self):
      if self.tope == 0:
          return True
      else:
          return False

def push(self, dato):
    if self.tope < self.size:
        self.lista += [dato]
        self.tope += 1
    else:
        prin("La pila está llena")
def pop(self):
    if self.empty():
        print("la pila está vacia")
    else:
        self.tope -=1
        self.lista = [self.lista[x] for x in range(self.tope)]
def show(self):
    for i in range(self.tope):
        print("[%d] => %d"%(i,self.lista[i]))
def Size(self):
    return self.tope
def Top(self):
    return self.lista[-1]                                

