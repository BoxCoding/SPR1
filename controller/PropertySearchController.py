from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/sprsearch', methods=['POST'])
def getSearch():
    dataDict = request.get_json()
    print(dataDict)
    retJson = {
        "final": dataDict
    }
    return jsonify(retJson), 200


if __name__ == "__main__":
    app.run(debug=True)
