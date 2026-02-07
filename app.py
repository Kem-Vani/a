import os, requests
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
ZALO_TOKEN = "740210487292609069:geEiYmngxOKonbNkDqxVuBQFozJcOwcHlxYbaNkJkHUBImvyEOBEEAaKytHaXtUj"

# --- CÁCH 1: XÁC THỰC BẰNG THẺ META (Zalo quét trang chủ) ---
@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="zalo-platform-site-verification" content="K_I_E9Jc5IuMuB0XtSKQUrt0ZtcnjbiWCZKv" />
        <title>Hệ thống Kem-Vani</title>
    </head>
    <body>
        <h1>Hệ thống Kem-Vani đã Online!</h1>
        <p>Đang sẵn sàng xử lý các báo cáo tín dụng cho bạn.</p>
    </body>
    </html>
    '''
    return render_template_string(html_content)

# --- CÁCH 2: XÁC THỰC BẰNG TỆP HTML (Zalo quét file riêng) ---
@app.route('/zalo_verifierK_I_E9Jc5IuMuB0XtSKQUrt0ZtcnjbiWCZKv.html')
def verify_zalo():
    return "K_I_E9Jc5IuMuB0XtSKQUrt0ZtcnjbiWCZKv"

def send_reply(user_id, text):
    url = "https://openapi.zalo.me/v3.0/oa/message/promotion"
    headers = {"access_token": ZALO_TOKEN, "Content-Type": "application/json"}
    payload = {"recipient": {"user_id": user_id}, "message": {"text": text}}
    return requests.post(url, headers=headers, json=payload).json()

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET': return "Webhook OK", 200
    data = request.json
    if data and "message" in data:
        user_id, user_text = data['sender']['id'], data['message']['text']
        if user_text.lower() == "/ping":
            send_reply(user_id, "Pong! Thằng ku em đã thông suốt 2 chiều.")
    return jsonify({"status": 200}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)