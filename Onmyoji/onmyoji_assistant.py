'''
there are functions of onmyoji_assistant.
'''

import time
import win32con
import win32api
import win32gui

def click(pos, times):
    ''' simulate mouse action'''
    if times == 0:
        return None
    handle = win32gui.FindWindow(None, '阴阳师-网易游戏')
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    tmp = win32api.MAKELONG(pos[0], pos[1])#869,452
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    time.sleep(0.3)
    return click(pos, times-1)

def calculate_times(health):
    """calculate how time need"""
    return health//6*(1+2//30)

def colse_game():
    """close game client"""
    win32gui.PostMessage(win32gui.FindWindow(None, '阴阳师-网易游戏'), win32con.WM_CLOSE, 0, 0)
    return None

def shua_game(shua_times, wait_time):
    """main function"""
    if shua_times == 0:
        return None
    #print("还有{}次,还剩下{}秒".format(Times,Times*150),end="\r")
    #click((869,452),30)
    #click((1033,491),30)
    click(pos=(1069, 552), times=30)
    click(pos=(1233, 591), times=30)
    time.sleep(int(wait_time))
    return shua_game(shua_times-1, wait_time)


def client_pos():
    '''
       help to find click pos
    '''
    handle = win32gui.FindWindow(None, '阴阳师-网易游戏')
    pos = win32gui.GetCursorPos()
    client_pos = win32gui.ScreenToClient(handle, pos)
    return client_pos
