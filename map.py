from flask import Flask, send_from_directory, render_template, jsonify
import utm
import os

app = Flask(__name__)

# 환경 변수에서 클라이언트 ID와 비밀번호 가져오기
CLIENT_ID = os.getenv('NAVER_CLIENT_ID', 'u3fh3k13l2')
CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET', 'Cx32NLrYuycqFzI7NiLU0xoNjRvnXT41saMDDEOr')

# 기본 라우트 정의
@app.route('/')
def index():
    return render_template('index2.html', client_id=CLIENT_ID)

# 웨이포인트 파일 제공 라우트 정의
@app.route('/waypoints.txt')
def waypoints():
    return send_from_directory('.', 'test_path14.txt')

# UTM 좌표를 위도/경도로 변환하여 제공하는 라우트 정의
@app.route('/convert_utm')
def convert_utm():
    waypoints = []
    with open('test_path14.txt', 'r') as f:
        for line in f:
            # 공백을 기준으로 데이터를 분리하도록 수정
            #x, y, z = map(float, line.split())
            x, y= map(float, line.split())
            lat, lng = utm.to_latlon(x, y, 52, 'N')  # 예시로 UTM Zone 52N 사용
            waypoints.append({
                'lat': lat,
                'lng': lng,
                #'description': f'x : {x}, y : {y}, sheading: {z:.2f}m'
                'description': f'x : {x}, y : {y}'
            })
    return jsonify(waypoints)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)