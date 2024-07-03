import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


#def connect_db():
    #conn = sqlite3.connect(app.config['Registration_DB'])
#database
#DATABASE = Registration_DB.db
#DEBUG = True


#base
@app.route('/')
def spawn():
    return render_template("Spawn.html")

@app.route('/Registration')
def Registration():
    return render_template("Registration.html")



#Not work...
@app.route('/Login')
def Login():
    return render_template("Login.html")



#category
@app.route('/XBOX Console')
def XBOXConsole():
    return render_template("XBOX Console.html")

@app.route('/PS Console')
def PSConsole():
    return render_template("PS Console.html")

@app.route('/All Console')
def AllConsole():
    return render_template("All Console.html")

@app.route('/Mobile Games')
def MobileGames():
    return render_template("Mobile Games.html")

@app.route('/PC Games')
def PCGames():
    return render_template("PC Games.html")





@app.route('/LastNews')
def LastNews():
    return render_template("Last news.html")

@app.route('/AllNews')
def AllNews():
    return render_template("All news.html")


#news



if __name__ == "__main__":
    app.run(debug=True)
