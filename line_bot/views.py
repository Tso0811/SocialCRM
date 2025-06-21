from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from ai.services import recommend_events_for_user
from .models import LineBindingStatus

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)
User = get_user_model()

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

@handler.add(MessageEvent, message=TextMessage)
def handle_line_message(event):
    line_id = event.source.user_id
    message = event.message.text.strip()
    user = User.objects.filter(line_id=line_id).first()
    binding, _ = LineBindingStatus.objects.get_or_create(line_id=line_id)

    # 優先處理帳號綁定流程
    if User.objects.filter(line_id=line_id).exists() and message == "綁定帳號":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="你已經綁定過帳號！")
        )
        return

    if message == "綁定帳號":
        binding.step = "wait_username"
        binding.temp_username = None
        binding.save()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入網站帳號：")
        )
        return

    elif binding.step == "wait_username":
        binding.temp_username = message
        binding.step = "wait_password"
        binding.save()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入密碼：")
        )
        return

    elif binding.step == "wait_password":
        username = binding.temp_username
        password = message
        user = authenticate(username=username, password=password)

        if user:
            user.line_id = line_id
            user.save()
            binding.delete()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="✅ 綁定成功！")
            )
        else:
            binding.step = "wait_username"
            binding.temp_username = None
            binding.save()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="❌ 帳號或密碼錯誤，請重新輸入帳號：")
            )
        return

    # 處理推薦活動
    if user and message == '推薦活動':
        recommendations = recommend_events_for_user(user)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=recommendations)
        )
        return

    # 處理一般訊息回覆
    if user:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"你剛剛說：{message}")
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='你還沒有綁定帳號，請輸入「綁定帳號」來綁定你的帳號')
        )