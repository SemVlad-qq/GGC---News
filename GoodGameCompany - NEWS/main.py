import sqlite3

from flask import Flask, render_template
#from flask_sqlalchemy import SQLAchemy

app = Flask(__name__)
#app.config['SOLALCHEMYE DATABASE_URI'] = 'sqlite://Registration_DB.db'
#db - SQLAlchemy(app)

#class REG(db.Model):
    #user = db.Column(primary_key=True)
    #password = db.Column(Nullable=False)
    #email = db.Column(Nullable=False)

    #def __repr__(self):
        #return '<Article %r>' % self.name

#base
@app.route('/')
def spawn():
    return render_template("Spawn.html")

@app.route('/Registration')
def Registration():
    return render_template("Registration.html")






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


#News

@app.route('/Xbox Servers Are Back Up After Extended Downtime')
def XboxServersAreBackUpAfterExtendedDowntime():
    return render_template("Xbox Servers Are Back Up After Extended Downtime.html")

@app.route('/PlayStation Plus Free Games For July 2024 Are Live Now')
def PlayStationPlusFreeGamesForJuly2024AreLiveNow():
    return render_template("PlayStation Plus Free Games For July 2024 Are Live Now.html")

@app.route('/Metal Gear Rising Revengeance Slashes A Power Hungry Senator And Its Own Price In New GOG Deal')
def MetalGearRisingRevengeanceSlashesAPowerHungrySenatorAndItsOwnPriceInNewGOGDeal():
    return render_template("Metal Gear Rising Revengeance Slashes A Power Hungry Senator And Its Own Price In New GOG Deal.html")

@app.route('/Haters Be Damned Elden Ring Summoning Leads To Shadow Of The Erdtrees Best Moment')
def HatersBeDamnedEldenRingSummoningLeadsToShadowOfTheErdtreesBestMoment():
    return render_template("Haters Be Damned Elden Ring Summoning Leads To Shadow Of The Erdtrees Best Moment.html")

@app.route('/LastNews')
def LastNews():
    return render_template("Last news.html")

@app.route('/AllNews')
def AllNews():
    return render_template("All news.html")


#news



if __name__ == "__main__":
    app.run(debug=True)
