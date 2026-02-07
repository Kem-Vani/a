import os, requests
from flask import Flask, request, jsonify

app = Flask(__name__)
ZALO_TOKEN = "740210487292609069:geEiYmngxOKonbNkDqxVuBQFozJcOwcHlxYbaNkJkHUBImvyEOBEEAaKytHaXtUj"

def send_reply(user_id, text):
    # Hàm gửi tin nhắn phản hồi qua Zalo API
    url = "https://openapi.zalo.me/v3.0/oa/message/promotion"
    headers = {"access_token": ZALO_TOKEN, "Content-Type": "application/json"}
    payload = {
        "recipient": {"user_id": user_id},
        "message": {"text": text}
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return "Hệ thống Kem-Vani đã Online!", 200
    
    data = request.json
    print(f"📥 Nhận tin nhắn: {data}")
    
    # Xử lý khi có tin nhắn văn bản đến
    if data and "message" in data:
        user_id = data['sender']['id']
        user_text = data['message']['text']
        
        # Phản hồi lệnh /ping
        if user_text.lower() == "/ping":
            send_reply(user_id, "Pong! Thằng ku em đã nhận lệnh và đang trực 24/7.")
        else:
            send_reply(user_id, f"Bot đã nhận tin: {user_text}")
            
    return jsonify({"status": 200}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)