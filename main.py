from flask import Flask, jsonify, request

app = Flask(__name__)

user_dict = {"slackUsername": "yuguda999",
             "backend": True,
             "age": 23,
             "bio": "Logical and result-driven programmer.I love to devise elaborate methods for solving general problems"
             }


@app.route("/user-info")
def user():
    return jsonify(user_dict)


@app.route("/math", methods=["POST"])
def operation():
    result=0
    operation_type = request.get_json()['operation_type']
    x = int(request.get_json()['x'])
    y = int(request.get_json()['y'])
    if operation_type == 'addition':
        result = x + y
    elif operation_type == 'subtraction':
        result = x - y
    elif operation_type == 'multiplication':
        result = x * y

    return {"slackUsername": "yuguda999","result": result, "operation_type": operation_type}, 200


if __name__ == "__main__":
    app.run()
