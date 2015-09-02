import csv, sqlite3
import os,sys
import shutil
import glob

user_input = raw_input("Enter the path of your video: ") 

conn = sqlite3.connect("test.db")
curs = conn.cursor()
curs.execute('''DROP TABLE PCFC''')
curs.execute("CREATE TABLE PCFC (id INTEGER PRIMARY KEY, type INTEGER, term TEXT, definition TEXT);")
reader = csv.reader(open(user_input+'/manifest.txt', 'r'), delimiter='|')
for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    curs.execute("INSERT INTO PCFC (type, term, definition) VALUES (?, ?, ?);", to_db)
conn.commit()

meta = curs.execute("select * from PCFC")
for r in meta:
    print r
    
#loop through the folder for mp4 movies and copy them to the designated folder.
movies = glob.glob(user_input+"/*.mp4") #video source
designated_dest = "/video"				#videos designated destination

for movie in movies:
	shutil.copy(movie,designated_dest)