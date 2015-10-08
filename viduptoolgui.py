#!python 2.7
from Tkinter import *
import tkFileDialog, base64, os, tempfile
from videoupload import vidup

folderIcon = """R0lGODlhEAAQAPcAAAAAAFVXU1haVltdWWZoYG5wbHx+eoiKeI+Rfo+SfoGDgIeJgYyNipKUgZmb
hpqch5qdiJ2fkaKkk6OklaOllqmqmq+wn7O1o7W4prm6pLm6rLu9qru8rr/Ar8HDssPFtcTFtcXG
tcXGtsvMvMvMvczNv83Ov8vMwM3OwM7PwdDRxNHTxtLUx9XWydbXytfYzNjZzAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAA
AAiOAA0EGDhQwb+DCBEG8PChoYYACSMG2ADhgQMLBDMGYPAvwIUECRA0qCBhAoWTFCJADIDhgMsD
BAYImClgQIGVBWgK4HAChgsWK1QsWOmiqNERGZImVbGyhdKnT5l2fAG1aomVKapCvdoRhdanXAOY
+KqUxEqkZDOEWAlChNu3bkPI7QCRgca7AzlG3BsxIAA7"""

windowIcon = """AAABAAEAIBwAAAEAIACYDgAAFgAAACgAAAAgAAAAOAAAAAEAIAAAAAAAAA4AAD8DAAA/AwAAAAAA
AAAAAACCMBkAgjAZAIIwGQCCMBkAAAAAAAAAAABFDZ0kRQ2cokUNnPFFDZzZRQycZkYMnAUAAAAA
AAAAAAAAAABGDJwARwqiBEUNnEBFDZyARQ2csEUNnMpFDZzERQ2cpUUNnH5FDZxXRQ+bGEUNnABF
DZwAAAAAAAAAAAAAAAAAAAAAAIIwGRuCMBljgjAZRIIwGQmCMBkAhDEVAEUNnG1FDZz9RQ2c/0UN
nP9FDZzURQ2cGVUIhgBFDpwARQycAEYMnBVGDZx1RQ2c2kUNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c
/kUNnPRFDZyuRQ2cP0UNnAFFDZwAAAAAAAAAAAAAAAAAgjAZU4IwGe+CMBnlgjAZp4IwGTiFMhIG
RAyfYkUNnPlFDZz/RQ2c/0UNnOxFDZxHRA2dAEUPnAVEDpw7RQ2csUUNnPZFDZz/RQ2c/0UNnP9F
DZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZzeRQ2cZUUNnAVEDZwAAAAAAAAAAACCMBlRgjAZ94Iw
Gf+CMBnPgjAZr4MwGIBnIVdARQ2du0UNnP9FDZz/RQ2c/kUNnLVFDZxURQ2chEUNnN1FDZz/RQ2c
/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZzmRQ2cWEQNnAMAAAAA
AAAAAIIwGTKCMBnWgjAZ9IIwGVuCMBkkgjAZboQxF3NaGW9XRA2dqEUNnP1FDZz/RQ2c/0UNnP9F
DZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP5FDZzXRQ2cjUUNnH5FDZyRRQ2c50UN
nP9FDZzNRg2bHUUNmAAAAAAAgjAZBoIwGZiCMBn7gjAZa4IwGQCBMBkAgjAZGZg9AAlCDKESRQ2c
cEUNnNhFDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP5FDZzjRQyckEQNnCVGDZoG
SQ6YAUUMnAhEDZxWRQ2c4EUNnP9FDZx/RQ2bAQAAAACCMBkAgjAZaIIwGfmCMBmVgjAZAIIwGQCC
MBkAgC8dAEMMoABFDZwBRg2bJkUNnJhFDZzJRQ2c90UNnP9FDZz/RQ2c/0UNnP9FDZz+RQ2c90UN
nKRFDZxIRQ6cGD8OmgBGDJsARQycAEMMmwJFDZxMRQ2cqEUNnV5FDZ4BAAAAAIIwGQCCMBk4gjAZ
5YIwGcCCMBkaAAAAAAAAAAAAAAAAAAAAAEUNnABGDZsARA+aDkUMnINFDZzxRQ2c/0UNnP9FDZz/
RQ2c/0UNnP1FDZz3RQ2c/0UNnOZFDZy7RQ2cf0UMmxhHD50BRQ2cAEgNoABEDJ0JRQqeAUUNngAA
AAAAAAAAAIIwGROCMBnQgjAZ8YIwGUyCMBkAAAAAAAAAAAAAAAAARw2eAEYMmxZFDZyPRQ2c60UN
nP1FDZz9RQ2c/0UNnP9FDZz/RQ2c/UUNnP9FDZz/RQ2c/0UNnP9FDZz7RQ2c0UUNnGhFDZsORA2c
AEUMnABFDJ0AAAAAAAAAAACCMBkAgjAZAoIwGaqCMBn/gjAZa4IwGQAAAAAAAAAAAEUQnQBHDZ4N
RQ2cjkUNnPpFDZz/RQ2c/0UNnP5FDZz+RQ2c/0UNnPdFDZuYRQ2ctEUNnPtFDZz/RQ2c/0UNnP9F
DZz/RQ2c90UNnJtFDZwpRQ2dAEUNnAAAAAAAAAAAAIIwGVSCMBkkgjAZZ4IwGfyCMBmMgjAZBwAA
AAAAAAAARQBsAEUNm11FDZzxRQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2cxEUNnBhGDpwrRQ2c
y0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/kUNnLJFDZ0nRQ2gAEUNpgAAAAAAgjAZaIIwGbaCMBnR
gjAZ/4IwGcmCMBkXAAAAAAAAAABFDp0YRQ2ctUUNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9F
DZyDRQ2cAksMmQFFDZxSRQ2c7EUNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/EUNnLhFDZ0iRA2cAAAA
AACCMBkDgjAZL4IwGY6CMBnsgjAZ9IIwGTMAAAAARQ6cAEUNnFBFDZz3RQ2c/0UNnP9FDZz/RQ2c
/0UNnP9FDZz/RQ2c/0UNnHhFDZwARw2bAEcNnA9FDZzDRQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/
RQ2c/UUNnJZEDZ0MRQybAIIwGQCCMBkAgjAZBoIwGUOCMBl+gjAZLwAAAABFC5wDRQ2cekUNnP9F
DZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2ceQAAAAAAAAAARA2cAkUNnGpFDZz9RQ2c/0UN
nP9FDZz/RQ2c/0UNnP9FDZz/RQ2c70UOnFpFAIoAAAAAAAAAAACCMBkAgjAZAIIwGQWCMBkDAAAA
AEUNnAhFDZyVRQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZx6SBSjAAAAAABFDZwA
RQ2dKkUNnN9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2ctUUNnBsAAAAAAAAAAAAAAACC
MBkAgjAZAIIwGQCCMBoARA2dB0UNnJRFDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UN
nINIFKMCAAAAAAAAAABFDZwORQ2cpEUNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz0RQ2c
WQAAAAAAAAAAAAAAAIIwGQCCMBlBgjAZd4MwFxJKD5MFRQ2cg0UNnP9FDZz/RQ2c/0UNnP9FDZz/
RQ2c/0UNnP9FDZz/RQ2cp0QPnBAAAAAAAAAAAEUNnAJFDJ1+RQ2c/0UNnP9FDZz/RQ2c/0UNnP9F
DZz/RQ2c/0UNnP9FDZyHAAAAAAAAAAAAAAAAgjAZDYIwGaWCMBn5gjAZmI02BRBEDJ9URQ2c/EUN
nP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZzbRQ6cKAAAAAAAAAAARQ2cAEUNnGJFDZz4RQ2c
/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnNAAAAAAAAAAAAAAAACCMBkRgjAZfYIwGfKCMBmh
jDYEDkIMny1FDZzWRQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnPVFDpw7RQ2cAAAAAAAA
AAAARQ2bRUUNnORFDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c7wAAAAAAAAAAAAAAAIIw
GQCCMBkLgjAZTIIwGS+MNgQARQ6YBUUNnIpFDZz+RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c
/EUNnGtFDZwBAAAAAAAAAABFDZwaRQ2cx0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz0
AAAAAAAAAAAAAAAAgjAZAIIwGQCCMBkAgjAZAAAAAABEDZsARQ2cPEUNnOFFDZz/RQ2c/0UNnP9F
DZz/RQ2c/0UNnP9FDZz/RQ2cnUUNnAUAAAAAAAAAAEULngBFDZy1RQ2c/0UNnP9FDZz/RQ2c/0UN
nP9FDZz/RQ2c/0UNnOAAAAAAAAAAAAAAAAAAAAAAgjAZAIIwGQCCMBkAAAAAAAAAAAA+B5YDRQ2c
ckUNnPhFDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZzTRA2eFEINnwAAAAAARQ2cAEUNnLVFDZz/
RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2cqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAEAJmABFDZ0TRQ2cp0UNnPtFDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnPhFDZxyPw+kAQAA
AABID5wARQ2ctUUNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2c/0UNnPlFDJxmAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEIQogBFDJ0jRQ2cqUUNnPtFDZz/RQ2c/0UNnP9FDZz/
RQ2c/0UNnLNDDJ0VRg2dAEkQnANFDZy3RQ2c/0UNnP9FDZz/RQ2c/0UNnP9FDZz/RQ2cwkUNnCQA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEUMnQBFDZwfRQ2cn0UN
nPdFDZz/RQ2c/0UNnP9FDZz/RQ2c70UNnGVDDZ0ARw2bJkUNnNBFDZz/RQ2c/0UNnP9FDZz/RQ2c
/0UNnOJFDZxJRQ2cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAEUNnABFDZwMRQ2cZEUNnNdFDZz/RQ2c/0UNnP9FDZz/RQ2c20UNnURFDZx2RQ2c90UNnP9F
DZz/RQ2c/0UNnP9FDZzhRQycWUUNngMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAARQ2cAEUNnABPB6sBRQycMUUNnIdFDZzSRQ2c+UUNnP9FDZz/RQ2c
50UNnOZFDZz/RQ2c/0UNnP5FDZzxRQ2csUUNnERFDJ4CRQ2dAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE8IqQBFDJwAQRGYA0UNnDFF
DZxgRQ2cj0UNnM1FDZztRQ2c9EUNnO1FDZzJRQ2chUUNnFNFDZwZRQ2cAEUNngAAAAAAAAAAAPwP
AD8MDgAPAAgABwAAAAMAAAABDAAAAY+AAcGH4AAzh8AAH4OAAA8DgAAHAwAAAwMAMAHCADAA8gA4
APoAGADwABgA4AAcAOAADADxAAwA/4AMAP+ADgD/wAYA/+AEAP/wBAH/+AAB//wAA///AA8="""


