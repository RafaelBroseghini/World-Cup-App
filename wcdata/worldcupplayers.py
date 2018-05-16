# import sqlite3
import records
db = records.Database("sqlite:///./worldcupplayers.db")

# db = conn.cursor()

db.query('''CREATE TABLE worldcupplayers (roundid int, matchid int, teaminit text,  coach text,  lineup text, shirtnumber int,
playername text,  position text, event text)''')

with open("WorldCupPlayers.csv") as file:
    for line in file:
        line = line.split(",")
        line[8] = line[8].replace('\n',"")
        for i in range(0,len(line)):
            line[i] = line[i].replace("'","")
        print(line)
        db.query('''INSERT INTO worldcupplayers VALUES({},{},{},{},{},{},{},{},{})'''.format("'"+line[0]+"'","'"+line[1]+"'",
        "'"+line[2]+"'","'"+line[3]+"'","'"+line[4]+"'","'"+line[5]+"'  ","'"+line[6]+"'","'"+line[7]+"'","'"+line[8]+"'"))

# conn.commit()

# conn.close()