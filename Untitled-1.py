def somma (a,b):
  return (a+b)
  
def AreaTrapezio():
  print("Dati Trapezio: ")
  a=int(input("Base 1: "))
  b=int(input("Base 2: "))
  h=int(input("Altezza: "))
  return((somma(a,b)*h)/2)
  print("")

def AreaRettangolo():
  print("Dati Rettangolo:")
  a=int(input("Base: "))
  b=int(input("Altezza: "))
  return(a*b)
  print("")

def SommaAree():
  return(AreaRettangolo()+AreaTrapezio())

print(SommaAree())