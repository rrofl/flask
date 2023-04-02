from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cs")
def game_cs():
    return render_template('cs.html')

@app.route("/valorant")
def game_valorant():
    return render_template('valorant.html')

if __name__ == "__main__":
    app.run(debug=True)