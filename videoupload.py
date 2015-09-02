import csv, sqlite3
import os,sys
import shutil
import glob


user_input = raw_input("Enter the path to copy video(s) from: ")
# open a file
#thisfile = os.open(user_input+"/manifest.txt",os.O_RDWR)
# reading text
#output = os.read(thisfile,100)
#print output

#source = user_input #video source
#designated_dest = "/video"
#shutil.move(source, designated_dest)  


conn = sqlite3.connect("test.db")
curs = conn.cursor()
curs.execute('''DROP TABLE PCFC''')
curs.execute("CREATE TABLE PCFC (id INTEGER PRIMARY KEY, type INTEGER, term TEXT, definition TEXT);")
reader = csv.reader(open(user_input+'/manifest.txt', 'r'), delimiter=',')
for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    curs.execute("INSERT INTO PCFC (type, term, definition) VALUES (?, ?, ?);", to_db)
conn.commit()

data = curs.execute("select * from PCFC")
for rel in data:
    print rel
    
#loop through the folder for mp4 movies and copy them to the designated folder.
movies = glob.glob(user_input+"/*.mp4") #video source
designated_dest = "/home/voti/django/iQ_Script/video2"				#videos designated destination

for movie in movies:
	shutil.copy(movie,designated_dest)
