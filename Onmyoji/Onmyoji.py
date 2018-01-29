import win32con,win32api,win32gui
import time

def click(pos,times):
    if times==0:
        return
    handle = win32gui.FindWindow(None,'阴阳师-网易游戏')
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    tmp = win32api.MAKELONG(pos[0],pos[1])#869,452
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp) 
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    time.sleep(0.3)
    return click(pos,times-1)

def calculateTimes(HP):
    return HP//6*(1+2//30)

def colseGame():
    win32gui.PostMessage(win32gui.FindWindow(None,'阴阳师-网易游戏'),win32con.WM_CLOSE,0,0)

def shuaGame(Times):
    if Times == 0:
        return 
    print("还有{}次,还剩下{}秒".format(Times,Times*150),end="\r")
    click([869,452],30)
    click([1033,491],30)
    time.sleep(150)
    return shuaGame(Times-1)

if __name__ == "__main__":
    print("还有多少体力？")
    shuaGame(calculateTimes(int(input(">>> "))))
    colseGame()