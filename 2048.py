import random,time,sys,os
WINDOWS = os.name=='nt'

import getkey

keys = getkey.keys
getkey = getkey.getkey

def clear():
  print(reset)
  os.system('clear' if os.name!='nt' else 'cls')
UP='up' if WINDOWS else keys.UP
DOWN='down' if WINDOWS else keys.DOWN
RIGHT='right' if WINDOWS else keys.RIGHT
LEFT='left' if WINDOWS else keys.LEFT

score=0
reset='\033[0m'
#WORKSSSSSSSSSSSSSSSSSS YESSSSSSSSSSSSS
board='''
┌────────────┬────────────┬────────────┬────────────┐
│            │            │            │            │
│    -0--    │    -1--    │    -2--    │    -3--    │
│            │            │            │            │
├────────────┼────────────┼────────────┼────────────┤
│            │            │            │            │
│    -4--    │    -5--    │    -6--    │    -7--    │
│            │            │            │            │
├────────────┼────────────┼────────────┼────────────┤
│            │            │            │            │
│    -8--    │    -9--    │    -a--    │    -b--    │
│            │            │            │            │
├────────────┼────────────┼────────────┼────────────┤
│            │            │            │            │
│    -c--    │    -d--    │    -e--    │    -f--    │
│            │            │            │            │
└────────────┴────────────┴────────────┴────────────┘
'''

real = [
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]
]
#pyinstaller -F --add-data "scoring/*.txt;scoring/" 2048.py
#SCORE SAVING

def file_name(name=""):
  try:
      base_path = sys._MEIPASS # PyInstaller creates a temp folder and stores path in _MEIPASS
  except Exception:
      base_path = os.path.abspath(".")
  return os.path.join(base_path, name)

highscore = 0

with open(file_name('scoring/2048scores.txt'),'r') as k:
  highscore = int(k.read())

newhigh = False

def save():
  global newhigh,highscore
  newhigh = False
  with open(file_name('scoring/2048scores.txt'), 'r') as h:
    oldscore = int(h.read())
  
  if oldscore < score:
    highscore = score
    newhigh = True
    with open(file_name('scoring/2048scores.txt'),'w') as sam:
      sam.write(str(score))



def printboard():
  for i in board:
    if i.isalnum():
      i = int(i,16)
      spot = real[i//4][i%4]
      print('    ' if spot==0 else dolro.get(spot,'')+f'{spot:^4}'+reset,end = '')
    elif i=='-':
      pass
    else:
      print(i,end = '')
  
      

spots={
  124:13,138:3,152:3,166:23, #Top
  358:1,372:0,386:0,400:2, #Lower
  590:1,604:0,618:0,632:2, #Lower
  822:14,836:4,850:4,864:24  #Bottom
}


dolro={
  2:'\033[38;5;1m',
  4:'\033[38;5;2m',
  8:'\033[38;5;3m',
  16:'\033[38;5;4m',
  32:'\033[38;5;5m',
  64:'\033[38;5;6m',
  128:'\033[38;5;7m',
  256:'\033[38;5;8m',
  512:'\033[38;5;9m',
  1028:'\033[38;5;10m'
}
def eq(other, thing = real):
  '''Returns other == real'''
  for i in range(16): 
    if other[i//4][i%4] != thing[i//4][i%4]: return False
  return True

def alive2(): #returns True if any possible move
  if alive(): return True
  for i in ['up','down','left','right']:
    if not move(i,False): #move will return whether that move results in the same board
      return True
  return False
  
  
def alive(): #revamped, need to add actual death detection
  for i in real:
    for j in i:
      if j==0: return True
  return False


def startboard(start = False): #revamped
  global real
  yuiop=random.choice([1,2,1]) if not start else 2
  
  
  for _ in range(yuiop):
    if not alive():
      continue
    while True:
      i = random.randint(0,15)
      if real[i//4][i%4]==0:
        real[i//4][i%4]=random.choice([2,4,2,2,4])
        break



#REVAMP OF MOVE SYSTEM:
#IF GOING RIGHT: START FROM RIGHT SIDE AND MOVE ALL PIECES RIGHT, IF A TILE MERGES THAT TILE CANT BE MERGED WITH IN THE SAME MOVE AGAIN!!!!!!!!!!!!
#FOR UP/DOWN MAKE A ROW OUT OF WHART YOU NEED TO MOVE AND PLACE IT ACCORDINGLY???



def move(dir, update = True):
  if dir == 'hi': return
  global board,real,score
  
  real2,real3 = [[],[],[],[]],[[],[],[],[]]
  for ind,i in enumerate(real):
    real2[ind] = i.copy()
    real3[ind] = i.copy()
  
  
  #start moving
  for ind,row in enumerate(real):
    cantagain = []
    
    if dir in ['up','down']: #make a list to do if up or down
      row = [E[ind] for E in real]

    if dir in ['right','down']:
      row = row[::-1] #flip if right OR down, special for down?
    
    for num,spot in enumerate(row):
      if spot == 0: #dont do anything for empty spaces
        continue
      else: #for actual nums:
        while num!=0: #while we arent in the first space move shit
          num-=1
          if row[num] == 0:
            row[num] = spot #move the number
            row[num + 1] = 0  #delete old number
          elif row[num] == spot:
            if num in cantagain:
              break
            row[num] = spot*2 #combine number (*2)
            if update:
              score += spot*2 #add to score
              save()
            row[num + 1] = 0 #delete old number
            cantagain.append(num) #add to spots you cant combine again
            break
          else:
            break
    if dir in ['right','left']:
      real3[ind] = row if dir == 'left' else row[::-1] #put flipped row if the direction is right
    else:
      if dir=='down': #ind
        row = row[::-1]
      for cur,_ in enumerate(real):
        real3[cur][ind] = row[cur]
          
  if not update:
    return eq(real2,real3)
  
  real = real3
  
  if not eq(real2, real):
    startboard()




clear()

print("Welcome to 2048")
print("If anything weird happens visually press 'c'!")
print("\nHigh score: \033[38;5;206m"+str(highscore))
input("\n\033[38;5;57m[Enter to continue]")

clear()
startboard(True)

while True:
  print("\033[H",end="")
  printboard()
  print(f"{'Score: '+str(score):^53}")
  print("" if not newhigh else f"\n\033[38;5;74m{'New highscore!':^54}"+reset)
  if alive2():
    keyz=getkey()
    move('up' if keyz in ['w',UP] else 'down' if keyz in ['s',DOWN] else 'right' if keyz in ['d',RIGHT] else 'left' if keyz in ['a',LEFT] else 'hi')
    if keyz in ['c','q']:
      os.system('clear')
  else:
    clear()
    print(f"{'You lost!':^53}\n{'Final Score: '+str(score) :^53}\n{'Highscore: '+str(highscore):^53}")
    printboard()
    time.sleep(1)
    print("Would you like to retry?\n[type yes/no]")
    thi = input("> ")
    if 'y' in thi:
      real = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      startboard(True)
      score = 0
      clear()
    else:
      sys.exit()