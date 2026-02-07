import os, requests
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
ZALO_TOKEN = "740210487292609069:geEiYmngxOKonbNkDqxVuBQFozJcOwcHlxYbaNkJkHUBImvyEOBEEAaKytHaXtUj"

# --- TRANG CHỦ: Chứa thẻ Meta xác thực ---
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="zalo-platform-site-verification" content="K_I_E9Jc5IuMuB0XtSKQUrt0ZtcnjbiWCZKv" />
        <title>Bot Thằng Ku Em</title>
    </head>
    <body>
        <h1>Hệ thống đã sẵn sàng!</h1>
    </body>
    </html>
    '''

# --- FILE HTML: Xác thực domain ---
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
    if request.method == 'GET': return "Webhook Online!", 200
    data = request.json
    if data and "message" in data:
        user_id = data['sender']['id']
        user_text = data['message']['text']
        if user_text.lower() == "/ping":
            send_reply(user_id, "Pong! Hệ thống đã thông suốt hoàn toàn.")
    return jsonify({"status": 200}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)