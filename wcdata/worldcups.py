import sqlite3


conn = sqlite3.connect("worldcups.db")

cur = conn.cursor()

cur.execute('''CREATE TABLE worldcups (year text, instance int, country text,  winner text,  runnerup text,  third text,  fourth text,
goalsscored int,  qualifiedteams int,  matchesplayed int,  attendance real)''')

with open("WorldCups.csv") as file:
    for line in file:
        line = line.split(",")
        line[9] = line[9].replace("\n","")
        cur.execute('''INSERT INTO worldcups VALUES({},{},{},{},{},{},{},{},{},{},{})'''.format('"'+line[0]+'"','"'+line[1]+'"',
        '"'+line[2]+'"','"'+line[3]+'"','"'+line[4]+'"','"'+line[5]+'"','"'+line[6]+'"','"'+line[7]+'"',
        '"'+line[8]+'"','"'+line[9]+'"','"'+line[10]+'"'))

conn.commit()

conn.close()
