import random
d10= [1,2,3,4,5,6,7,8,9,10]
d6=[1,2,3,4,5,6]
d2= [1,2]
playerpf=10
playerstr = 0
playercha = 0
playerwiz = 0

giocatore=[1,2,3,4]
torch=False
redpotion = 0
greenpotion = 0
playersword = False
swordiscursed = True

damage=1
goblinpf=2

orcpf=4
orcmod=1

dragonpf=10
dragonmod=3

#Skillroll
def StrenghtRoll():
  r=int(random.choice(d10))
  tot=r+playerstr
  print("You roll a " + str(r) + "+" + str(playerstr) + "=" + str(tot))
  return(tot)
def CharismaRoll():
  r=int(random.choice(d10))
  tot=r+playercha
  print("You roll a " + str(r) + "+" + str(playercha) + "=" + str(tot))
  return(tot)
def WizardryRoll():
  r=int(random.choice(d10))
  tot=r+playerwiz
  print("You roll a " + str(r) + "+" + str(playerwiz) + "=" + str(tot))
  return(tot)

#Enemyroll
def GoblinRoll():
  r=int(random.choice(d10))
  print("The goblin rolls a " +str(r))
  return(r)
def OrcRoll():
  r=int(random.choice(d10))
  tot=r+orcmod
  print("The orc rolls a " + str(r) + "+" + str(orcmod) + "=" + str(tot) )
  return(tot)
def DragonRoll():
  r=int(random.choice(d10))
  tot=r+dragonmod
  print("The dragon rolls a " + str(r) + "+" + str(dragonmod) + "=" + str(tot) )
  return(tot)

#Playerdeath
def Death():
  print(str(playername) + " , YOU DIED!")
if playerpf == 0:
  Death()

#Beginning
print("A great adeventure awaits you!")
print("[To answer the question, write the number corresponding to the desired outcome!]")

#Playername
playername = input("What's your name? ")
print("Greetings, " + playername + "!")
print("You are on a quest to venture in the Dragon Dungeon and kill the red dragon! ")
print("")
#Playerskills
print("You have 3 skills: STRENGHT, CHARISMA and WIZARDRY. ")
print("All three starting at 0")
print("You have two SKILL POINTS, choose in which skill")
print("STRENGHT(1), CHARISMA(2), or WIZARDRY(3) you want to spend them")
playerskill=input("(2 points remaining)")

if playerskill == str(1):
  playerstr = playerstr+1
elif playerskill == str(2):
  playercha = playercha+1
else:
  playerwiz = playerwiz + 1

playerskill= input("(1 point remaining) ")
if playerskill == str(1):
  playerstr = playerstr+1
elif playerskill == str(2):
  playercha = playercha+1
else:
  playerwiz = playerwiz + 1

def Showstats():
  print("Your stats are:")
  print("HEALTH POINTS(HP): " + str(playerpf))
  print("STR = " + str(playerstr))
  print("CHA = " + str(playercha))
  print("WIZ = " + str(playerwiz))
  return()
Showstats()
###FUNZIONI
#POTIONROOM()
def IdentifyPotion():
  print("")
  print("You use your WIZARDRY to try to identify the red one.")
  if WizardryRoll() >7:
    print("You recognize the red potion as a healing potion")
    print("It heals you 3pf when you drink it")
  else:
    print("You don't recognize the red potion")
  print("You use your Wizardry again to try to identify the green one")
  if WizardryRoll()>6:
    print("You recognize the green potion as a vial of acid")
    print("It removes you 3pf if you drink it.")
  else:
    print("You don't recognize the green potion")
  return (redpotion)

def TakePotion():
  print("")
  print("Do you take the red one(1), the green one (2), both(3)")
  potiontaken=input(" or none of them(4)? ")
  if potiontaken==1:
    redpotion==redpotion+1
    print("You take the red potion and proceed through the dungeon. ")
  elif potiontaken==2:
    greenpotion==greenpotion+1
    print("You take the green potion and proceed through the dungeon. ")
  elif potiontaken==3:
    redpotion==redpotion+1
    greenpotion==greenpotion+1
    print("You take both the potions and proceed through the dungeon. ")
  else:
    print("You leave the potions there and progress into the next room. ")
  return (greenpotion)

