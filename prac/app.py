from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sparta', methods=["GET"])
def sparta():
    title = request.args.get('title')
    return jsonify({'result': 'success', 'msg': 'get 방식입니다', 'title': title})

@app.route('/sparta', methods=["POST"])
def post_sparta():
    address = request.form["address"]
    name = request.form["name"]
    print(address)
    print(name)
    return jsonify({
        'result': 'success',
        'data': {
        'title': address + '' + name
        }
    })

@app.route('/sum', methods=["GET"])
def sum():
    num = request.args.get('num')
    num_int = int(num)
    total = 0
    if num is None:
        return jsonify({'result': 'fail', 'msg': '값이 들어오지 않았습니다', 'total': 'null'})
    for i in range(0, num_int+1):
        total += i
    return jsonify({'result': 'success', 'msg': 'get 방식입니다', 'total': total})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# 숫자를 하나 입력받아서 그 숫자까지의 합을 구해라
# GET