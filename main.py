import twipz
import sys
import config
import os.path as path
from colores import bcolors
configura=config.Configura()
x=twipz.Twipz()
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
    x.asceso()
q=x.visualizar(5)
var=""
while(var!="exit"):
    q=x.visualizar(var)
    for t in q:
        print(str(t.created_at))
        print("\033[1;44m"+t.user.screen_name+"\033[0m")
        print(bcolors.OKGREEN +t.text+bcolors.ENDC)
        print(bcolors.nuevo +bcolors.BOLD+' *'*40+bcolors.ENDC)
    var=input()
    if(var==""):
        print("\n"*5)
