import sqlite3
conn = sqlite3.connect("groups18.db")

cur = conn.cursor()

cur.execute("CREATE TABLE groups18 (gp text, t1 text, t2 text, t3 text, t4 text)")

with open("groups.csv") as file:
    for line in file:
        line = line.split(",")
        line[4] = line[4].replace('\n',"")
        for i in range(0,len(line)):
            line[i] = line[i].replace("'","")
        print(line)
        cur.execute('''INSERT INTO groups18 VALUES({},{},{},{},{})'''.format("'"+line[0]+"'","'"+line[1]+"'",
        "'"+line[2]+"'","'"+line[3]+"'","'"+line[4]+"'"))

conn.commit()

conn.close()