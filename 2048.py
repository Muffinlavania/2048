import random,time,sys,os,json,datetime
from datetime import date

WINDOWS = os.name=='nt'




#EVERYTHINGS DONE!!!
#JUST NEEDTO TEST IF QUEST REFRESH FR WORKS, AND UST PLAY IT A BUNCH


#TODO
#MAKE THE SHOP (DONE)
#MAKE THE NAME CUSTOMIZATION USABLE (done)
#MAKE QUESTS (DONE)
#GAMBLING MODE (LOWKEY MID??? DONT DO IT???)

print('\033[?25l')

#MAKE THE BORDERS (done)
#MAKE BABY LOVE SECRETS (PINK IS ONLYHERS, name it coquette) (done)
#alternate board - changes num colors into background (done)

#colors for the board
bdict = {
  'R': '\033[0m',
  'P': '\033[48;5;5m ',
  'Q': '\033[48;5;93m ',
  'W': '\033[48;5;13m ',
  'J': '\033[48;5;13m ',
  '‗': '\033[38;5;5m─',
  '‖': '\033[38;5;5m│',
  'ˍ': '\033[38;5;13m─',
  'M': '\033[48;5;88m ',
  'm': '\033[48;5;236m\033[38;5;88m─',
  'L': '\033[48;5;52m ',
  'F': '\033[48;5;166m ',
  'l': '\033[48;5;172m ',
  'B': '\033[48;5;236m ',
  'w': '\033[48;5;19m ',
  '#': '\033[48;5;21m ',
  '!': '\033[48;5;33m ',
  'S': '\033[48;5;216m ',
  's': '\033[48;5;167m ',
  '@': '\033[48;5;178m ',
  '$': '\033[48;5;62m ',
  '%': '\033[48;5;133m ',
  'G': '\033[48;5;220m ',
  'g': '\033[48;5;214m ',
  'Z': '\033[48;5;232m ',
  'X': '\033[48;5;40m ',
  'x': '\033[48;5;94m ',
  'V': '\033[48;5;34m ',
  'N': '\033[48;5;245m ',
  'n': '\033[48;5;247m ',
  'v': '\033[48;5;242m ',
  'T': '\033[48;5;20m ',
  'Y': '\033[48;5;231m ',
  'y': '\033[48;5;195m ',
}

import getkey

keys = getkey.keys
getkey = getkey.getkey

def clear():
  print(reset)
  os.system('clear' if os.name!='nt' else 'cls')
def clearline(amo=1):
  print(reset,end='')
  sys.stdout.write(f'\x1b[1A\x1b[2K'*amo)
UP='up' if WINDOWS else keys.UP
DOWN='down' if WINDOWS else keys.DOWN
RIGHT='right' if WINDOWS else keys.RIGHT
LEFT='left' if WINDOWS else keys.LEFT
BACKSPACE,ENTER,TAB='backspace' if WINDOWS else keys.BACKSPACE,'enter' if WINDOWS else keys.ENTER,'tab' if WINDOWS else keys.TAB

score=2
ccs = 0
reset='\033[0m'

