#Divisibile o non divisibile per n
print("Numeri divisibili per 3 (DA 0 A 30)")
for x in range(31): #Sostituire 31 con (numero range-1)
  if x%3 != 0: #Sostituire n con divisore desiderato
    print(x, ":", "Non divisibile")
  else:
    print(x, ":", "Divisibile")

#Pari o dispari (uguale a sopra)
print("")
print("Numeri pari o dispari (DA 0 A 30)")
for x in range(31): 
  if x%2 != 0:
    print(x, ":","Dispari")
  else:
    print(x, ":", "Pari")

#Print numeri pari (uguale a sopra)
print("")
print("Stampa solo i numeri pari")
for x in range(31):
  if x%2 == 0:
    print(x)

#Divisori di n
print("")
print("Divisori di n")
n=56
for x in range(1,n+1):
  if n%x == 0:
    print(x)

#Tabellina di n
print("")
print("Tabellina di n")
n = 9
for x in range (11):
  print(n*x)

#BUZZ
print("")
print("Scrive BUZZ se un numero contiene o è divisibile per la cifra n")
n = 7
for x in range(1, 101):
  numero = str(x)
  divisore = str(n)
  if divisore in numero:
    print("BUZZ")
  else:
    int(x)
    int(n)
    if x%n != 0:
      print(x)
    else:
     print("BUZZ")

#Sequenza di Fibonacci 
print("")
print("Sequenza di Fibonacci")
n=0
m=1
for x in range(10):
  m=m+n
  n=n+m
  print(m)
  print(n)

#Perimetro ed area del rettangolo. 
print("")
#Var da inserire:
  #Base
  #Altezza
b=15
h=10
a=b*h
p=b*2+h*2
print("Perimetro:", p)
print("Area:", a)

print("")
n = int(input("Scegli un numero naturale"))
m = int(input ("Scegli un altro numero naturale"))
r = 0

while n > 0:
  r = r+m
  n = n-1
print ("Moltiplicando i due numeri si ottiene:" + str(r))