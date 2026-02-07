import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return "Bot 'thằng ku em' của Kem-Vani đã Online 24/7!", 200
    
    data = request.json
    print(f"📥 Zalo nhận tin: {data}")
    # Đây là nơi bạn sẽ gọi DuckDB để lấy báo cáo NIM/CASA/CL025
    return jsonify({"status": 200}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)