boards = {
  'Default':'''
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
''',
  'heartful':'''
JJJJ‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗JJJJ
JJ        PPP PPP         ‖         PPP PPP        JJ
J    -0--PPPPPPPPP-1--    ‖    -2--PPPPPPPPP-3--    J
‖         PPPPPPP         ‖         PPPPPPP         ‖
‖ˍˍˍˍˍˍˍˍˍˍˍPPPˍˍˍˍˍˍˍˍˍˍˍ‖ˍˍˍˍˍˍˍˍˍˍˍPPPˍˍˍˍˍˍˍˍˍˍˍ‖
‖            ‖    WWWW    ‖    WWWW    ‖            ‖
‖    -4--    ‖   W-5--W   ‖   W-6--W   ‖    -7--    ‖
‖            ‖   W     PPP PPP     W   ‖            ‖
‖ˍˍˍˍˍˍˍˍˍˍˍˍ‖ˍˍˍˍWWWWPPPPPPPPPWWWWˍˍˍˍ‖ˍˍˍˍˍˍˍˍˍˍˍˍ‖
‖            ‖         PPPPPPP         ‖            ‖
‖    -8--    ‖    -9--W  PPP  W-a--    ‖    -b--    ‖
‖            ‖       W    ‖    WWW     ‖            ‖
‖ˍˍˍˍˍˍˍˍˍˍˍˍ‖ˍˍˍˍˍˍˍˍˍˍˍˍ‖ˍˍˍˍˍˍˍˍˍˍˍˍ‖ˍˍˍˍˍˍˍˍˍˍˍˍ‖
‖         PPP PPP         ‖         PPP PPP         ‖
J    -c--PPPPPPPPP-d--    ‖    -e--PPPPPPPPP-f--    J
JJ        PPPPPPP         ‖         PPPPPPP        JJ
JJJJ‗‗‗‗‗‗‗‗PPP‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗PPP‗‗‗‗‗‗‗‗JJJJ
''',
  'hellscape':'''
lllllllllFFFllllllllllllllFllllllllllllllFFFFFlllllFF
llllFFFFFFBFFllllFFFFFFFlllllFFFFFFFlllFFFBBBFFFFlllF
lFFFF-0--BBBFFFFFF-1--BFFlllFFB-2--FFFFFBBBB-3--FlllF
FFBBBBBBBBBBBBBBBBBBBBBBFFlFFBBBBBBBBBBBBBBBBBBBFFlll
lFmmmmmmmmmmmmmmmmmmmmmLLLLLLLmmmmmmmmmmmmmmmmmmmFFll
lFFBBBBBBBBBBBBBBBBBBBLLMMMMMLLBBBBBBBBBBBBBBBBBBBFFl
llFBB-4--BBBBBBBBB-5--LLMMMMMLL-6--BBBBBBBBB-7--BBBFF
llFBBBBBBBBBBBBBBBBBBBLMMMMMMMLBBBBBBBBBBBBBBBBBBBBBF
llFFmmmmmmmmmmmmmmmmmmLMMMMMMMLmmmmmmmmmmmmmmmmmmmFFl
FllFBBBBBBBBBBBBBBBBBBLMMMMMMMLBBBBBBBBBBBBBBBBBBFFll
FllFB-8--BBBBBBBBB-9--LLMMMMMLL-a--BBBBBBBBB-b--BFllF
llFFBBBBBBBBBBBBBBBBBBLLMMMMMLLBBBBBBBBBBBBBBBBBFFllF
lFFmmmmmmmmmmmmmmmmmmmmLLLLLLLmmmmmmmmmmmmmmmmmmFllFF
lFBBBBBBBBBBBBBBBBBBBBBBFFlFFBBBBBBBBBBBBBBBBBBBFFllF
FFFBB-c--BBFFFFFFF-d--BFFlllFFB-e--FFFFFFFBB-f--BFFll
llFFFFFFFBFFlllllFFFFFFFlllllFFFFFFFlllllFFFBBFFFFlll
llllllllFFFlllFlllllllFlllFlllllllllllFFlllFFFFlllllF
''',
  'oceanfront':'''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$
$$$$$-0--$$$$$%%%%-1--%%%%%%%%%-2--%%%%$$$$$-3--$$$$$
$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%$$$$$$$$$$
$$$$$$$%%%%%%%%%%%%%sssssssssssss%%%%%%%%%%%%%$$$$$$$
$$$$%%%%%%%%%%%%sssssssssssssssssssss%%%%%%%%%%%%$$$$
$$%%%-4--%%%ssssss-5--sssssssss-6--ssssss%%%-7--%%%$$
%%%%%%%%%sssssssssssFFFFFFFFFFFFFsssssssssss%%%%%%%%%
%%%%%%ssssssssssssFFFFFFFFFFFFFFFFFssssssssssss%%%%%%
%%%%sssssssssssFFFFFFFF@@@@@@@FFFFFFFFsssssssssss%%%%
%%%ss-8--sssFFFFFF-9--@@@@@@@@@-a--FFFFFFsss-b--ss%%%
!!!!!!!!!!!!!!!!!!!!#############!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!###################################!!!!!!!!!
SS!!#############################################!!SS
SSSS#-c--####wwwww-d--wwwwwwwww-e--wwwww####-f--#SSSS
SSSSSS###wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww###SSSSSS
SSSSSSSwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwSSSSSSS
''',
  'brilliance':'''
llgggggggggggggggggggggggglggggggggggggggggggggggggll
lG           gG           gG           gG           l
gG   -0--G   gG   -1--G   gG   -2--G   gG   -3--G   g
gG           gG           gG           gG           g
ggggggggggggglggggggggggggggggggggggggglggggggggggggg
gG           gG           gG           gG           g
gG   -4--G   gG   -5--G   gG   -6--G   gG   -7--G   g
gG           gG           lG           gG           g
lgggggggggggggggggggggggglllggggggggggggggggggggggggl
gG           gG           lG           gG           g
gG   -8--G   gG   -9--G   gG   -a--G   gG   -b--G   g
gG           gG           gG           gG           g
ggggggggggggglggggggggggggggggggggggggglggggggggggggg
gG           gG           gG           gG           g
gG   -c--G   gG   -d--G   gG   -e--G   gG   -f--G   g
lG           gG           gG           gG           l
llgggggggggggggggggggggggglggggggggggggggggggggggggll
''',
  'block game':'''
YYYyYYYYYYYYYYYYyYYYYYYYYYYYYyYYYYYYYYYYYYyYYYYYYYYYY
YYyYyYYYyYYYYYYyYyYYYyYYYYYYyYyYYYyYYYYYYyYyYYYyYYYYY
YYYYY-0--yYYYYYYYY-1--yYYYYYYYY-2--yYYYYYYYY-3--yYYYY
YYYYYYYYyYYYYYYYYYYYYyYYYYYYYYYYYYyYYYYYYYYYYYYyYYYYY
TTTTT#TTTTTTTTTTTT#TTTTTTTTTTTT#TTTTTTTTTTTT#TTTTTTTT
TTTT#TTTTTT#TTTTT#TTTTTT#TTTTT#TTTTTT#TTTTT#TTTTTT#TT
TTT#T-4--T#TTTTT#T-5--T#TTTTT#T-6--T#TTTTT#T-7--T#TTT
TTTTTTTTT#TTTTTTTTTTTT#TTTTTTTTTTTT#TTTTTTTTTTTT#TTTT
XXXXXXXXXXXXXVXXXXXXXXXXXXVXXXXXXXXXXXXVXXXXXXXXXXXXX
XxxXxxXXxXXxXVxxXxxXXxXXxXVxxXxxXXxXXxXVxxXxxXXxXXxXX
xxxxx-8--Xxxxxxxxx-9--Xxxxxxxxx-a--Xxxxxxxxx-b--Xxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
vvNNNvvvNNNvvvvNNNvvvNNNvvvvNNNvvvNNNvvvvNNNvvvNNNvvN
Nnnnv-c--nnvNNnnnv-d--nnvNNnnnv-e--nnvNNnnnv-f--nnvNn
NNNvvvNNNNvNNNNNvvvNNNNvNNNNNvvvNNNNvNNNNNvvvNNNNvNNN
NNvvNnnnNvvnnNNvvNnnnNvvnnNNvvNnnnNvvnnNNvvNnnnNvvnnN
''',
  'alternate':'''
Z                                                    
Z_           Z=           Z+           Z[           Z
Z_   -0--_   Z=   -1--=   Z+   -2--+   Z[   -3--[   Z
Z_           Z=           Z+           Z[           Z
Z                                                    
Z{           Z]           Z}           Z;           Z
Z{   -4--{   Z]   -5--]   Z}   -6--}   Z;   -7--;   Z
Z{           Z]           Z}           Z;           Z
Z                                                    
Z:           Z,           Z<           Z.           Z
Z:   -8--:   Z,   -9--,   Z<   -a--<   Z.   -b--.   Z
Z:           Z,           Z<           Z.           Z
Z                                                    
Z>           Z/           Z?           Z`           Z
Z>   -c-->   Z/   -d--/   Z?   -e--?   Z`   -f--`   Z
Z>           Z/           Z?           Z`           Z
Z                                                    R
'''
}

