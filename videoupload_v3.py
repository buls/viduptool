import sqlite3
import json
import re
import shutil
import glob

user_input = raw_input("Enter the path to copy video(s) from: ")

# connects to database
conn = sqlite3.connect("/home/voti/ka-lite-master/kalite/database/data.sqlite")
curs = conn.cursor()

# create a tables
#curs.execute('''DROP TABLE table_name''')
#curs.execute("CREATE TABLE table_name(col1,col2,col3);")

# create a tables
curs.execute('''DROP TABLE IF EXISTS Class''')
curs.execute("CREATE TABLE Class(id text,desc text,primary key(id));")
curs.execute('''DROP TABLE IF EXISTS Subject''')
curs.execute("CREATE TABLE Subject(id text,desc text,primary key(id));")
curs.execute('''DROP TABLE IF EXISTS Term''')
curs.execute("CREATE TABLE Term(id text,desc text,primary key(id));")
curs.execute('''DROP TABLE IF EXISTS Week''')
curs.execute("CREATE TABLE Week(id text,desc text,primary key(id));")
# create lesson tables for 13 weeks
# for all three terms i.e 1st - 3rd term



# open a json file
with open('video/manifest.iq') as data_file:
    data = json.load(data_file)

#loop through the json file and get its attribute 
check = 0   
for i in data:
    term = i['term']
    file_format = i['file_format']
    term_week = i['term_week']
    vclass = i['vclass']
    lesson_part = i['lesson_part']
    lesson = i['lesson']
    subject = i['subject']
    
    # dynamically creates table name
    # from manifest file
    table_name = vclass+"_"+subject+"_"+term
    #print table_name
    #make id and lessonid composite keys
    #curs.execute('''DROP TABLE IF EXISTS '''+ table_name)
    curs.execute("CREATE TABLE if not exists " + table_name + "(id text,lessonid text,desc text,primary key(id,lessonid));")
    
    # make id and videoid composite keys
    video_table = table_name +"_video"
    #print video_table
    #curs.execute('''DROP TABLE IF EXISTS p1_mth_f_01_video''')
    curs.execute("CREATE TABLE if not exists " + video_table + "(id text,videoid text,title text,filename text,primary key(id,videoid));")
    
    
    #creates the file name with the required format
    class_subj_term_week_lesson_lessonpart = vclass+"_"+subject+"_"+term+"_"+term_week+"_"+lesson+"_"+lesson_part
    # do an insert into the created table above with attributes from the json file
    curs.execute('''insert or ignore into Class(id) values(?)''',[vclass])
    curs.execute('''insert or ignore into Subject(id) values(?)''',[subject])
    curs.execute('''insert or ignore into Term(id) values(?)''',[term]) 
    curs.execute('''insert or ignore into Week(id) values(?)''',[term_week])
    
    # check for pattern and extract desired section for each file name
    #print  class_subj_term_week_lesson_lessonpart
    match = re.search('([\w.-]+)_([\w.-]+)_([\w.-]+)_([\w.-]+)_([\w.-]+)_([\w.-]+)', class_subj_term_week_lesson_lessonpart)
    if match:
        classx = match.group(1)
        subjectx = match.group(2)
        termx = match.group(3)
        weekx = match.group(4)
        lessonx = match.group(5)
        lessonpartx = match.group(6)
        #print weekx
        
        # for math, bsc and eng first term
        if (classx == 'p1') and (subjectx == 'mth') and (termx == 'f'):
            idx = classx+"_"+subjectx+"_"+termx+"_"+weekx
            lessonid = lessonx
            idxx = idx+"_"+lessonid
            lessonpart  = lessonpartx
            print idxx
            curs.execute('''insert or ignore into p1_mth_f(id,lessonid) values(?,?)''',(idx,lessonid))
            
            title = 'dummy title for now'
            filename = classx+"_"+subjectx+"_"+termx+"_"+weekx+"_"+lessonid+"_"+lessonpart + file_format
            curs.execute('''insert or ignore into p1_mth_f_video(id,videoid,title,filename)\
            values(?,?,?,?)''',(idxx,lessonpart,title,filename))
            
        if (classx == 'p1') and (subjectx == 'eng') and (termx == 'f'):
            idx = classx+"_"+subjectx+"_"+termx+"_"+weekx
            lessonid = lessonx
            idxx = idx+"_"+lessonid
            lessonpart  = lessonpartx
            print idxx
            curs.execute('''insert or ignore into p1_eng_f(id,lessonid) values(?,?)''',(idx,lessonid))
            
            title = 'dummy title for now'
            filename = classx+"_"+subjectx+"_"+termx+"_"+weekx+"_"+lessonid+"_"+lessonpart + file_format
            curs.execute('''insert or ignore into p1_eng_f_video(id,videoid,title,filename)\
            values(?,?,?,?)''',(idxx,lessonpart,title,filename))  
            
        if (classx == 'p1') and (subjectx == 'bsc') and (termx == 'f'):
            idx = classx+"_"+subjectx+"_"+termx+"_"+weekx
            lessonid = lessonx
            idxx = idx+"_"+lessonid
            lessonpart  = lessonpartx
            print idxx
            curs.execute('''insert or ignore into p1_bsc_f(id,lessonid) values(?,?)''',(idx,lessonid))
            
            title = 'dummy title for now'
            filename = classx+"_"+subjectx+"_"+termx+"_"+weekx+"_"+lessonid+"_"+lessonpart + file_format
            curs.execute('''insert or ignore into p1_bsc_f_video(id,videoid,title,filename)\
            values(?,?,?,?)''',(idxx,lessonpart,title,filename))        
            conn.commit()
            
            
#loop through the folder for mp4 movies and copy them to the designated folder.
movies = glob.glob(user_input+"/*.mp4") #video source
designated_dest = "/home/voti/ka-lite-master/vids" #videos designated destination

for movie in movies:
    shutil.copy(movie,designated_dest)
 
            
