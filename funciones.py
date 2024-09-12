print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print(f"chat {mensa}")
    
def ellacontesta(mensa):
    print(f"chat ella: {mensa}")
    
def escribenombre(ap,n):
    print(f"Tu nombre completo es : {n} {ap}")
    
def suma(a,b):
    s=a+b
    return s

def res(a,b):
    r=a-b
    return r

def mult(a,b):
    m=a*b
    return m

def div(a,b):
    d=a/b
    return d





# llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Cisneros", "Abril")

print("Operacion suma")
c1=int(input("Ingresa un numero:  "))
c2=int(input("Ingresa un numero:  "))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacion resta")
c3=int(input("Ingresa un numero:  "))
c4=int(input("Ingresa un numero:  "))
dameresta=res(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print("Operacion multiplicacion")
c5=int(input("Ingresa un numero:  "))
c6=int(input("Ingresa un numero:  "))
damemult=mult(c5,c6)
print(f"La multiplicacion de {c5} * {c6} = {damemult}")

print("Operacion divicion")
c7=int(input("Ingresa un numero:  "))
c8=int(input("Ingresa un numero:  "))
damediv=div(c7,c8)
print(f"La multiplicacion de {c7} / {c8} = {damediv}")