board = boards['Default']

real = [
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]
]
#pyinstaller -F 2048.py

#item descriptions!!!
#posunlocks = ['default','pastel','classic','cinna','coquette','sunset']
view_key = {'1':'f"   {D[2]}2   {D[4]}4   {D[8]}8   {D[16]}16   {D[32]}32\033[0m   "','2':"f'   {D[64]}64  {D[128]}128    {D[256]}256  {D[512]}512\033[0m   '",'3':'f"        {D[1024]}1024 {D[2048]}2048\033[0m        "','#':'\033[01m','@':'\033[38;5;127m'}
descs = {'default':'''
         Default         
                         
1
2
3
                         
#Just the default theme...''',
'pastel':'''
          Pastel         
                         
1
2
3
                         
#A soft, light color theme''',
'classic':'''
         Classic         
                         
1
2
3
                         
   #The classic's color.  ''',
'cinna':'''
       Cinnamoroll       
                         
1
2
3
                         
#blue white and pink!!!!!!''',
'coquette':'''
      ୨ৎ PINKKKK ୨ৎ      
                         
1
2
3
                         
#@COQUETTEEEEEEEEEEEEEEEEEE
#Only for the cutest. :) ♡''',
'sunset':'''
          Sunset         
                         
1
2
3
                         
#The layers of a sunset...
  #A colorful melody!!!!  ''',
"ccs":"""
       Cinna coins       
     ⊂⎼⎼(｡● ⤙ ●｡)⎼⎼⊃     
         ૮     ১         
         (") (")         
    Use to buy boxes!    """,
'Default':['Default theme','The normal board, kinda bland.'],
'heartful':['Heartful','tip: press "b" ingame to toggle the bow!'],
'hellscape':['Hellscape','All hell breaks loose.'],
'oceanfront':['Oceanfront','A sunset fit for a king.'],
'brilliance':['brilliance','Shiny, shimmering gold.'],
'block game':['"Block Game"','Based off of a game with blocks.'],
'alternate':['Alternate theme','Turns your number theme into full box colors!']
}
#ꕀ,୨ৎ
def theme_view(theme):
  global achieve
  isnum = theme not in unlocks_board
  clear()
  if isnum:
    if theme not in unlocks_num and theme != 'ccs': theme = 'default'
    if theme!='ccs':
      D = num_theme(theme)
    for i in descs[theme]:
      print(i if i not in view_key else eval(view_key[i]) if i in '123' else view_key[i],end='')
    print()
  else:
    print(f"{descs[theme][0]:^53}")
    printboard(boards[theme], [[2,4,8,16],[32,64,128,256],[512,1024,2048,4],[2,4,8,16]])
    print(f"{descs[theme][1]:^53}")
  sys.stdout.flush()
  time.sleep(1)
  print('\n\n\033[0m[Enter to exit]\n['+(("\033[38;5;123m'e' to equip this theme!" if theme not in achieve["selected"] else "\033[38;5;33mtheme already equipped!") if theme!='ccs' else '')+'\033[0m]')
  inp = getkey().lower()
  if inp == 'e' and theme!='ccs':
    achieve['selected'][0 if isnum else 1] = theme
    clear()
    save()
    input(theme.title()+(" number" if isnum else ' board')+" theme equipped!\n[Enter to exit]")
    reload()
  clear()


terminalcolours = ""
for c in range(255):
  terminalcolours += '\033[38;5;%dm %03d \033[0m' % (c, c)
  if (((c + 1) % 6)) == 4:
    terminalcolours+='\033[0m \n'
  if (((c + 9)/6) % 6) == 4:
    terminalcolours += '\033[0m \n'
terminalcolours += '\n\n'

