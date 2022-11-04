from flask import Flask, jsonify, request

app = Flask(__name__)

user_dict = {"slackUsername": "yuguda999",
             "backend": True,
             "age": 23,
             "bio": "Logical and result-driven programmer.I love to devise elaborate methods for solving general problems"
             }

# hng backend Task 1
@app.route("/user-info")
def user():
    return jsonify(user_dict)

#hng back end Task 2
@app.route("/math", methods=["POST"])
def operation():
    result=0
    operation_type = request.get_json()['operation_type']
    splited_operatiion_type = operation_type.lower().split(' ')
    x = int(request.get_json()['x'])
    y = int(request.get_json()['y'])
    if 'addition' in splited_operatiion_type or 'add' in splited_operatiion_type or 'plus' in splited_operatiion_type or '+' in splited_operatiion_type:
        result = x + y
    elif 'subtraction' in splited_operatiion_type or 'subtract' in splited_operatiion_type or 'minus' in splited_operatiion_type or '-' in splited_operatiion_type:
        result = x - y
    elif 'multiplication' in splited_operatiion_type or 'multiply' in splited_operatiion_type or 'times' in splited_operatiion_type or '*' in splited_operatiion_type:
        result = x * y
    else:
        result = "i can't understand the operation type"

    return {"slackUsername": "yuguda999","result": result, "operation_type": operation_type}, 200


if __name__ == "__main__":
    app.run()
