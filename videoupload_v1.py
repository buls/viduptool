import json
import sqlite3
import shutil
import glob
from pprint import pprint

# prompts user where to copy video(s) from
user_input = raw_input("Enter the path to copy video(s) from: ")

# connects to database
conn = sqlite3.connect("test.db")
curs = conn.cursor()
curs.execute('''DROP TABLE iqsys''')
curs.execute("CREATE TABLE iqsys(term text,file_format TEXT,term_week TEXT,vlass text,lesson_part text,lesson text,subject text);")

with open('video/manifest.json') as data_file:
    data = json.load(data_file)
    
for i in data:
    term = i['term']
    file_format = i['file_format']
    term_week = i['term_week']
    vclass = i['vclass']
    lesson_part = i['lesson_part']
    lesson = i['lesson']
    subject = i['subject']
    print term + " " + file_format + " " + term_week + " " + vclass + " " + lesson_part + " " + lesson + " " + subject
    curs.execute('''insert into iqsys(term,file_format,term_week,vlass,lesson_part,lesson,subject)\
    values(?,?,?,?,?,?,?)''',(term,file_format,term_week,vclass,lesson_part,lesson,subject))
    conn.commit()
    
    
        
#loop through the folder for mp4 movies and copy them to the designated folder.
movies = glob.glob(user_input+"/*.mp4") #video source
#user_input2 = raw_input("Enter the path to copy video(s) to: ")
designated_dest = "/home/voti/django/iQ_Script/video2"	#videos designated destination

for movie in movies:
	shutil.copy(movie,designated_dest)
 
    
    
