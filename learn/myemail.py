import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output

from django.conf import settings

# print(settings.EMAIL_BACKEND)
# receiver = '137740537@qq.com'
# mail_host = 'smtp.qq.com'
mail_host = settings.EMAIL_HOST
# mail_user = 'ydy201@qq.com'
mail_user = settings.EMAIL_HOST_USER
# mail_pass = 'crdyyuilyrsubjbg'
mail_pass = settings.EMAIL_HOST_POSSWORD
sender = mail_user
# receivers = [receiver]

class MyEmail(object):
    @staticmethod
    def send(subject, context, receivers):
        # message = MIMEText(log)
        message = MIMEText(context)
        message['From'] = Header(mail_user, 'utf-8')
        message['To'] = Header(str(receivers), 'utf-8')
        # subject = 'my test'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            # print('smtpObj')
            smtpObj.login(mail_user, mail_pass)
            print('login')
            smtpObj.sendmail(sender, receivers, message.as_string())
            print('send')
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e :
            print(e)