def PotionRoom():
  print("")
  print("You take the right path and enter the next room. There you find ")
  print("a RED POTION and a GREEN POTION.")
  print("You can try to identify them(1), take them(2) or leave them there ")
  analyze=input("and progress(3) in the dungeon ")
  if analyze==str(1):
    IdentifyPotion()
    TakePotion()
  elif analyze==str(2):
    TakePotion()
  elif analyze==str(3):
    print("You leave the potions there and progress into the next room.")
  return (playerpf)

#SWORDROOM()
def SwordRoom():
  print("")
  print("As you advance in the next room, you find a sword. ")
  print("You recognize it as the CURSED BLACKSWORD: it gives you +1 STR but you suffer double damage. ")
  print("If purified, the negative effect will be removed, while the positive one will remain")
  print("You can try to purify it(1), take it(2) or ")
  swordtaken=input("leave it there(3) ")
  if swordtaken==str(1):
    PurifySword()
  elif swordtaken==str(2):
    playersword==True
    print("You take the sword and proceed through the dungeon")
    for x in range(1):
      if playersword==True:
        playerstr==playerstr+1
  else:
     print("You leave the sword there and progress into the next room.")
  for x in range(1):
    if playersword==True:
      playerstr==playerstr+1
    if swordiscursed==True and playersword==True:
      damage==damage*2
  return(playerpf)

def PurifySword():
  print("You use your WIZARDRY to try to purify the sword.")
  if WizardryRoll()>7:
    print("You manage to purify it")
    swordiscursed==False
  else:
    print("Your power isn't enough to purify the sword. ")
  TakeSword()
  return(playerpf)

def TakeSword():
  print("Do you take the sword(1) or leave it ")
  swordtaken=input("there(2)?" )
  if swordtaken==str(1):
    playersword==True
    print("You take the sword and proceed through the dungeon")
    for x in range(1):
      if playersword==True:
        playerstr==playerstr+1
  else: 
    print("You leave the sword there and progress into the next room. ")
  for x in range(1):
    if playersword==True:
      playerstr==playerstr+1
    if swordiscursed==True and playersword==True:
      damage==damage*2
  return(playerpf)

#GOBLINROOM()
def GoblinRoom():
  print("")
  print("As you proceed, a nasty goblin ambushes you!")
  print("You can fight him(1) or flee(2). If you flee you will suffer" )
  goblinfight=input("some damage. ")
  if goblinfight==str(1):
    GoblinFight()
  else:
    fleedamage=((random.choice(d6))*damage)
    print("You run away from the goblin, but you suffer " + str(damage) + " points of damage ")
    print("from his attack. ")
    playerpf==playerpf-fleedamage
    print("")
    print("After you've escaped the goblin ambush, you continue your quest in the next room. ")

def GoblinFight():
  damage=1
  goblinpf=2
  while goblinpf>0:
    goblinroll=GoblinRoll()
    yourroll=StrenghtRoll()
    if yourroll>goblinroll:
      goblinpf=goblinpf-1
      print("You strike the goblin! ")
    elif yourroll==goblinroll:
      print("As the goblin deflect your hit, your weapons clashes together in a cloud of sparks! ")
    else:
      playerpf==playerpf-damage
      print("The goblin lands a clean hit on you! You lose " + str(damage) + " HP")
  else:
    print(str(playername) + ", you killed the goblin! You find a TORCH and a HEALING POTION. ")
    redpotion==redpotion+1
    torch==torch+1

#FUNCTION PROGRESSION
print("")
print("After a long journey, you finally entered the Dragon Dungeon. The place is a dark, cold cave.")
print("You see two path in front of you.")
playerpath= input("Choose if you want to go to the right(1) or to the left(2)")
if playerpath ==str(1):
  PotionRoom()
else:
  SwordRoom()
GoblinRoom()






