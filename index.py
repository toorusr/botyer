# MainUi
# from logging import exception
from tkinter import *
from tkinter.ttk import *
from random import randint
from threading import Thread
# from pexpect import pxssh


network = []


# class Func:
#     def __init__(self, hostname, username, password):
#         self.hostname = hostname
#         self.username = username
#         self.password = password
#         self.session = self.connect

#     @property
#     def connect(self):
#         try:
#             con = pxssh.pxssh()
#             con.login(self.hostname, self.username, self.password)
#             return con
#         except exception:
#             print('[!]Error Connecting:\n;start ErrorReport\n%s\n;end ErrorReport' % exception)

#     def send_command(self, command):
#         self.session.sendline(command)
#         self.session.prompt()
#         return self.session.before


# def networkSend(command):
#     for bot in network:
#         output = func.send_command(command)
#         print('[>]Output from [%s][%s]' % (func.hostname, func.username))
#         print('[|>]:%s' % output)


# def addClient(hostname, username, password):
#     bot = Func(hostname, username, password)
#     network.append(bot)




class App:
    def __init__(self):
        self.counter2 = 0
        self.curr_index = None
        self.bots = [['239' ,'127.127.127.127', 'usr92458', 'maskl02', 'Max'],
                     ['969', '721.721.721.721', 'usr35467', 'df87dgjhsd', 'Max Laptop']]
        self.currentVersion = '0.1'
        self.root = Tk()
        self.root.geometry('900x510')
        self.root.resizable(0, 0)
        self.root.title('BotyerSuit')
        # self.root.iconbitmap('index_files/botyer.ico')
        self.image_botyerIcon = PhotoImage(file='./index_files/botyer.gif')
        self.image_botyerIcon_small = PhotoImage(file='./index_files/botyer_fiex.gif')
        self.index_rmc = None
        self.clientConfigFrameF()
        self.processFrameF()
        self.startFrameF()


        self.mainFrameF()

        self.startFrame.tkraise()
        self.inDev()

        self.counter = 0
        def changeP():

            self.counter += 1
            if self.counter == 1:
                self.processOut.config(text='Loading processDisplay...')
                self.processOut.after(3000, changeP)
            elif self.counter == 2:
                self.processOut.config(text='Welcome to BotyerSuit!!!')
                self.processOut.after(2000, changeP)
            elif self.counter == 3:
                self.processOut.config(text='Developing BotyerSuit')
                self.processOut.after(1000, changeP)
            elif self.counter == 4:
                self.processOut.config(text='Developing BotyerSuit ⚫')
                self.processOut.after(1000, changeP)
            elif self.counter == 5:
                self.processOut.config(text='Developing BotyerSuit ⚫⚫')
                self.processOut.after(1000, changeP)
            elif self.counter == 6:
                self.processOut.config(text='Developing BotyerSuit ⚫⚫⚫')
                self.counter = 2
                self.processOut.after(1000, changeP)
            else:
                print('App.__init__.changeP error')
        #changeP()


        self.root.mainloop()

    def startFrameF(self):
        def raise_frame():
            self.mainFrame.tkraise()
            self.processFrame.tkraise()
        self.image_startFrame = PhotoImage(file='layout/startFrame_withBackground.layout.gif')
        self.image_startButton = PhotoImage(file='startFrame_files/startButton.gif')
        self.startFrame = Frame(self.root)
        self.startFrame.place(x=0, y=0, height=510, width=900)
        background = Label(self.startFrame, image=self.image_startFrame)
        background.place(x=0, y=0, height=510, width=900)
        style = Style()
        style.configure('my.TButton', bg='black')
        startButton = Button(self.startFrame, image=self.image_startButton, style='my.TButton', command=raise_frame)
        startButton.place(x=320, y=217)
        versionInfo = Canvas(self.startFrame)
        versionInfo.place(x=810, y=480, width=90, height=30)
        versionInfo.create_text(30, 11, fill='black', font="Akkadian",
                               text="v%s" %self.currentVersion)
        versionInfo.create_image(70, 15, image=self.image_botyerIcon_small)

    def mainFrameF(self):
        self.image_mainFrame = PhotoImage(file='./layout/mainFrame.layout.gif')
        self.image_sendButton = PhotoImage(file='./mainFrame_files/sendButton.gif')
        self.mainFrame = Frame(self.root)
        self.mainFrame.place(x=0, y=0, height=510, width=900)
        background = Label(self.mainFrame, image=self.image_mainFrame)
        background.place(x='-1', y='-1', height=510, width=900)
        self.hoverEvent(background, 'WIDGETS MISSING')
    # log
        log = Text(self.mainFrame)
        log.place(x=0, y=0, height=450, width=680)
        scrollbarLog = Scrollbar(self.mainFrame)
        scrollbarLog.place(x=680, y=0, height=450, width=20)
        log.config(yscrollcommand=scrollbarLog.set, state=DISABLED)
        scrollbarLog.config(command=log.yview)
    # commandEntry
        commandEntry = Entry(self.mainFrame)
        commandEntry.place(x=0, y=450, height=40, width=550)
        self.focusEvent(commandEntry, 'Usage: [BotNumber/"ALL"]$[COMMAND]')
        commandEntry.bind('<Return>', lambda e:  self.processOut.configure(text='SENDED by <Return>'))
    # sendButton
        style = Style()
        style.configure('my.TButton', font=('Akkadian', 10), bg='white')
        sendButton = Button(self.mainFrame, style='my.TButton', text='SEND>')
        sendButton.place(x=550, y=450, height=40, width=150)
        self.hoverEvent(sendButton, 'Double-click to send command.')
        sendButton.bind('<Double-Button-1>', lambda e:  self.processOut.configure(text='SENDED by pressing Button'))
    # configButton
        def raise_frame():
            self.clientConfigFrame.tkraise()
            self.processFrame.tkraise()
        style2 = Style()
        style2.configure('my2.TButton', relief='flat')
        configButton = Button(self.mainFrame, style='my2.TButton', text='add/del Bots')
        configButton.place(x=700, y=0, height=50, width=200)
        configButton.bind('<Double-Button-1>', lambda e:  raise_frame())
    # botList
        self.botList = Frame(self.mainFrame)
        self.botList.place(x=700, y=50, height=400, width=200)
    # logo
        logoArea = Canvas(self.mainFrame)
        logoArea.place(x=700, y=450, height=60, width=200)
        logoArea.create_image(168, 30, image=self.image_botyerIcon)

    def processFrameF(self):
        self.processFrame =  Frame(self.root)
        self.processOut = Label(self.processFrame, font='Arial 9', text='In Development...')
        self.processFrame.place(x=0, y=490, width=700, height=20)
        self.processOut.place(x=0, y=0, width=700, height=20)
        # label... connected to info

    def errorFrameF(self):
        self.errorFrame = Frame(self.root)
        self.errorFrame.place(x=0, y=0, height=100, width=200)
        # label... ErrorInfo
        # pops-up at error

    def downloadFrameF(self):
        self.downloadFrame = Frame(self.root)
        self.downloadFrame.place(x=0, y=0, height=510, width=900)
        # backgroundGraphic
        # Entry's (URL&ClientChooser)
        # List of connected clients
        # title
        # back&submit button

    def clientConfigFrameF(self):
        self.clientConfigFrame = Frame(self.root)
        self.clientConfigFrame.place(x=0, y=0, height=510, width=900)
        self.image_clientConfigFrame = PhotoImage(file='./layout/botConfig_withbackground_2.layout.gif')
        background = Label(self.clientConfigFrame, image=self.image_clientConfigFrame)
        background.place(x='-1', y='-1', height=510, width=900)
    # clientList
        # Menu
        self.clientList = Listbox(self.clientConfigFrame)
        self.clientList.place(x=50, y=200, height=261, width=410)
        scrollbarLog = Scrollbar(self.clientConfigFrame)
        scrollbarLog.place(x=460, y=201, height=260, width=20)
        self.clientList.config(yscrollcommand=scrollbarLog.set, state='normal')
        scrollbarLog.config(command=self.clientList.yview)
    # clientipEntry
        clientipEntry = Entry(self.clientConfigFrame)
        clientipEntry.place(x=50, y=160, height=30, width=100)
        self.placeHolder(clientipEntry, 'IP')
    # clientusernameEntry
        clientusernameEntry = Entry(self.clientConfigFrame)
        clientusernameEntry.place(x=155, y=160, height=30, width=100)
        self.placeHolder(clientusernameEntry, 'USERNAME')
    # clientpasswordEntry
        clientpasswordEntry = Entry(self.clientConfigFrame)#show=''
        clientpasswordEntry.place(x=260, y=160, height=30, width=100)
        self.placeHolder(clientpasswordEntry, 'PASSWORD', pw=True)
    # clientnameEntry
        clientnameEntry = Entry(self.clientConfigFrame)
        clientnameEntry.place(x=380, y=160, height=30, width=90)
        self.placeHolder(clientnameEntry, 'BOTNAME')
    # addClient
        addclientButton = Button(self.clientConfigFrame, text='+')
        addclientButton.bind('<Button-1>', lambda e: self.addClient(clientipEntry.get(),
                                                                    clientusernameEntry.get(),
                                                                    clientpasswordEntry.get(),
                                                                    clientnameEntry.get()))
        addclientButton.place(x=480, y=160, height=30, width=30)
    def hoverEvent(self, widget, hoverText):
        widget.bind('<Enter>', lambda event:  self.processOut.config(text=hoverText))
        widget.bind('<Leave>', lambda enent:  self.processOut.config(text=''))

    def sendCommand(self):
        pass
        # !!! Send to bots

    def focusEvent(self, widget, focusText):
        widget.bind('<FocusIn>', lambda e:  self.processOut.config(text=focusText))
        widget.bind('<FocusOut>', lambda e:  self.processOut.config(text=''))

    def placeHolder(self, widget, placeholderText, pw=False):
        def checkWidget_Out(widget):
            if widget.get() != '':
                pass
            else:
                widget.insert(0, placeholderText)
                widget.configure(font='standart 9 italic', foreground='gray')
                if pw == True:
                    widget.config(show='')
                else:
                    pass
        def checkWidget_In(placeholderText, widget):
            if widget.get() == placeholderText:
                widget.delete(0, END)
                s = Style()
                s.configure('my.TEntry', foreground='black')
                widget.configure(font='standart 9', foreground='black')
                if pw == True:
                    widget.config(show='•')
                else:
                    pass
            else:
                pass
        checkWidget_Out(widget)
        widget.bind('<FocusIn>', lambda e:  checkWidget_In(placeholderText, widget))
        widget.bind('<FocusOut>', lambda e:  checkWidget_Out(widget))

    def addClient(self, ip, name, password, botName):
        print('AUSGEFÜHRTZ')
        '''login stuff here...'''
        login = True
        if login == True:
            rndm = randint(1, 999)
            for x in self.bots:
                if x[0] == rndm:
                    rndm = randint(1, 999)
                else:
                    pass
                    print('pass')

            self.bots.append([rndm, ip, name, password, botName])
            size = self.clientList.size()
            self.clientList.delete(0, size)
            for x in self.bots:
                self.clientList.insert(0, '{%s|%s}[%s$%s]' % (x[0], x[4], x[1], x[2]))
        else:
            self.processOut.config(text='[!]Login to user %s$%s failed.' % (ip, name))

    def inDev(self):
        self.root_tl = Toplevel(self.root)
        self.root_tl.overrideredirect(1)
        self.root_tl.geometry('230x30')
        self.root_tl.wm_attributes("-topmost", 1)
        canv = Canvas(self.root_tl)  # LOGO
        canv.place(x='-2', y='-2', width=234, height=34)
        canv.create_rectangle(0, 0, 234, 34, fill='gray')
        logo = Canvas(self.root_tl)
        logo.place(x=2, y=2, width=28, height=26)
        logo.create_image(14, 13, image=self.image_botyerIcon_small)
        self.lbl_tl = Label(self.root_tl, text='[!]Error.')
        self.lbl_tl.place(x=30, y=2, width=198, height=26)

        def changel():
            self.counter2 += 1
            if self.counter2 == 1:
                self.lbl_tl.config(text='Loading DEV_SCREEN...')
                self.lbl_tl.after(2000, changel)
            elif self.counter2 == 2:
                self.lbl_tl.config(text='Start...')
                self.lbl_tl.after(2000, changel)
            elif self.counter2 == 3:
                self.lbl_tl.config(text='Developing BotyerSuit')
                self.lbl_tl.after(1000, changel)
            elif self.counter2 == 4:
                self.lbl_tl.config(text='Developing BotyerSuit ⚫')
                self.lbl_tl.after(1000, changel)
            elif self.counter2 == 5:
                self.lbl_tl.config(text='Developing BotyerSuit ⚫⚫')
                self.lbl_tl.after(1000, changel)
            elif self.counter2 == 6:
                self.lbl_tl.config(text='Developing BotyerSuit ⚫⚫⚫')
                self.counter2 = 2
                self.lbl_tl.after(1000, changel)
            else:
                pass
        changel()




app = App()
# CommandEntry, Prompt, connectedClients, logout, closeControl
# Are you sure you want to send this command? <Function
