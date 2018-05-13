import requests
import sqlite3
from flask import Flask, Response, request, render_template
from flask_bootstrap import Bootstrap
from worldcup import *

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    winners = get_winners()
    data = get_years()
    return render_template("index.html", years = data, winners=winners)

@app.route("/getworldcup")
def process_form():
    participants = get_teams_in_wc()
    res = get_info_on_year()
    news = requests.get("https://newsapi.org/v2/everything?sources=espn,bbc-sport&q=fifa+world+cup+"+res[1]+"&apiKey=36071cd47bf64942aeb3ae57d16f664c").json()
    print(news)
    return render_template("list.html", data=res[0], news=news, year=res[1], participants=participants, wc_instace = res[0][0][1])

@app.route("/get_roster")
def process_roster():
    players = get_roster_from_country()
    matches = get_matches_in_year()
    roster = build_roster(matches, players)
    stats = build_stats(roster)
    return render_template("roster.html", roster=stats)

if __name__ == '__main__':
    app.run(debug=True)
