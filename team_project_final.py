from tkinter import *
from tkinter import ttk
from pynput import mouse
from pynput import keyboard
import time
import pyautogui

wd = Tk()
wd.title("SimpleAutoClicker")
wd.geometry("380x230")
wd.resizable(False, False)

xLabel = Label(wd, text = "X좌표")
xLabel.grid(row = 1, column = 1)

xEntry = Entry(wd, width = 10)
xEntry.grid(row = 1, column = 2)

yLabel = Label(wd, text="Y좌표")
yLabel.grid(row=1, column=3)

yEntry = Entry(wd, width = 10)
yEntry.grid(row=1, column=4)

PositionBtn = Button(wd, text="마우스 위치", command = lambda:insertPosition())
PositionBtn.grid(row=1, column=5)

radSelect = IntVar()
radVar = IntVar()
radVarClick = IntVar()
radStyle = IntVar()

#마우스 부분
mouseClick = Radiobutton(wd, text="마우스", variable = radSelect, value=1)
mouseClick.grid(row=2, column=3)

leftClick = Radiobutton(wd, text="좌클릭", variable = radVar, value=2)
leftClick.grid(row=3, column=2)

rightClick = Radiobutton(wd, text="우클릭", variable = radVar, value=3)
rightClick.grid(row=3, column=4)

oneClick = Radiobutton(wd, text="클릭", variable = radVarClick, value=4)
oneClick.grid(row=4, column=2)

doubleClick = Radiobutton(wd, text="더블클릭", variable = radVarClick, value = 5)
doubleClick.grid(row=4, column=4)

#키보드 부분

keyClick = Radiobutton(wd, text="키보드", variable = radSelect, value=6)
keyClick.grid(row=5, column=3)

blankWrite = Radiobutton(wd, text="띄어쓰기", variable = radStyle, value=7)
blankWrite.grid(row=6, column=2)

enterWrite = Radiobutton(wd, text="줄 바꿈", variable = radStyle, value=8)
enterWrite.grid(row=6, column=4)

# 키보드 ui================================================
keyLabel = Label(wd, text = "입력 문자")
keyLabel.grid(row=7, column=1)

keyEntry = Entry(wd, width = 10)
keyEntry.grid(row=7, column=2)
keyEntry.insert(END, '')

#키보드 ui ================================================

reLabel = Label(wd, text = "반복 횟수")
reLabel.grid(row=8, column=1)
 
reEntry = Entry(wd, width=10)
reEntry.grid(row=8, column=2)
reEntry.insert(END,'0')

intervalLabel = Label(wd, text="반복 간격")
intervalLabel.grid(row=8, column=3)

intervalEntry = Entry(wd, width=10)
intervalEntry.grid(row=8, column=4)
intervalEntry.insert(END,'0')

startBtn = Button(wd, text="시작", command = lambda:click_run())
startBtn.grid(row=9, column=3)

 
 # 함수
def insertPosition():
    with mouse.Listener(on_click=savePosition) as listener:
        listener.join()
    xEntry.insert(END,x1)
    yEntry.insert(END,y1)
 
def savePosition(x, y, button, pressed):
    if pressed:
        global x1
        global y1
        x1 = x
        y1 = y
        
    if not pressed :
        return False

def click_run():
    click_num = int(reEntry.get()) # 클릭 횟수를 reEntry에 입력한 것을 받아온다.
    click_inter = float(intervalEntry.get()) # 클릭 주기를 intervalEntry에 입력한 것을 받아온다.
    key_type = str(keyEntry.get()) # 키보드 타입을 keyEntry에 입력한 것을 받아온다.
 
    ##반복시작
    for a in range(0,click_num):

        # radio버튼 마우스 클릭 선택했을 경우
        if radSelect.get() == 1:
            # radio버튼 좌클릭 선택했을 경우
            if radVar.get() == 2:
                # radio버튼 클릭 선택했을 경우
                if radVarClick.get() == 4:
                    pyautogui.click(x1,y1, button='left')
                    time.sleep(click_inter)

                # radio버튼 더블클릭 선택했을 경우
                if radVarClick.get() == 5:
                    pyautogui.doubleClick(x1,y1, button='left')
                    time.sleep(click_inter)

            # radio버튼 우클릭 선택했을 경우 수행
            if radVar.get() == 3:
                # radio버튼 클릭 선택했을 경우
                if radVarClick.get() == 4:
                    pyautogui.click(x1,y1, button='right')
                    time.sleep(click_inter)

                # radio버튼 더블클릭 선택했을 경우
                if radVarClick.get() == 5:
                    pyautogui.doubleClick(x1,y1, button='right')
                    time.sleep(click_inter)

        # radio버튼 키보드 선택했을 경우 수행
        if radSelect.get() == 6:
            # radio버튼 띄어쓰기 선택했을 경우 
            if radStyle.get() == 7:
                time.sleep(0.5)
                pyautogui.write(key_type, interval=0.1)
                pyautogui.write(' ')
                time.sleep(click_inter)
            
            # radio버튼 줄 바꿈 선택했을 경우
            if radStyle.get() == 8:
                time.sleep(0.5)
                pyautogui.write(key_type, interval=0.1)
                pyautogui.write('\n')
                time.sleep(click_inter)

wd.mainloop()