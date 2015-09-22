"""
Video upload tool reads a file containing a JSON array of all the .mp4 videos in the 
specified root folder as JSON objects.
"""

import sqlite3
import json
import re
import shutil
import glob

# descriptions for classes
classList = {"p1":"Primary One", "p2":"Primary Two", "p3":"Primary Three", "p4":"Primary Four", "p5":"Primary Five", "p6":"Primary Six"}

# descriptions for subjects
subjectList = {"mth":"Mathematics", "eng":"English", "bsc":"Basic Science"}

# description for terms
termList = {"f":"First Term", "s":"Second Term", "t":"Third Term"}

user_input = raw_input("Enter the path to copy video(s) from: ")

# connects to database
#conn = sqlite3.connect("/home/voti/ka-lite-master/kalite/database/data.sqlite")

conn = sqlite3.connect("C:/Users/Ola/Desktop/NG/Dev/projects/python/viduptool/data1.sqlite")
curs = conn.cursor()

### create tables
curs.execute('''DROP TABLE IF EXISTS Class''')
curs.execute("CREATE TABLE Class(id text,desc text,primary key(id));")

curs.execute('''DROP TABLE IF EXISTS Subject''')
curs.execute("CREATE TABLE Subject(id text,desc text,primary key(id));")

curs.execute('''DROP TABLE IF EXISTS Term''')
curs.execute("CREATE TABLE Term(id text,desc text,primary key(id));")

curs.execute('''DROP TABLE IF EXISTS Theme''')
curs.execute("CREATE TABLE Theme(cstid text,themeid text,desc text);")

curs.execute('''DROP TABLE IF EXISTS Topic''')
curs.execute("CREATE TABLE Topic(cst_themeid text,topicid text,desc text);")

# create lesson tables for 13 weeks
# for all three terms i.e 1st - 3rd term



# open a json file
with open('manifest.iq') as data_file:
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
    
    # dynamically creates table name
    # from manifest file
    table_name = vclass+"_"+subject+"_"+term    #Lesson table
    curs.execute("CREATE TABLE if not exists " + table_name + "(id text,lessonid text,desc text,primary key(id,lessonid));")
    
    # make id and videoid composite keys
    video_table = table_name +"_video"          #Video table
    curs.execute("CREATE TABLE if not exists " + video_table + "(id text,videoid text,title text,filename text,primary key(id,videoid));")
    
    
    #creates the file name with the required format
    class_subj_term_theme_topic_lesson_lessonpart = vclass+"_"+subject+"_"+term+"_"+theme+"_"+topic+"_"+lesson+"_"+lesson_part
        
    # do an insert into the created table above with attributes from the json file
    curs.execute('''insert or ignore into Class(id,desc) values(?,?)''',(vclass,classList[vclass]))
    curs.execute('''insert or ignore into Subject(id, desc) values(?,?)''',(subject, subjectList[subject]))
    curs.execute('''insert or ignore into Term(id, desc) values(?,?)''',(term, termList[term])) 
    curs.execute('''insert or ignore into Theme(themeid) values(?)''',[theme])
    curs.execute('''insert or ignore into Topic(topicid) values(?)''',[topic])
    
    # check for pattern and extract desired section for each file name
    #print  class_subj_term_week_lesson_lessonpart
    match = re.search('([\w.-]+)_([\w.-]+)_([\w.-]+)_([\w.-]+)_([\w.-]+)_([\w.-]+)_([\w.-]+)', class_subj_term_theme_topic_lesson_lessonpart)
    if match:
        classx = match.group(1)
        subjectx = match.group(2)
        termx = match.group(3)
        themex = match.group(4)
        topicx = match.group(5)
        lessonx = match.group(6)
        lessonpartx = match.group(7)
        print classx, " ", subjectx, " ",termx, " ", themex, " ", topicx, " ", lessonx, " ", lessonpartx


        # for math, bsc and eng first term
        csttt_id = classx+"_"+subjectx+"_"+termx+"_"+themex+"_"+topicx
        lessonid = lessonx
        cstttl_id = csttt_id+"_"+lessonid
        lessonpart  = lessonpartx
        theLessonTable = classx+"_"+subjectx+"_"+termx
        theVideoTable = theLessonTable+"_video"
        curs.execute("insert or ignore into "+theLessonTable+"(id,lessonid,desc) values(?,?,?)",(csttt_id,lessonid,"some description"))
        
        title = 'dummy title for now'
        filename = classx+"_"+subjectx+"_"+termx+"_"+themex+"_"+topicx+"_"+lessonid+"_"+lessonpart + file_format
        curs.execute("insert or ignore into "+theVideoTable+"(id,videoid,title,filename)\
        values(?,?,?,?)",(cstttl_id,lessonpart,title,filename))
        
        conn.commit()
            
###loop through the folder for mp4 movies and copy them to the designated folder.
##movies = glob.glob(user_input+"/*.mp4") #video source
##designated_dest = "/home/voti/ka-lite-master/vids" #videos designated destination
##
##for movie in movies:
##    shutil.copy(movie,designated_dest)
## 
##            
