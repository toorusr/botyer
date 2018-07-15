#from win32 import *
#import win32api
#import win32console
#import win32gui
import pythoncom, pyHook
import ascii
#win = win32console.GetConsoleWindow()
#win32gui.ShowWindow(win, 0)

keylist = []
def OnKeyboardEvent(event):

    if event.Key != chr(event.Ascii):
        #print('<' + event.Key + '>')
        print('ASCII:' + chr(event.Ascii))
    else:
        print('KEY  :' + event.Key)



hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
