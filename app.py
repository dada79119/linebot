import requests
from bs4 import BeautifulSoup
from flask import Flask, request, abort
import ssl
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    #get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "200"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
         event.reply_token,
         TextSendMessage(text=event.message.text))
    return 0


if __name__ == "__main__":
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_cert_chain('{{your ssl_certificate.crt}}','{{your ssl_private.key}}')
    ctx.load_verify_locations('{{ your ssl_ca_bundle.crt}}')
    app.run(host='{{SERVER PUBLIC IP}}',port={{SERVER PORT}},ssl_context=ctx)

