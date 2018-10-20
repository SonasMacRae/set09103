from flask import *
app = Flask(__name__)

# Loads the data from the JSON files
consoleData = json.load(open("data/consoles.json"))
developerData = json.load(open("data/developers.json"))
gameData = json.load(open("data/games.json"))

# Accesses a certain array from the JSON files that were loaded
developerInput = developerData["developers"]
consoleInput = consoleData["consoles"]
gameInput = gameData["games"]

@app.errorhandler(404)
def page_not_found(error):
	return render_template("errorpage.html"), 404

# Route for the home page, which doubles as the page to display all of the developers
@app.route("/developer/")
@app.route("/")
def home():
	return render_template("home.html", developers=developerInput)

# Returns a developers page with required console and developer data
@app.route("/developer/<search>")
def developer(search):
	output = []
	for d in developerInput:
		if d["name"].lower() == search.lower():
			output.append(d)
	consoleList = []
	for console in consoleInput:
		if console["developer"].lower() == search.lower():
			consoleList.append(console)
	return render_template("developerpage.html", developer=output, consoleList=consoleList)

# Page that displays all of the consoles
@app.route("/allconsoles/")
def all():
	return render_template("searchconsoles.html", consoleList=consoleInput)

# Page that displays all of the consoles after a filter is applied
@app.route("/allconsoles/<search>")
def consoles(search):
	consoleList = []
	for console in consoleInput:
		if console["developer"].lower() == search.lower():
			consoleList.append(console)
	return render_template("searchconsoles.html", consoleList=consoleList)

# Page to display one console in more detail
@app.route("/console/<search>")
def console(search):
	game = []
	console = []
	for c in consoleInput:
		if c["name"].lower() == search.lower() or c["ref"].lower() == search.lower():
			console.append(c)
	for g in gameInput:
		if g["id"].lower() == search.lower():
			game.append(g)
	return render_template("consoleprofile.html", console=console, game=game)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
