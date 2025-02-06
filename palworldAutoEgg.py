import pyautogui as pa
import time

def openegg():
    pa.sleep(0.28)
    #palworld能识别到的最高速度
    pa.keyDown('f')
    print("Fkeydown",end=" ")
    pa.sleep(1.9)
    pa.keyUp('f')
    print("Fkeyup")
    pa.sleep(0.4)
    pa.hotkey("f")
Settings={'starttime':2,"line":5,"eggopenkey":"f",}
def loadSettings():
    with open(r"python\PalAutoEggSettings.txt","r") as file:
        for line in file:
            
            if line.startswith("#"):
                continue
            else:
                line=line.strip()
            key,value=line.split("=")
            Settings[key]=value
def initialize():
    global width,height
    global startx,starty
    #loadSettings()
    print(Settings)
    pa.FAILSAFE=True
    width,height=pa.size()
    #2560*1600
    startx,starty=430,670
initialize()
time.sleep(Settings["starttime"])
pa.leftClick()
pa.sleep(0.5)
pa.hotkey("f")
print("Fpress")
#time.sleep(30)
for y in range(Settings["line"]):
    for x in range(6):
        pa.hotkey(Settings["eggopenkey"])
        print("Fpress",end=" ")
        pa.sleep(0.3)
        pa.moveTo(startx+116*(x),starty+114*(y))
        xp,yp=pa.position()
        print(f"pos:({xp},{yp})",end=" ")
        pa.sleep(0.3)
        pa.rightClick()
        print("rightclick")
        openegg()
#6 wid 7 hei
#为什么byd物品栏长宽不一样啊
#2025-2-4 