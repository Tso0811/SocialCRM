from django.core.mail import send_mail
from django.conf import settings

def user_register(to_user):
        send_mail(
                subject='註冊成功',
                message='您好，感謝您註冊成為我們的會員！',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_user],
                fail_silently=False,            #預設為False  信件發送錯誤會拋出錯誤訊息 在正式環境中要設為True
                )

def send_event_register(to_user):
        send_mail(
            subject='活動報名成功',
            message='您好，恭喜你活動報名成功！',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_user],
            fail_silently=False,       
            )                              