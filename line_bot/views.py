from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from utils.sending_mail import send_event_register
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def line_webhook(request):
    if request.method == "POST":
        signature = request.META.get('HTTP_X_LINE_SIGNATURE', '')
        body = request.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            print("錯誤")
            return HttpResponse(status = 400)
        return HttpResponse("OK")
    return HttpResponse("這是 webhook endpoint", status = 200)

@handler.add(MessageEvent, message = TextMessage) #這個裝飾器是告訴後端 當用戶傳送訊息時要叫哪個涵式處理
def handle_message(event):
    try:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = f"你剛剛說：{event.message.text}")
        )
    except Exception as e:
        print("回覆訊息失敗：", e)
        import traceback; traceback.print_exc()