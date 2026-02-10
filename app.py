import os, requests
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
ZALO_TOKEN = "740210487292609069:geEiYmngxOKonbNkDqxVuBQFozJcOwcHlxYbaNkJkHUBImvyEOBEEAaKytHaXtUj"

# 1. TRANG CHỦ (Để Zalo quét Thẻ Meta)
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="zalo-platform-site-verification" content="K_I_E9Jc5IuMuB0XtSKQUrt0ZtcnjbiWCZKv" />
        <title>Bot Tro Ly BDS</title>
    </head>
    <body><h1>He thong Bot da Online!</h1></body>
    </html>
    '''

# 2. FILE HTML XÁC THỰC (Đúng tên theo ảnh 02:33)
@app.route('/zalo_verifierK_I_E9Jc5IuMuB0XtSKQUrt0ZtcnjbiWCZKv.html')
def verify_zalo():
    return "K_I_E9Jc5IuMuB0XtSKQUrt0ZtcnjbiWCZKv"

# 3. HÀM GỬI TIN NHẮN
def send_reply(user_id, text):
    url = f"https://bot-api.zaloplatforms.com/bot740210487292609069:geEiYmngxOKonbNkDqxVuBQFozJcOwcHlxYbaNkJkHUBImvyEOBEEAaKytHaXtUj/sendMessage"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "chat_id": user_id,
        "text": text
    }
    return requests.post(url, headers=headers, json=payload).json()

# 4. CỔNG NHẬN TIN NHẮN WEBHOOK
@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return "Webhook OK", 200
    data = request.json
    if data and "message" in data:
        user_id = data['sender']['id']
        user_text = data['message']['text']
        if user_text.lower() == "/ping":
            send_reply(user_id, "Pong! Thang ku em da thong suot 100%.")
    return jsonify({"status": 200}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)