def name_cust():
  global achieve
  clear()
  T=False
  ye,final = '',''
  print("Name customization:\n"+(terminalcolours if not T else '')+"Please type the number you want your name to be!\nHit \033[38;5;175menter\033[0m when you are done.\n\033[38;5;146mc\033[0m to toggle color palette, \033[38;5;217mx\033[0m to leave (no change)")
  while ye not in ['x',ENTER]:
    print(f"\nOld color: {achieve['ncolor']}\nNew name preview: \033[38;5;{7 if final=='' else 254 if int(final)>254 else final}m{name}\033[0m\n\nNew number > "+final)
    ye = getkey()
    ye = ye.lower() if ye not in [ENTER,BACKSPACE] else ye
    if ye==BACKSPACE:
      final = final[0:-1]
    
    if ye.isdigit() and len(final)<=3:
      final += ye
    
    if ye=='c':
      T = not T
      clear()
      print("Name customization:\n"+(terminalcolours if not T else '')+"Please type the number you want your name to be!\nHit \033[38;5;175menter\033[0m when you are done.\n\033[38;5;146mc\033[0m to toggle color palette, \033[38;5;217mx\033[0m to leave (no change)")


    if ye==ENTER:
      if final.isdigit() and int(final)<255:
        clear()
        achieve['ncolor'] = int(final)
        save()
        input(f"New name color, \033[38;5;{final}m{final}\033[0m, saved!\n[Enter to continue]")
      else:
        input(f"Name color not changed due to invaid number, still \033[38;5;{achieve['ncolor']}m{achieve['ncolor']}\033[0m.\n[Enter to continue]")
    if ye!='c':
      clearline(5)


def inv(): #view inventory here
  addccs(0) #usually for refreshing quests and you already have the needed number of ccs
  nthemes = [i for i in unlocks_num if i in achieve['unlocks']]
  bthemes = [i for i in unlocks_board if i in achieve['unlocks']]
  maxer = max(len(nthemes),len(bthemes))
  
  Co = lambda e: achieve['unlocks'].count(e)

  inp = ''
  while inp!='x':
    thestr = ''
    thestr += f"{'Inventory  (CCs - '+str(ccs)+')':^52}" + '\n'
    cccolor = '\033[38;5;34m'
    thestr += "\n\033[38;5;51mQuests:\033[0m\n"
    for i in achieve['quests'][1]:
      thestr += f"{i+'...':<15}{cccolor}{f'Reward: {quests[i][3]}ccs':<20}{reset}{quests[i][2]} ["+('\033[38;5;28mCompleted!' if achieve['quests'][1][i] else  f'{ccs}/{quests[i][1]}' if quests[i][0]=='cc' else '\033[38;5;124mIn progress')+"\033[0m]\n"
    thestr += f"\n\nNUMBER THEMES{'BOARD THEMES':>39}\n"
    for i in range(maxer):
      if i<len(bthemes):
        thestr += ('\033[0m' if bthemes[i] not in achieve['selected'] else '\033[38;5;40m') + f'{f"{chr(i+97)}) {bthemes[i]}[{Co(bthemes[i])}]":>52}\r' + ('' if i<len(nthemes) else '\n')
      if i<len(nthemes):
        thestr += (f'\033[{"38;5;207" if nthemes[i]=="coquette" else "0"}m' if nthemes[i] not in achieve['selected'] else '\033[38;5;40m') + f"{i+1}) {nthemes[i]}[{Co(nthemes[i])}]\n"
    clear()
    print(thestr)
    if 'name_cust' in achieve['unlocks']:
      print('\n'+(f'\033[38;5;{achieve["ncolor"]}m{"z) Name customization":^52}'))
    print(f"\033[38;5;69m{'s) Cinna Coins':^52}\033[0m")
    print("\033[0m\n('x' to exit, hit num/letter to view/equip themes)")
    inp = getkey().lower()
    if inp.isdigit():
      if int(inp)>len(nthemes): continue
      theme_view(nthemes[int(inp)-1])
    elif inp=='z':
      if 'name_cust' in achieve['unlocks']:
        name_cust()
    elif inp=='s':
      theme_view("ccs")
    elif inp.isalnum():
      if inp == 'z': name_cust()
      if int(inp,36)-9>len(bthemes): continue
      theme_view(bthemes[int(inp,36)-10])
  
  clear()


#SCORE SAVING
def shigh(score):
  global achieve
  achieve['high'] = score
def high():
  return achieve['high']

achieve = {'ncolor':7, 'high':0,'ccs':0,'unlocks':['default','Default'],'selected':['default','Default']}
name = ""

#cc = total ccs, end = at end of round, high = daily high, 
#quest type (cc/end/high), quest requirement, quest desc, quest reward
quests = {
  'Hoarder': ['cc', 1000, 'Have 1000ccs at once', 400],
  'Accumulator': ['cc', 500, "Have 500ccs at once", 200],
  'Collector': ['cc', 400, 'Have 400ccs at once', 100],
  'Baby Love': ['end', 2222, 'End with 2222 score exactly', 2000],
  'Baby':['end', 222, 'End with 222 score exactly', 500],
  'Perfection': ['end', 1002, 'End with 1002 score exactly', 1000],
  'Winner': ['high', 5000, 'Get a score over 5000', 1000],
  'Gamer': ['high', 2500, 'Get a score over 2500', 100],
  'Crazy': ['high', 2222, 'Get a score over 2222', 100]
}
#quests become a random choice from each of these list (of each category)
Qs = [['Hoarder','Accumulator','Collector'],['Baby Love','Baby','Perfection'],["Winner",'Gamer','Crazy']]

def addccs(amo = 0): #adds ccs and checks for quests
  global ccs, achieve
  ccs += amo
  for i in achieve['quests'][1]:
    if not achieve['quests'][1][i]:
      if quests[i][0] == 'cc' and ccs>=quests[i][1]:
        achieve['quests'][1][i] = True
        addccs(quests[i][3])
        save()

