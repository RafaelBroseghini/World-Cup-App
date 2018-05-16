import records
from flask import request

def get_years():
    db = records.Database('sqlite:///wcdata/worldcups.db')
    rows = db.query('select distinct(year) from worldcups').all()
    return rows

def get_groups_wc_18():
    db = records.Database('sqlite:///wcdata/groups18.db')
    rows = db.query("SELECT * from groups18").all()
    return rows

def get_info_on_year():
    year = request.args.get("q")
    db = records.Database('sqlite:///wcdata/worldcups.db')
    rows = db.query("select * from worldcups where year = "+year+"").all()
    return rows, year

def get_winners():
    db = records.Database('sqlite:///wcdata/worldcups.db')
    rows = db.query("select winner, count(winner) from worldcups group by winner ORDER BY COUNT(winner) DESC;").all()
    return rows

def get_fun_facts():
    year = request.args.get("q")
    fun_facts_lst = []
    db = records.Database('sqlite:///wcdata/worldcupsmatches.db')
    res = db.query("select hometeaminit, hometeamgoals, awayteaminit, max(awayteamgoals) from worldcupsmatches where year = "+year+"").all()
    fun_facts_lst.append(res)
    res = db.query("select hometeaminit, max(hometeamgoals), awayteaminit, awayteamgoals from worldcupsmatches where year = "+year+"")
    fun_facts_lst.append(res)
    res = db.query("select distinct(city) from worldcupsmatches where year = "+year+"")
    fun_facts_lst.append(res)
    return fun_facts_lst

def get_teams_in_wc():
    counter_dict = {}
    year = request.args.get("q")
    db = records.Database('sqlite:///wcdata/worldcupsmatches.db')
    home_teams = db.query("select hometeam, hometeaminit from worldcupsmatches where year = "+year+"").all()
    db = records.Database('sqlite:///wcdata/worldcupsmatches.db')
    away_teams = db.query("select awayteam, awayteaminit from worldcupsmatches where year = "+year+"").all()
    teams = [home_teams, away_teams]
    for i in range(len(teams)):
        for d in teams[i]:
            if d[0] not in counter_dict:
                counter_dict[d[0]] = d[1]
    return counter_dict

def get_roster_from_country():
    country = request.args.get("team")
    db = records.Database('sqlite:///wcdata/worldcupplayers.db')
    players = db.query('''select matchid, playername, event, shirtnumber from worldcupplayers where teaminit = {}'''.format("'"+country+"'")).all()
    return players

def get_matches_in_year():
    year = request.args.get("year")
    db = records.Database('sqlite:///wcdata/worldcupsmatches.db')
    matches = db.query('''select matchid, date_txt from worldcupsmatches where year = {}'''.format("'"+year+"'")).all()

    return matches

def get_cities():
    cities = {}
    year = request.args.get("y")
    db = records.Database("sqlite:///wcdata/worldcupsmatches.db")
    rows = db.query("select distinct(city) from worldcupsmatches where year = "+year+"").all()
    for i in range(0,len(rows)):
        cities["City"+str(i)] = rows[i][0] 
    return cities

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
    