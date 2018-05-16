# import sqlite3
import records
db = records.Database("sqlite:///./worldcupsmatches.db")

# cur = conn.cursor()

db.query('''CREATE TABLE worldcupsmatches (year text, date_txt text,  stage text,  stadium text,  city text,  hometeam text,
hometeamgoals int,  awayteamgoals int,  awayteam text,  winconditions text, attendance real, hthomegoals int, htawaygoals int,
referee text, assistant1 text, assistant2 text, roundid int, matchid int, hometeaminit text, awayteaminit text)''')

with open("WorldCupMatches.csv") as file:
    count = 0
    for line in file:
        line = line.split(",")
        line[19] = line[19].replace('\n',"")
        for i in range(0,len(line)):
            line[i] = line[i].replace('"',"")
        print(line)
        db.query('''INSERT INTO worldcupsmatches VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})'''.format('"'+line[0]+'"',"'"+line[1]+"'",
        '"'+line[2]+'"',"'"+line[3]+"'","'"+line[4]+"'","'"+line[5]+"'  ","'"+line[6]+"'",'"'+line[7]+'"',"'"+line[8]+"'",
        "'"+line[9]+"'","'"+line[10]+"'",'"'+line[11]+'"','"'+line[12]+'"','"'+line[13]+'"','"'+line[14]+'"','"'+line[15]+'"',
        '"'+line[16]+'"','"'+line[17]+'"','"'+line[18]+'"','"'+line[19]+'"'))

# conn.commit()

# conn.close()
