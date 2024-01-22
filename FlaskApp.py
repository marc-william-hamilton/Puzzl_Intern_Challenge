from flask import Flask, render_template
from RockPaperScissors import get_opponent_choice, determine_winner

app = Flask(__name__)

emojis = {}
emojis["rock"] = "🪨"
emojis["paper"] = "📄"
emojis["scissors"] = "✂️"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/rock", methods=["POST"])
def rock():
    return do_game("rock")


@app.route("/paper", methods=["POST"])
def paper():
    return do_game("paper")


@app.route("/scissors", methods=["POST"])
def scissors():
    return do_game("scissors")


def do_game(player_choice):
    opponent_choice = get_opponent_choice()
    result = determine_winner(player_choice, opponent_choice)
    return render_template(
        "results.html",
        player_choice=emojis[player_choice],
        opponent_choice=emojis[opponent_choice],
        result=result,
    )


if __name__ == "__main__":
    app.run(debug=True)
