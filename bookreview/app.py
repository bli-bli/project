from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
	# 1. 클라이언트가 준 title, author, review 가져오기.
    title = request.form["title"]
    author = request.form["author"]
    bookReview = request.form["bookReview"]
    print(title, author, bookReview)
	# 2. DB에 정보 삽입하기
    db.bookReview.insert_one({'title': title,
                             'author': author,
                             'bookReview': bookReview})
	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '정상적으로 등록이 완료되었습니다'})

@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.bookReview.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'reviews': reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)