def checkquests():
  global achieve
  if achieve['quests'][0]!=str(date.today()):
    achieve['quests'] = [str(date.today()), {random.choice(i):False for i in Qs}]
    save()

def load():
  global achieve,ccs
  with open("2048scores.json",'r') as q:
    achieve = json.load(q)[name]
  if len(achieve) < 6: #if its an old safe data thing, grab the high score but reset everything else
    achieve = {'ncolor':7, 'high':achieve.get('high',0),'ccs':0,'unlocks':['default','Default'],'selected':['default','Default'],'quests':['1',[]]}
    save()
  ccs = achieve['ccs']
  checkquests()
  


def save():
  global achieve
  achieve['ccs'] = ccs
  with open('2048scores.json','r') as k:
    theone = json.load(k)
  theone[name] = achieve
  with open('2048scores.json','w') as q:
    q.write(json.dumps(theone))



clear()
if '2048scores.json' not in os.listdir():
  print("hiiiiiiii sammmmmmmmmmm")
  print("can you tell me your username pls?")
  name = input(">\033[38;5;207m ")
  clear()
  input("HI "+name.upper()+"!!!!\n[Enter to continue]")
  with open('2048scores.json','w') as k:
    k.write(json.dumps({}))
  save()
else:
  print(f"Welcome back \033[38;5;207m{random.choice(['cutie','sam','adorableness','cuteness','sam','sammmm','SAMM','MLL','my love','babe','babyyyy','perfection'])}\033[0m!!!\n\nWhich number account do you want to load?\n\033[38;5;20m [Say 'n' for a new user!!!]\033[0m")
  with open('2048scores.json','r') as h:
    names = list(json.load(h).keys())
  print(', '.join([f"\033[38;5;121m{ind+1}\033[0m) {i}" for ind,i in enumerate(names)]))
  while (an:=input(">\033[38;5;121m "))!='n' and not (an.isdigit() and 0 < int(an) <= len(names)):
    clearline()
  clear()
  if an=='n':
    print("Enter the name of your new user!\nCannot be in: \033[38;5;121m"+','.join(names))
    while (an:=input("\033[0m>\033[38;5;121m ")) in names:
      clearline()
    clear()
    name = an
    input("HI "+name.upper()+"!!!!\n[Enter to continue]")
    save()
  else:
    name = names[int(an)-1]
    input("HI "+name.upper()+"!!!!\n[Enter to continue]")
clear()
load()
BABY = name.lower() == 'srnkt02'
if BABY:
  if 'coquette' not in achieve['unlocks']:
    achieve['unlocks'] += ['coquette']
    save()