class Application():
    """Build the basic window frame template"""

    def __init__(self, master):      
        self.mainwindow = Frame(master)
        self.mainwindow.pack()
        self.mainwindow.pack(fill=BOTH, expand=1)

        self.videoAndManifestSource = ""
        self.databaseFile = ""
        self.videoDestination = ""

        #setup window icon
        self.iconData = base64.b64decode(windowIcon)
        self.tempIconFile = tempfile.NamedTemporaryFile(delete=False) #do not delete on close
        #print(self.tempIconFile.name)
        self.tempIconFile.write(self.iconData)
        self.tempIconFile.close()
        master.wm_iconbitmap(self.tempIconFile.name)

        #self.create_widgets()


    #def create_widgets(self):
        frame = Frame(self.mainwindow, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        group = LabelFrame(frame, text="Video & Manifest Source", padx=5, pady=5)
        group.pack(padx=5, pady=5, fill=X, expand=1)

        group1 = LabelFrame(frame, text="Database File", padx=5, pady=5)
        group1.pack(padx=5, pady=5, fill=X, expand=1)

        group2 = LabelFrame(frame, text="Video Destination", padx=5, pady=5)
        group2.pack(padx=5, pady=5, fill=X, expand=1)
        
####        menubar = Menu(self)
####        filemenu = Menu(menubar)
####        filemenu.add_command(label='Calculate', command=self.calculate)
####        filemenu.add_command(label='Reset', command=self.clear)
####        menubar.add_cascade(label='File', menu=filemenu)
####        menubar.add_command(label='Quit', command=self.quit)
####        root.config(menu=menubar)

        self.videoSrcTxt = Entry(group)
        self.videoSrcTxt.pack(side=LEFT, padx=5, fill=X, expand=1)
        self.videoSrcTxt.focus_set()

        self.photo = PhotoImage(data=folderIcon)
        
        self.videoSrcTxtBrowseBtn = Button(group, image=self.photo, command=self.select_videoAndManifestSource)
        self.videoSrcTxtBrowseBtn.pack(side=RIGHT)

        self.dbSrcTxt = Entry(group1)
        self.dbSrcTxt.pack(side=LEFT, padx=5, fill=X, expand=1)

        self.dbSrcTxtBrowseBtn = Button(group1, image=self.photo, command=self.select_db)
        self.dbSrcTxtBrowseBtn.pack(side=RIGHT)

        self.videoDestTxt = Entry(group2)
        self.videoDestTxt.pack(side=LEFT, padx=5, fill=X, expand=1)

        self.videoDestTxtBtn = Button(group2, image=self.photo, command=self.select_videoDestination)
        self.videoDestTxtBtn.pack(side=RIGHT)

        self.exitBtn = Button(self.mainwindow, text="Exit", width=10,command=self.quit)
        self.exitBtn.pack(side=RIGHT, padx=5, pady=5)

        self.runBtn = Button(self.mainwindow, text="Run", width=10, command=self.run_vidupScript)
        self.runBtn.pack(side=RIGHT, padx=5)
        

    def select_videoAndManifestSource(self):
        dirpath = tkFileDialog.askdirectory(parent=self.mainwindow,initialdir="/",\
                    title="Please select the source directory", mustexist=True)
        self.videoSrcTxt.delete(0,END)
        self.videoSrcTxt.insert(0, dirpath)
        self.videoAndManifestSource = dirpath
        #print("Video and manifest source: "+dirpath)

    def select_db(self):    
        filepath = tkFileDialog.askopenfilename(parent=self.mainwindow, title="Please select the database file")
        self.dbSrcTxt.delete(0,END)
        self.dbSrcTxt.insert(0, filepath)
        self.databaseFile = filepath
        #print("Database file: "+self.databaseFile)

    def select_videoDestination(self):
        dirpath = tkFileDialog.askdirectory(parent=self.mainwindow,initialdir="/",\
                   title="Please select the source directory", mustexist=True)
        self.videoDestTxt.delete(0,END)
        self.videoDestTxt.insert(0, dirpath)
        self.videoDestination = dirpath
        #print("Video destination: "+dirpath)

    def run_vidupScript(self):
        vidup(self.videoAndManifestSource, self.databaseFile, self.videoDestination)

    def quit(self):
        self.mainwindow.quit()
        
        if os.path.exists(self.tempIconFile.name):
            os.remove(self.tempIconFile.name)
##            if os.path.exists(self.tempIconFile.name)==False:
##                print(self.tempIconFile.name+"removed")

                

root = Tk()
root.title('Video Upload Tool')
root.geometry('500x280')

app = Application(root)
root.mainloop()
root.destroy()

