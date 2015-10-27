"""
#!python 2.7
A graphical interface to videoupload.py
YemiDaniel-12/10/2015
"""
from Tkinter import *
from videoupload import Videoupload
import tkFileDialog,tkMessageBox, base64, os, tempfile, time

#try:

class Videouploadgui(Frame):

    def __init__(self):

        self.dbButtonIconData = """R0lGODlhEAAQAPcAAAAAAHd3d3l5eXp6ent7e3x8fH5+foGBgYKCgoODg4SEhIWFhYaGhoeHh4iI
        iImJiYqKiouLi4yMjI2NjY6Ojo+Pj5CQkJGRkZKSkpOTk5SUlJWVlZaWlpiYmJmZmZqampubm52d
        nZ6enp+fn6CgoKGhoaKioqOjo6SkpKWlpaampqenp6ioqKmpqaqqqqysrK2tra+vr7CwsLGxsbKy
        srOzs7S0tLW1tba2tre3t7m5ubq6uru7u7y8vL29vb6+vr+/v8DAwMHBwcLCwsTExMXFxcbGxsfH
        x8jIyMnJycvLy8zMzM3Nzc7Ozs/Pz9DQ0NHR0dLS0tPT09TU1NbW1tfX19jY2NnZ2dvb29zc3N3d
        3eDg4OLi4uPj4+bm5gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAA
        AAjpAP8JHEiwoEANHVDQ8GFkCRMkQW6wAKFDoAUSLnIUiZJlSxUlQGakcCGQgAIMJ2wYmXKFiY8X
        HyCcECgBwQQPKGDYwCFjRYgLC3hYNBHjx5IrXLxoiULkxgqS/xxsKFGUyRUtUozkmLhC4IAACTCY
        mOFDSI4WHyIUeCEwAwgWOYg0mULlyREeMETcsDiiRVwoHako+SEDBVQBByyUqFFEipUlPVx0cGBC
        IIUGGES0mJFDh40XJjY86DEUBo8kVLZ0weJkSA0VUBlkhuFjiZUsTG+o6ND1n4EACCqEcIFjR2EO
        DgjMMMicYEAAOw=="""

        self.folderButtonIconData = """R0lGODlhEAAQAPcAAAAAAFVXU1haVltdWWZoYG5wbHx+eoiKeI+Rfo+SfoGDgIeJgYyNipKUgZmb
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

        self.windowIconData = """AAABAAEAIBwAAAEAIACYDgAAFgAAACgAAAAgAAAAOAAAAAEAIAAAAAAAAA4AAD8DAAA/AwAAAAAA
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
        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"""

        self.master = Tk()
        self.master.title('Video Upload Tool')
        self.master.geometry('500x480')

        #setup window icon
        self.iconData = base64.b64decode(self.windowIconData)
        self.tempIconFile = tempfile.NamedTemporaryFile(delete=False) #do not delete on close
        self.tempIconFile.write(self.iconData)
        self.tempIconFile.close()
        self.master.wm_iconbitmap(self.tempIconFile.name)

        #initialize the video upload script and pass it a handle to the GUI
        self.vidup = Videoupload(self)
        self.dbFile = self.vidup.get_dbFile()
        self.vidDest = self.vidup.get_vidDest()

        Frame.__init__(self, self.master)
        self.create_widgets()
        self.feildDefaults()

        #bound to rhe return key
    def return_key(self, event):
        self.run_vidupScript()

    def start_gui(self):
        self.master.mainloop()

    def create_widgets(self):
        self.pack(fill=BOTH, expand=1)
        self.master.bind('<Return>', self.return_key)

        bottomFrame = Frame(self, borderwidth=1)
        bottomFrame.pack(side=BOTTOM, fill=X)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(side=TOP, fill=BOTH, expand=1)

        self.exitBtn = Button(bottomFrame, text="Exit", width=12,command=self.quit)
        self.exitBtn.pack(side=RIGHT, padx=5, pady=5)

        self.runBtn = Button(bottomFrame, text="Run", width=12, command=self.run_vidupScript)
        self.runBtn.pack(side=RIGHT, padx=5)

        self.defaultsBtn = Button(bottomFrame, text="Defaults", width=12, command=self.feildDefaults)
        self.defaultsBtn.pack(side=LEFT, padx=5)

        self.clearConsoleBtn = Button(bottomFrame, text="Clear Console", width=12, command=self.clearConsole)
        self.clearConsoleBtn.pack(side=LEFT, padx=5)

        group = LabelFrame(frame, text="Video & Manifest Source", padx=5, pady=5)
        group.pack(padx=5, pady=5, fill=X)

        group1 = LabelFrame(frame, text="Database File", padx=5, pady=5)
        group1.pack(padx=5, pady=5, fill=X)

        group2 = LabelFrame(frame, text="Video Destination", padx=5, pady=5)
        group2.pack(padx=5, pady=5, fill=X)

        group3 = LabelFrame(frame, text="Console", padx=5, pady=5)
        group3.pack(padx=5, pady=5, fill=BOTH, expand=1)
        
####        menubar = Menu(self)
####        filemenu = Menu(menubar)
####        filemenu.add_command(label='Calculate', command=self.calculate)
####        filemenu.add_command(label='Reset', command=self.clear)
####        menubar.add_cascade(label='File', menu=filemenu)
####        menubar.add_command(label='Quit', command=self.quit)
####        root.config(menu=menubar)

        self.consoleWindowScrollb = Scrollbar(group3)
        self.consoleWindowScrollb.pack(side=RIGHT, fill=Y)

        self.consoleWindow = Text(group3, wrap='word', state=DISABLED)
        self.consoleWindow.pack(side=LEFT, fill=BOTH, expand=1)

        #interconnect scrollbar and consolewindow
        self.consoleWindow.config(yscrollcommand=self.consoleWindowScrollb.set)
        self.consoleWindowScrollb.config(command=self.consoleWindow.yview)

        testtext = Text(frame,bd=3, width=145, height=30, undo=True)

        self.videoSrcTxt = Entry(group)
        self.videoSrcTxt.pack(side=LEFT, padx=5, fill=X, expand=1)
        self.videoSrcTxt.focus_set()

        self.folderButtonIcon = PhotoImage(data=self.folderButtonIconData)
        self.dbButtonIcon = PhotoImage(data=self.dbButtonIconData)
        
        self.videoSrcTxtBrowseBtn = Button(group, image=self.folderButtonIcon, command=self.select_videoAndManifestSource)
        self.videoSrcTxtBrowseBtn.pack(side=RIGHT)

        self.dbSrcTxt = Entry(group1)
        self.dbSrcTxt.pack(side=LEFT, padx=5, fill=X, expand=1)

        self.dbSrcTxtBrowseBtn = Button(group1, image=self.dbButtonIcon, command=self.select_db)
        self.dbSrcTxtBrowseBtn.pack(side=RIGHT)

        self.videoDestTxt = Entry(group2)
        self.videoDestTxt.pack(side=LEFT, padx=5, fill=X, expand=1)

        self.videoDestTxtBtn = Button(group2, image=self.folderButtonIcon, command=self.select_videoDestination)
        self.videoDestTxtBtn.pack(side=RIGHT)

##        self.exitBtn = Button(self, text="Exit", width=10,command=self.quit)
##        self.exitBtn.pack(side=RIGHT, padx=5, pady=5)
##
##        self.runBtn = Button(self, text="Run", width=10, command=self.run_vidupScript)
##        self.runBtn.pack(side=RIGHT, padx=5)
##
##        self.defaultsBtn = Button(self, text="Defaults", width=10, command=self.feildDefaults)
##        self.defaultsBtn.pack(side=LEFT, padx=5)        

    def select_videoAndManifestSource(self):
        dirpath = tkFileDialog.askdirectory(parent=self,initialdir="/",\
                    title="Copy videos from:", mustexist=True)
        self.videoSrcTxt.delete(0,END)
        self.videoSrcTxt.insert(0, dirpath)

    def select_db(self):
        filepath = tkFileDialog.askopenfilename(parent=self, title="Please select the database file")
        self.dbSrcTxt.delete(0,END)
        self.dbSrcTxt.insert(0, filepath)

    def select_videoDestination(self):
        dirpath = tkFileDialog.askdirectory(parent=self,initialdir="/",\
                   title="Copy videos to:", mustexist=True)
        self.videoDestTxt.delete(0,END)
        self.videoDestTxt.insert(0, dirpath)

    def feildDefaults(self):
        #self.writeToConsole("set defaults")
        self.videoSrcTxt.delete(0,END)
        #self.videoSrcTxt.insert(0, "")
        
        self.dbSrcTxt.delete(0,END)
        self.dbSrcTxt.insert(0, self.dbFile)
        
        self.videoDestTxt.delete(0,END)
        self.videoDestTxt.insert(0, self.vidDest)

    def run_vidupScript(self):

        #check that all fields have been completed
        videoSrcTxt = self.videoSrcTxt.get()
        dbSrcTxt = self.dbSrcTxt.get()
        videoDestTxt = self.videoDestTxt.get()
        
        if len(videoSrcTxt) < 1 or len(dbSrcTxt) < 1 or len(videoDestTxt) < 1:
            tkMessageBox.showwarning(
                "Incomplete",
                "Please ensure that all fields have been completed and try again.")
        else:
            self.vidup.set_vidSource( videoSrcTxt )
            self.vidup.set_dbFile( dbSrcTxt)
            self.vidup.set_vidDest( videoDestTxt )
        
            self.vidup.runVideoUpload()

    def writeToConsole(self, theMsg):
        self.consoleWindow.config(state=NORMAL)
        self.consoleWindow.insert(END, theMsg+"\n")
        self.consoleWindow.see(END)
        self.consoleWindow.config(state=DISABLED)

    def clearConsole(self):
        self.consoleWindow.config(state=NORMAL)
        self.consoleWindow.delete("1.0",END)
        self.consoleWindow.config(state=DISABLED)

    def quit(self):
        #self.mainwindow.quit()
        self.master.destroy()

        if os.path.exists(self.tempIconFile.name):
            os.remove(self.tempIconFile.name)
##            if os.path.exists(self.tempIconFile.name)==False:


if __name__ == "__main__": #only run the code below if this file is run as a standalone module, ie. not imported
    app = Videouploadgui()
    app.start_gui()
    #root.destroy()
##except:
##    theErr = str(sys.exc_info())   
##    with open('videoUploadGUI.log', 'a+') as f:
##        f.writelines((time.strftime("%d/%m/%Y"))+" "+(time.strftime("%H:%M:%S"))+" "+theErr+"\n")
##    raise