newhigh = False
thres = 1000 #used for adding ccs
def save2():
  global newhigh,ccs,thres,achieve
  newhigh = False
  with open('2048scores.json', 'r') as h:
    oldscore = json.load(h)[name]['high']
  
  if score>thres:
    addccs(10 * thres//1000)
    thres+=1000
    save()
  
  #QUESTS CHECKING (except the endones)
  checkquests()
  for i in achieve['quests'][1]:
    if not achieve['quests'][1][i]:
      if quests[i][0] == 'high' and score>=quests[i][1]:
        achieve['quests'][1][i] = True
        addccs(quests[i][3])
        save()
  

  if oldscore < score:
    shigh(score)
    newhigh = True
    save()



def printboard(board2 = '', spots = ''):
  board2 = board if board2 == '' else board2
  real2 = real if spots == '' else spots

  finale = ""
  for i in board2:
    if i in '0123456789abcdef':
      i = int(i,16)
      spot = real2[i//4][i%4]   #'=' is only in alternate (i hope)
      finale += ('    ' if spot==0 else f'{dolro.get(spot,"") if "=" not in board2 else ""}{spot:^4}') + '\033[0m'
    elif i in bdict.keys():
      finale += bdict.get(i,i) + ('\033[0m' if i not in 'GZ' else '')
    elif i in '_=+[{]};:,<.>/?`':
      seled = {'_': 0, '=': 1, '+': 2, '[': 3, '{': 4, ']': 5, '}': 6, ';': 7, ':': 8, ',': 9, '<': 10, '.': 11, '>': 12, '/': 13, '?': 14, '`':15}[i]
      spot = real2[seled//4][seled%4]
      finale += '\033[0m ' if spot==0 else f'{dolro.get(spot,"").replace("[38","[48")} '
    else:
      finale += i if i!='-' else ''
  print(finale)


spots={
  124:13,138:3,152:3,166:23, #Top
  358:1,372:0,386:0,400:2, #Lower
  590:1,604:0,618:0,632:2, #Lower
  822:14,836:4,850:4,864:24  #Bottom
}
dolro = {}
unlocks_num = ['default','pastel','classic','cinna','coquette','sunset']
unlocks_board = ['Default','heartful','hellscape','oceanfront','brilliance','block game','alternate']#heartless?

#------ box animation, first 3 = opening box, last one use.split("???????????") and put the drop:^11 in between -------

stages = ['''\n\n\n\n\n       //_______________/\n      /BB/CCCCCCCCCCCCCCC/\n     /BBBB/CCCCCCCCCCCCCCC/\n    /BBBBBB/CCCCCCCCCCCCCCC/\n   /BBBBBBBB/_______________/\n   /BBBBBBBB/CCCCCCCCCCCCCCC/\n    /BBBBBB/CCCCCCCCCCCCCCC/\n     /BBBB/CCCCCCCCCCCCCCC/\n      /BB/CCCCCCCCCCCCCCC/\n       //_______________/''',
'''\n\n\n\n\n       //_______________/\n      /BB///CCCCCCCCCCCCC//\n     /BBBB/A//CCCCCCCCCCCCC//\n    /BBBBBB/AA//CCCCCCCCCCCCC//\n   /BBBBBBBB/___//___________//\n   /BBBBBBBB/CCCCCCCCCCCCCCC/\n    /BBBBBB/CCCCCCCCCCCCCCC/\n     /BBBB/CCCCCCCCCCCCCCC/\n      /BB/CCCCCCCCCCCCCCC/\n       //_______________/''',
'''\n\n\n\n\n       ////_____________/\n      /BB/A///CCCCCCCCCCC///\n     /BBBB/AAA///CCCCCCCCCCC///\n    /BBBBBB/AAAAA///CCCCCCCCCCC///\n   /BBBBBBBB/_______///________///\n   /BBBBBBBB/CCCCCCCCCCCCCCC/\n    /BBBBBB/CCCCCCCCCCCCCCC/\n     /BBBB/CCCCCCCCCCCCCCC/\n      /BB/CCCCCCCCCCCCCCC/\n       //_______________/''',
'''            /_______________/   \n           /CCCCCCCCCCCCCCC/    \n          /CCCCCCCCCCCCCCC/     \n         /CCCCCCCCCCCCCCC/      \n        /CCCCCCCCCCCCCCC/       \n       //_______________/       \n      /BB/AAAAAAAAAAAAAAA/      \n     /BBBB/AAAAAAAAAAAAAAA/     \n    /BBBBBB/AAAAAAAAAAAAAAA/    \n   /BBBBBBBB/_______________/   \n   /BBBBBBBB/CCCCCCCCCCCCCCC/   \n    /BBBBBB/CCCCCCCCCCCCCCC/    \n     /BBBB/CCCCCCCCCCCCCCC/     \n      /BB/CCCCCCCCCCCCCCC/      \n       //_______________/       ''',
'''\n            /_______________/   \n           /CCCCCCCCCCCCCCC/    \n         FFFFFFFFFFFFFFFFF/     \n        FFFFFFFFFFFFFFFFFFF     \n       FFFFFFFFFFFFFFFFFFFFFF   \n      FFF________________/FFFF  \n     FFFF/AAAAAAAAAAAAAAA/FFFFF \n     FFFFF/AAAAAAAAAAAAAAA/FFFF \n    /BFFFFF/AAAAAAAAAAAAAAA/FFF \n   /BBFFFFFF/_______________/FF \n   /BBBBFFFFFFFFFFFFFFFFFFFFFF  \n    /BBBBBFFFFFFFFFFFFFFFFFFF   \n     /BBBB/CFFFFFFFFFFFFCC/     ''',
'''\n       F               R\n     F                   R\n   F                       R\n  F                          R\n  F                          R\n  F                           R\n   F         P       F         R\n   F     _______________/F      R\n    F    /AAAAAAAAAAAAAAA/F      R \n    F     /AAAAAAAAAAAAAAA/F     R \n    /F     /AAAAAAAAAAAAAAA/F   R  \n   /BF      /______________/F   R \n   /BBF                        R    ''',
'''\n  F                             R\n F                               R\nF                                 R\nF                                 R\nF                                 R\nF                                 R\nF         P              F        R\n F       P                F      R\n  F      P   ??????????P  F     R\n  F      P                F     R\n   F      P              F     R\n   F      ///////////////F     R\n    F    /AAAAAAAAAAAAAAA/F   R ''',
'''\nF              P    F             R\nF            P        F           R\nF          P            F         R\nF        P                F       R\nF        P                F       R\nF        P                F       R\nF        P  ???????????P  F       R\nF        P                F       R\nF        P                F       R\nF        P                F       R\nF          P             F        R\nF            P         F          R\nF              P     F            R''']
B_dict = {
  '_':"\033[48;5;0m ",
  '/':"\033[48;5;0m ",
  'C':"\033[48;5;130m ",
  'B':"\033[48;5;8m ",
  'A':"\033[48;5;51m ",
  'F':"\033[48;5;13m ",
  'R':"\033[0m ",
  'P':"\033[48;5;1m ",
  '?':"\033[48;5;1m?",
}

#accentcolors for all the drops (FOR BOX ANIMATION), defaults to 7
accentcolors = {'default':8,'pastel':10,'classic':208,'cinna':69,'coquette':164,'sunset':3,'Default':0,'heartful':212,'hellscape':52,'oceanfront':167,'brilliance':214,'block game':2,'alternate':21}

def printbox(board):
  finale = ""
  for i in board:
    if i in B_dict.keys():
      finale += B_dict.get(i,i) + ('\033[0m' if i not in 'FP' else '')
    else:
      finale += ('\033[0m ' if i=='\n' else '')+ i
  return finale


def open_box(reward):
  global B_dict
  B_dict['P'] = f'\033[48;5;{accentcolors.get(reward,"7")}m '
  B_dict['?'] = f'\033[48;5;{accentcolors.get(reward,"7")}m?'
  final_reward = stages[-1][1:].split("???????????")
  final_reward.insert(1,B_dict['P'][:-1]+f"{reward:^11}")
  final_reward = "".join(final_reward)
  final_reward = printbox(final_reward)
  stages2 = [printbox(i) for i in stages]
  
  count = 0
  while count<3:
    print(stages2[count])
    print(f"[Press any key to open! (x{3-count})]")
    getkey()
    clear()
    count+=1
  clear()
  while count<len(stages2):
    print(stages2[count])
    time.sleep(1)
    clear()
    count+=1
  print(f"{B_dict['P'].replace('[48','[38')[:-1]}{'You got:':^35}\033[0m\n"+final_reward+"\033[0m\n[Press anykey to continue!]")
  getkey()

shoptxts = ['''
\033[01m          Shop          \033[0m
                        
\033[38;5;99m    Number Theme Box    \033[0m
\033[38;5;40m         100ccs         \033[0m
------------------------
`  |    Default     |  ` (0%)
@  |     Pastel     |  @ (40%)
#  |    Classic     |  # (40%)
=  |     Sunset     |  = (15%)
$  |   Cinnamoroll  |  $ (5%)'''+("\n    For baby love ~\n:) |    Coquette    | :) (ily)" if BABY else '')+"\n------------------------",
'''
\033[01m          Shop          \033[0m
                        
\033[38;5;99m    Board Themes Box    \033[0m
\033[38;5;40m         100ccs         \033[0m
------------------------
^  |    Default     |  ^ (0%)
_  |   Block Game   |  _ (30%)
{  |   Oceanfront   |  { (25%)
]  |   Brilliance   |  ] (20%)
*  |   Hellscaped   |  * (15%)
+  |   Alternate.   |  + (9%)
&  |    Heartful    |  & (1%)
------------------------
''','''
\033[01m          Shop          \033[0m
                        
\033[38;5;99m   Name Customization   \033[0m
\033[38;5;40m         100ccs         \033[0m
------------------------
   Change your name's   
      appearance!       
------------------------
''']
Slegend = {'`':'default','@':'pastel','#':'classic','$':'cinna','=':'sunset','^':'Default','&':"heartful",'*':"hellscape",'{':"oceanfront",']':"brilliance",'_':'block game','+':'alternate'}
pools = {0: {40:'pastel',80:'classic',95:'sunset',100:'cinna'}, 1: {30:'block game',55:'oceanfront',75:'brilliance',90:'hellscape',99:'alternate',100:'heartful'}}
def shop():
  global ccs, achieve
  clear()
  count,you = 0,''
  while you!='x':
    F = ''
    for i in shoptxts[count]:
      F += i if not i in Slegend else f"\033[48;5;{'46' if Slegend[i] in achieve['unlocks'] else '196'}m \033[0m"
    print(F)
    slashn = "\n"
    print(f'{slashn*(15-F.count(slashn))}     Your ccs:\033[38;5;40m{ccs:>4}\033[0m\n         Page {count+1}/3\n\033[38;5;9mx\033[0m-exit, \033[38;5;4ma/d\033[0m - switch, \033[38;5;28my\033[0m - buy')
    you = getkey()
    if you=='y':
      clear()
      print(f"Are you sure you want to buy: \033[38;5;99m{'Number Theme Box' if count==0 else 'Board Theme Box' if count==1 else 'Name Customization'}\033[0m\nFor: \033[38;5;40m100ccs\033[0m")
      print("(y to confirm)")
      if getkey()=='y':
        clear()
        if ccs<100 or (count==2 and 'name_cust' in achieve['unlocks']):
          input(f"{'You wish you could buy this!' if ccs<100 else 'Do you enjoy ripping yourself off, this is already unlocked???'}\n\n[Enter to exit]")
          clear()
          return
        ccs-=100
        print("Purchase confirmed! (\033[38;5;1m-100ccs\033[0m)")
        if count==2:
          achieve['unlocks'].append('name_cust')
          save()
          input("\033[38;5;31mTo customize your name, go into your inventory!\033[0m\nThere you can edit your name color, and it will appear below every game!\n\n[Enter to exit]")
        else:
          dropn = random.randrange(0,100)
          reward = ''
          for i in list(pools[count]):
            if i>dropn:
              reward = pools[count][i]
              break
          achieve['unlocks'].append(reward)
          save()
          input("[Enter to open your box!]")
          clear()
          open_box(reward)
        clear()
        return
    if you in ['a','d',LEFT,RIGHT]:
      count += (0 if count==2 else 1) if you in ['d',RIGHT] else (0 if count==0 else -1)
    clear()
  clear()



def num_theme(Se):
  def r(DEF=1,PAS=1,CIN=1,PIN=1,SUN=1,CLA=1):
    return DEF if Se=='default' else PAS if Se=='pastel' else CIN if Se=='cinna' else PIN if Se=='coquette' else SUN if Se=='sunset' else CLA if Se=='classic' else 1
  return {
    2:f'\033[38;5;{r(1,180,252,162,3,247)}m',
    4:f'\033[38;5;{r(2,71,195,163,221,230)}m',
    8:f'\033[38;5;{r(3,69,75,164,214,208)}m',
    16:f'\033[38;5;{r(4,99,69,201,208,202)}m',
    32:f'\033[38;5;{r(5,126,21,199,202,124)}m',
    64:f'\033[38;5;{r(6,172,177,200,204,130)}m',
    128:f'\033[38;5;{r(7,160,169,132,124,178)}m',
    256:f'\033[38;5;{r(8,196,165,177,139,184)}m',
    512:f'\033[38;5;{r(9,189,91,93,147,190)}m',
    1024:f'\033[38;5;{r(10,13,163,141,111,154)}m',
    2048:f'\033[38;5;{r(11,185,123,13,69,226)}m',
  }

def reload():
  global dolro,board
  Se = achieve['selected'][0]
  board = boards[achieve['selected'][1]]
  def r(DEF=1,PAS=1,CIN=1,PIN=1,SUN=1,CLA=1):
    return DEF if Se=='default' else PAS if Se=='pastel' else CIN if Se=='cinna' else PIN if Se=='coquette' else SUN if Se=='sunset' else CLA if Se=='classic' else 1
  dolro = num_theme(Se)
reload()
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
              save2()
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
    if Sounding:
      print('\a')
    startboard()




clear()
print("Welcome to 2048 "+("YOU CUTE SRN BABYYYYYYYYY" if BABY else ''))
print("Quests refresh daily!")
print("\n\033[01mWASD/Arrows to move pieces, other controls are shown on the next screen!\033[0m\n")
print("\nHigh score: \033[38;5;206m"+str(high()))
input("\033[38;5;57m[Enter to continue]")

clear()
startboard(True)

TESTnum = 0 #testing
toggled = True #for the control promp
ended = False

Sounding = False #secret!!

while True:
  print("\033[H",end="")
  printboard()
  print(f"\033[38;5;{achieve['ncolor']}m{name:^53}\033[0m\n{'CCS: '+str(ccs):^53}\n{'Score: '+str(score):^53}"+("\n\033[38;5;212mc\033[0m = redraw, \033[38;5;208mz\033[0m = end, \033[38;5;141mp\033[0m = shop, \033[38;5;127mi\033[0m = inv, \033[38;5;21mf\033[0m = toggle me" if toggled else ''))
  print("" if not newhigh else f"\n\033[38;5;74m{'New highscore!':^54}"+reset,end='')
  if alive2() and not ended:
    keyz=getkey()
    keyz = keyz.lower() if keyz not in [UP,DOWN,LEFT,RIGHT] else keyz
    
    move('up' if keyz in ['w',UP] else 'down' if keyz in ['s',DOWN] else 'right' if keyz in ['d',RIGHT] else 'left' if keyz in ['a',LEFT] else 'hi')
    
    if keyz == 'c':
      clear()
    
    if keyz == 'p':
      shop()
    
    if keyz=='i':
      inv()
    
    if keyz == 'y' and name=='muffinlavania': #testing
      addccs(10)
      score += 100
    
    if keyz=='m':
      Sounding = not Sounding

    if keyz=='f':
      toggled = not toggled
      clear()

    if keyz=='b':
      bdict['W'] = bdict['J'] if bdict['W']==' ' else ' '
    
    if keyz=='z':
      clear()
      print("Do you want to end your current game?\n(Press y/n)")
      if getkey().lower() == 'y':
        ended = True
      clear()
  else:
    ended = False
    clear()
    print(f"{'You lost!':^53}\n{'Final Score: '+str(score) :^53}\n{'Highscore: '+str(high()):^53}")
    printboard()
    checkquests()
    for i in achieve['quests'][1]:
      if not achieve['quests'][1][i]:
        if quests[i][0] == 'end' and score==quests[i][1]:
          achieve['quests'][1][i] = True
          addccs(quests[i][3])
          save()
          print(f"\033[38;5;129m{f'Quest | {i} | Completed!':^53}\033[0m")
    time.sleep(1)
    print("Would you like to retry?\n[type no to exit]")
    thi = input("> ").lower()
    if 'no' not in thi:
      real = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      startboard(True)
      score = 2
      thres = 1000
      newhigh = False
      clear()
    else:
      sys.exit()


'''
OLD HELLSCAPE:
lllllllllFFFllllllllllllllFllllllllllllllFFFFFlllllFF
llllFFFFFFBFFllllFFFFFFFlllllFFFFFFFlllFFFBBBFFFFlllF
lFFFF-0--BBBFFFFFF-1--BFFlllFFB-2--FFFFFBBBB-3--FlllF
FFBBBBBBBBBBBBBBBBBBBBBBFFlFFBBBBBBBBBBBBBBBBBBBFFlll
lFmmmmmmmmmmmmmmmmmmmLLLLLLLLLLLmmmmmmmmmmmmmmmmmFFll
lFFBBBBBBBBBBBBLLLLLLMMMMMMMMMMMLLLLLLBBBBBBBBBBBBFFl
llFBB-4--BBBBBLMMM-5--MMMMMMMMM-6--MMMLBBBBB-7--BBBFF
llFBBBBBBBBBBLMMMMMMMMMMMMMMMMMMMMMMMMMLBBBBBBBBBBBBF
llFFmmmmmmmmmLMMMMMMMMMMMMMMMMMMMMMMMMMLmmmmmmmmmmFFl
FllFBBBBBBBBBLMMMMMMMMMMMMMMMMMMMMMMMMMLBBBBBBBBBFFll
FllFB-8--BBBBBLMMM-9--MMMMMMMMM-a--MMMLBBBBB-b--BFllF
llFFBBBBBBBBBBBLLLLLLMMMMMMMMMMMLLLLLLBBBBBBBBBBFFllF
lFFmmmmmmmmmmmmmmmmmmLLLLLLLLLLLmmmmmmmmmmmmmmmmFllFF
lFBBBBBBBBBBBBBBBBBBBBBBFFlFFBBBBBBBBBBBBBBBBBBBFFllF
FFFBB-c--BBFFFFFFF-d--BFFlllFFB-e--FFFFFFFBB-f--BFFll
llFFFFFFFBFFlllllFFFFFFFlllllFFFFFFFlllllFFFBBFFFFlll
llllllllFFFlllFlllllllFlllFlllllllllllFFlllFFFFlllllF


'''


