import random
print("SASSO, CARTA, FORBICE")
puntigiocatore = 0
punticpu = 0
for x in range(int(input("Scegli quanti turni vuoi giocare:"))):
  mosse = ["s", "c", "f"]
  mossecpu = ["s", "c" , "f"]
  giocatore = (input("Scegli tra carta (scrivi: c), forbice (scrivi: f) e sasso (scrivi: s): "))
 
  if giocatore not in mosse:
   punticpu = punticpu +1
   print("Mossa non contemplata, punto al Computer")
   print("Punti CPU:" + str(punticpu))
   print("Tuoi punti:" + str(puntigiocatore))
  
  else:
    cpu = (random.choice(mossecpu))

    print("CPU gioca:" + cpu)

    #Pareggio
    if cpu == giocatore:
      print("Pari!")

   #Computer vince
    elif  (cpu == "s" and giocatore == "f"):
      print("Hai perso il round")
      punticpu = punticpu +1
    elif  (cpu == "f" and giocatore == "c"):
      print("Hai perso il round")
      punticpu = punticpu +1
    elif  (cpu == "c" and giocatore == "s"):
      print("Hai perso il round")
      punticpu = punticpu +1
  
    #Giocatore Vince
    elif  (giocatore == "s" and cpu == "f"):
      print("Hai vinto il round")
      puntigiocatore = puntigiocatore +1 
    elif  (giocatore == "f" and cpu == "c"):
      print("Hai vinto il round")
      puntigiocatore = puntigiocatore +1 
    elif  (giocatore == "c" and cpu == "s"):
      print("Hai vinto il round")
      puntigiocatore = puntigiocatore +1 
    
    print("Punti Computer:" + str(punticpu))
    print("Tuoi punti:" + str(puntigiocatore))

if punticpu > puntigiocatore:
  print("Hai perso!")
elif punticpu == puntigiocatore:
  print("Pareggio!")
else:
  print("Hai vinto!")
