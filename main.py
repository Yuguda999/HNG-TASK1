from flask import Flask, jsonify

app = Flask(__name__)

user_dict = {"slackUsername": "yuguda999",
        "backend": True,
        "age": 23,
        "bio": "Logical and result-driven programmer.I love to devise elaborate methods for solving general problems"
        }
@app.route("/user-info")
def user():
    return jsonify(user_dict)


if __name__ == "__main__":
    app.run()
