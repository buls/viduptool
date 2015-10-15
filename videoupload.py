import sqlite3, json, shutil, sys

class Videoupload(object):  

    def validDescription(self, theSQL, theID=""):
                validity = False
                self.curs.execute(theSQL)
                result=self.curs.fetchone()
                try:
                   if result[0] is None: #no description
                       self.print_to(theID+"is in the database but has no description.")
                       validity = False
                   else:                 #description exists
                       validity =  True
                except:                  #no matching id in table
                       self.print_to(theID+" is not in the database.")
                       validity =  False
                return validity
    """Checks the given table for a description to the specified id"""

    def __init__(self, vidupGUI=None):

        self.vidupGUI = vidupGUI #a handle to the GUI object

        self.set_dbFile("C:/Users/Ola/Desktop/NG/Dev/projects/python/viduptoolWorking/data1.sqlite")
        #dbFile = "/home/pi/iq/kalite/database/data.sqlite" #on the pi

        self.set_vidDest("C:/1d")
        #vidDest = "/home/pi/iq/kalite/distributed/static/iqcontent/videos" #on the pi

    def print_to(self, theStr): #console or gui depending on which is running
        if __name__ == "__main__":
            print(theStr)
        else:
            self.vidupGUI.writeToConsole(theStr)

    def set_vidSource(self, vidSource):
        self.vidSource = vidSource

    def set_dbFile(self, dbFile):
        self.dbFile = dbFile

    def get_dbFile(self):
        return self.dbFile

    def set_vidDest(self, vidDest):
        self.vidDest = vidDest

    def get_vidDest(self):
        return self.vidDest

    def runVideoUpload(self):
        # connect to database
        self.conn = sqlite3.connect(self.dbFile)
        self.curs = self.conn.cursor()

        # open the (json) manifest file
        #self.print_to(vidSource+'/manifest.iq')
        with open(self.vidSource+'/manifest.iq') as data_file:
            self.data = json.load(data_file)

        #loop through the json file and get its attribute
        check = 0
        for i in self.data:
            self.term = i['term']
            self.file_format = i['file_format']
            self.theme = i['theme']
            self.vclass = i['vclass']
            self.lesson_part = i['lesson_part']
            self.lesson = i['lesson']
            self.subject = i['subject']
            self.topic = i['topic']
            self.videotitle = i['videotitle']

            self.lesson_table = self.vclass+"_"+self.subject+"_"+self.term

            self.video_table = self.lesson_table +"_video"
                
            #1 CLASS:
            self.theClassSQL = "select desc from Class where id = '{0}'".format(self.vclass)

            #2 SUBJECT
            self.theSubjectSQL = "select desc from Subject where id = '{0}'".format(self.subject)

            #3 TERM
            self.theTermSQL = "select desc from Term where id = '{0}'".format(self.term)

            #4 THEME
            self.cstid = self.vclass+"_"+self.subject+"_"+self.term
            self.theThemeSQL = "select desc from Theme where cstid = '{0}' AND themeid = '{1}'".format(self.cstid, self.theme)

            #5 TOPIC
            self.cst_themeid = self.cstid+"_"+self.theme
            self.theTopicSQL = "select desc from Topic where cst_themeid = '{0}' AND topicid = '{1}'".format(self.cst_themeid, self.topic)

            #6 LESSSON
            self.csttt_id = self.vclass+"_"+self.subject+"_"+self.term+"_"+self.theme+"_"+self.topic
            self.cstttl_id = self.csttt_id+"_"+self.lesson
            self.theLessonTable = self.vclass+"_"+self.subject+"_"+self.term
            self.theLessonSQL = "select desc from {0} where id = '{1}' AND lessonid = '{2}'".format(self.theLessonTable, self.csttt_id, self.lesson)

            #7 VIDEO, add video to video table if it has valid Class, Subject, Term, Theme, Topic and Lesson descriptions
            if self.validDescription(self.theClassSQL, self.vclass) and self.validDescription(self.theSubjectSQL, self.subject)\
               and self.validDescription(self.theTermSQL, self.term) and self.validDescription(self.theThemeSQL, self.cstid+" "+self.theme)\
               and self.validDescription(self.theTopicSQL, self.cst_themeid+" "+self.topic) and self.validDescription(self.theLessonSQL, self.csttt_id+" "+self.lesson):

                self.theVideoTable = self.theLessonTable+"_video"
                filename = self.vclass+"_"+self.subject+"_"+self.term+"_"+self.theme+"_"+self.topic+"_"+self.lesson+"_"+self.lesson_part+"_"+self.videotitle+self.file_format
                self.curs.execute("insert or ignore into "+self.theVideoTable+"(id,videoid,title,filename)\
                values(?,?,?,?)",(self.cstttl_id,self.lesson_part,self.videotitle,filename))
                self.print_to("adding "+self.cstttl_id+" "+self.lesson_part+" "+filename+" to db")

                #copy to the designated folder
                movie = self.vidSource+"/"+filename #video source
                self.print_to("copying to iq: "+filename+"\n")
                shutil.copy(movie,self.vidDest)
            else:
                #filename = vclass+"_"+subject+"_"+term+"_"+theme+"_"+topic+"_"+lesson+"_"+lesson_part+"_"+videotitle+file_format
                self.print_to("failed: "+filename)
            self.conn.commit()

        self.print_to("DONE...")

#############################################################


if __name__ == "__main__": #only run the code below if this file is run as a standalone module, ie. not imported
    usage = "\t\tusage: 'videoupload -con' to run in console \n\t\tor 'videoupload -gui' to launch the graphical interface"

    if len(sys.argv) >= 2:
        
        if sys.argv[1] == "-gui" or sys.argv[1] == "/gui":
            print("loading GUI...")
            from videouploadgui import Videouploadgui
            app = Videouploadgui()
            app.start_gui()

        elif sys.argv[1] == "-help" or sys.argv[1] == "/help":
            print(usage)

        else:
            print("\n"+"invalid argument: "+"'"+sys.argv[1]+"'")
            print(usage)
    else:
        vidSource = raw_input("Enter the path to upload video(s) from: ")
        print("")
        vidup = Videoupload()
        vidup.set_vidSource(vidSource)
        vidup.runVideoUpload()
        raw_input("\npress ENTER to end...")
        
