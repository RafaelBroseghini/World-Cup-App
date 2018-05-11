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
    return render_template("index.html.j2", years = data, winners=winners)

@app.route("/getworldcup")
def process_form():
    participants = get_teams_in_wc()
    res = get_info_on_year()
    print(res)
    news = requests.get("https://newsapi.org/v2/everything?sources=espn,bbc-sport&q=fifa+world+cup+"+res[1]+"&apiKey=36071cd47bf64942aeb3ae57d16f664c").json()
    return render_template("list.html.j2", data=res[0], news=news, year=res[1], participants=participants, wc_instace = res[0][0][1])

if __name__ == '__main__':
    app.run(debug=True)
