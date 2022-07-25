from flask import Flask, jsonify,json,request
from similarity import get_similarity

app = Flask(__name__)


@app.route('/similarity/',methods=['POST'])
def run_step():
    data = json.loads(request.data)
    sentence1 = data['sentence1']
    sentence2 = data['sentence2']
    result = get_similarity(sentence1,sentence2)
    return jsonify(str(result))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
