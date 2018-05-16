import requests
import records
from flask import Flask, Response, request, render_template, jsonify
from flask_bootstrap import Bootstrap
from worldcup import *

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/home")
def home():
    groups = get_groups_wc_18()
    winners = get_winners()
    data = get_years()
    return render_template("index.html", years = data, winners=winners, groups = groups)

@app.route("/getworldcup")
def process_form():
    participants = get_teams_in_wc()
    print(participants)
    res = get_info_on_year()
    fun_facts = get_fun_facts()
    news = requests.get("https://newsapi.org/v2/everything?sources=espn,bbc-sport&q=fifa+world+cup+"+res[1]+"&apiKey=36071cd47bf64942aeb3ae57d16f664c").json()
    return render_template("list.html", data=res[0], news=news, year=res[1], participants=participants, wc_instace = res[0][0][1], high_score = fun_facts[0:2], hosts=fun_facts[2])

@app.route("/get_roster")
def process_roster():
    players = get_roster_from_country()
    matches = get_matches_in_year()
    roster = build_roster(matches, players)
    stats = build_stats(roster)
    return render_template("roster.html", roster=stats)

@app.route("/get_cities")
def show_cities():
    cities = get_cities()
    return jsonify(cities)

if __name__ == '__main__':
    app.run(debug=True)
