import pyautogui as pa
import time
def openegg():
    pa.sleep(0.5)
    pa.keyDown('f')
    print("Fkeydown",end=" ")
    pa.sleep(2.0)
    pa.keyUp('f')
    print("Fkeyup")
    pa.sleep(0.5)
    pa.hotkey("f")
pa.FAILSAFE=True
#width,height=pa.size()
startx,starty=430,670
time.sleep(4)
pa.leftClick()
pa.sleep(0.5)
pa.hotkey("f")
print("Fpress")
for y in range(5):
    for x in range(6):
        pa.hotkey("f")
        print("Fpress",end=" ")
        pa.sleep(0.3)
        pa.moveTo(startx+116*(x),starty+114*(y))
        xp,yp=pa.position()
        print(f"pos:({xp},{yp})",end=" ")
        pa.sleep(0.5)
        pa.rightClick()
        print("rightclick")
        openegg()