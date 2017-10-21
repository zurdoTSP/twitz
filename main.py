import twipz
import sys
import config
import os.path as path
from colores import bcolors
configura=config.Configura()
x=twipz.Twipz()
favoritos=[]
if not path.exists('config.cfg'):
    print(x.url())
    y=input()
    x.obtenerAccess(y)
    configura.access_key=x.access_key
    configura.access_secret=x.access_secret
    configura.guardar()
else:
    configura.leer()
    x.access_key=configura.access_key
    x.access_secret=configura.access_secret
    favoritos=configura.favoritos.split(",")
    x.asceso()
q=x.visualizar(5)
var=""

while(var!="exit"):
    q=x.visualizar(5)
    for t in q:
        print(str(t.created_at))
        if(t.user.screen_name in favoritos):
            print("\033[1;41m"+t.user.screen_name+"\033[0m")
        else:
            print("\033[1;44m"+t.user.screen_name+"\033[0m")
        print(bcolors.OKGREEN +t.text+bcolors.ENDC)
        print(bcolors.nuevo +bcolors.BOLD+' *'*40+bcolors.ENDC)
    var=input()
    if(var==""):
        print("\n"*5)
    else:
        cad=var.split(" ")
        if(cad[0]=="fav"):
            favoritos.append(cad[1])
            print("\n"*8)
else:
    configura.favoritos=favoritos
    configura.guardar()
