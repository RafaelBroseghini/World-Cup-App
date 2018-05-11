import sqlite3
from flask import request

def get_years():
    conn = sqlite3.connect("wcdata/worldcups.db")
    cur = conn.cursor()
    cur.execute("select distinct(year) from worldcups")
    res = cur.fetchall()
    return res

def get_info_on_year():
    conn = sqlite3.connect("wcdata/worldcups.db")
    cur = conn.cursor()
    year = request.args.get("q")
    cur.execute("select * from worldcups where year = "+year+"")
    res = cur.fetchall()
    return res, year

def get_winners():
    year = request.args.get("q")
    conn = sqlite3.connect("wcdata/worldcups.db")
    cur = conn.cursor()
    cur.execute("select winner, count(winner) from worldcups group by winner ORDER BY COUNT(winner) DESC;")
    res = cur.fetchall()
    return res

def get_teams_in_wc():
    counter_dict = {}
    year = request.args.get("q")
    conn = sqlite3.connect("wcdata/worldcupsmatches.db")
    cur = conn.cursor()
    cur.execute("select hometeam, awayteam from worldcupsmatches where year = "+year+"")
    participants = cur.fetchall()
    for d in participants:
        for team in d:
            if team not in counter_dict:
                counter_dict[team] = 1
    return counter_dict
