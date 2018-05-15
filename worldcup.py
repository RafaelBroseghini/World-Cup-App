import sqlite3
from flask import request

def get_years():
    conn = sqlite3.connect("wcdata/worldcups.db")
    cur = conn.cursor()
    cur.execute("select distinct(year) from worldcups")
    res = cur.fetchall()
    return res

def get_groups_wc_18():
    conn = sqlite3.connect("wcdata/groups18.db")
    cur = conn.cursor()
    cur.execute("SELECT * from groups18")
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
    conn = sqlite3.connect("wcdata/worldcups.db")
    cur = conn.cursor()
    cur.execute("select winner, count(winner) from worldcups group by winner ORDER BY COUNT(winner) DESC;")
    res = cur.fetchall()
    return res

def get_fun_facts():
    fun_facts_lst = []
    conn = sqlite3.connect("wcdata/worldcupsmatches.db")
    cur = conn.cursor()
    year = request.args.get("q")
    cur.execute("select hometeaminit, hometeamgoals, awayteaminit, max(awayteamgoals) from worldcupsmatches where year = "+year+"")
    res = cur.fetchall()
    fun_facts_lst.append(res)
    cur.execute("select hometeaminit, max(hometeamgoals), awayteaminit, awayteamgoals from worldcupsmatches where year = "+year+"")
    res = cur.fetchall()
    fun_facts_lst.append(res)
    cur.execute("select distinct(city) from worldcupsmatches where year = "+year+"")
    res = cur.fetchall()
    fun_facts_lst.append(res)
    return fun_facts_lst

def get_teams_in_wc():
    counter_dict = {}
    year = request.args.get("q")
    conn = sqlite3.connect("wcdata/worldcupsmatches.db")
    cur = conn.cursor()
    cur.execute("select hometeam, hometeaminit from worldcupsmatches where year = "+year+"")
    home_teams = cur.fetchall()
    cur.execute("select awayteam, awayteaminit from worldcupsmatches where year = "+year+"")
    away_teams = cur.fetchall()
    teams = [home_teams, away_teams]
    for i in range(len(teams)):
        for d in teams[i]:
            if d[0] not in counter_dict:
                counter_dict[d[0]] = d[1]
    return counter_dict

def get_roster_from_country():
    country = request.args.get("team")
    conn = sqlite3.connect("wcdata/worldcupplayers.db")
    cur = conn.cursor()
    cur.execute('''select matchid, playername, event, shirtnumber from worldcupplayers where teaminit = {}'''.format("'"+country+"'"))
    players = cur.fetchall()
    return players

def get_matches_in_year():
    year = request.args.get("year")
    conn = sqlite3.connect("wcdata/worldcupsmatches.db")
    cur = conn.cursor()
    cur.execute('''select matchid, date_txt from worldcupsmatches where year = {}'''.format("'"+year+"'"))
    matches = cur.fetchall()
    return matches

def build_roster(lst1, lst2):
    matches_dict = {}
    players_dict = {}
    for date in lst1:
        if date[0] not in matches_dict:
            matches_dict[date[0]] = 1
    for p in lst2:
        for m in matches_dict:
            if p[0] == m and p[1] not in players_dict:
                if p[2] != "":
                    players_dict[p[1]] = {p[2]:1,"Number":p[3]}
                else:
                    players_dict[p[1]] = {"Number":p[3]}
            elif p[1] in players_dict and p[2] != "" and p[0] == m:
                players_dict[p[1]][p[2]] = 1 
    return players_dict

def build_stats(roster):
    stats_dict = {}
    for player in roster:
        stats_dict[player] = {"Number":roster[player]["Number"], "Goals": 0, "Yellow Cards": 0, "Red Cards":0}
        for stat in roster[player]:
            for l in stat:
                if l == "G"or l == "P":
                    stats_dict[player]["Goals"] += 1
                elif l == "Y":
                    stats_dict[player]["Yellow Cards"] += 1
                elif l == "R":
                    stats_dict[player]["Red Cards"] += 1

    return stats_dict
    