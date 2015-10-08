#NOTE: Import and RUN from viduptoolgui.py
"""
    Video upload tool reads a file containing a JSON array of all the .mp4 videos in the 
    specified root folder as JSON objects.

    Update: YemiDaniel.07/10/2015
    1. Read the manifest.
    2. Then for each record, confirm that the IDs (class, subject, term, theme, topic, lesson) have a correcsponding description in the DB.
    3. and only if a description is returned for ALL, insert the video into the DB (video table)
    4. and copy from source to destination folder.
"""

def vidup(vidSource, dbFile, vidDest):
    #print("script imported")

    import sqlite3
    import json
    import shutil
    import glob

    # connects to database
    conn = sqlite3.connect(dbFile)
    curs = conn.cursor()

    def validDescription(theSQL, theID=""):
        validity = False
        curs.execute(theSQL)
        result=curs.fetchone()
        try:
           if result[0] is None: #no description
               print(theID+" has no description")
               validity = False
           else:                 #description exists
               validity =  True
        except:                  #no matching id in table
               print(theID+" is invalid")
               validity =  False
            
        return validity
    """Checks the given table for a description to the specified id"""


    # open the (json) manifest file
    print(vidSource+'/manifest.iq')
    with open(vidSource+'/manifest.iq') as data_file:
        data = json.load(data_file)

    #loop through the json file and get its attribute
    check = 0
    for i in data:
        term = i['term']
        file_format = i['file_format']
        theme = i['theme']
        vclass = i['vclass']
        lesson_part = i['lesson_part']
        lesson = i['lesson']
        subject = i['subject']
        topic = i['topic']
        videotitle = i['videotitle']

        lesson_table = vclass+"_"+subject+"_"+term

        video_table = lesson_table +"_video"
            
        #1 CLASS:
        theClassSQL = "select desc from Class where id = '{0}'".format(vclass)

        #2 SUBJECT
        theSubjectSQL = "select desc from Subject where id = '{0}'".format(subject)

        #3 TERM
        theTermSQL = "select desc from Term where id = '{0}'".format(term)

        #4 THEME
        cstid = vclass+"_"+subject+"_"+term
        theThemeSQL = "select desc from Theme where cstid = '{0}' AND themeid = '{1}'".format(cstid, theme)

        #5 TOPIC
        cst_themeid = cstid+"_"+theme
        theTopicSQL = "select desc from Topic where cst_themeid = '{0}' AND topicid = '{1}'".format(cst_themeid, topic)

        #6 LESSSON
        csttt_id = vclass+"_"+subject+"_"+term+"_"+theme+"_"+topic
        cstttl_id = csttt_id+"_"+lesson
        theLessonTable = vclass+"_"+subject+"_"+term
        theLessonSQL = "select desc from {0} where id = '{1}' AND lessonid = '{2}'".format(theLessonTable, csttt_id, lesson)

        #7 VIDEO, add video to video table if it has valid Class, Subject, Term, Theme, Topic and Lesson descriptions
        if validDescription(theClassSQL, vclass) and validDescription(theSubjectSQL, subject)\
           and validDescription(theTermSQL, term) and validDescription(theThemeSQL, cstid+" "+theme)\
           and validDescription(theTopicSQL, cst_themeid+" "+topic) and validDescription(theLessonSQL, csttt_id+" "+lesson):

            theVideoTable = theLessonTable+"_video"
            filename = vclass+"_"+subject+"_"+term+"_"+theme+"_"+topic+"_"+lesson+"_"+lesson_part+"_"+videotitle+file_format
            curs.execute("insert or ignore into "+theVideoTable+"(id,videoid,title,filename)\
            values(?,?,?,?)",(cstttl_id,lesson_part,videotitle,filename))
            print ("VALID video file: "+filename)
        else:
            filename = vclass+"_"+subject+"_"+term+"_"+theme+"_"+topic+"_"+lesson+"_"+lesson_part+"_"+videotitle+file_format
            print ("INVALID video file: "+filename)
        conn.commit()

    #loop through the folder for mp4 movies and copy them to the designated folder.
    movies = glob.glob(vidSource+"/*.mp4") #video source
    designated_dest = vidDest #"/home/voti/ka-lite-master/vids" #videos designated destination

    for movie in movies:
        shutil.copy(movie,designated_dest)

    print("\nDONE...")
