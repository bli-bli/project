from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result':'success', 'msg':'이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_get():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result':'success', 'msg':'이 요청은 POST!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# 숫자를 하나 입력받아서 그 숫자까지의 합을 구해라
# GET : ajax 의 url 부분에 물음표 형식으로 가지고 간다
# POST : ajax 의 data 부분에 데이터를 담아서 전달한다