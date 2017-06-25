import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output

receiver = '137740537@qq.com'
mail_host = 'smtp.qq.com'
mail_user = 'ydy201@qq.com'
mail_pass = 'crdyyuilyrsubjbg'
sender = mail_user
receivers = [receiver]

# message = MIMEText(log)
message = MIMEText('hello')
message['From'] = Header(mail_user, 'utf-8')
message['To'] = Header(str(receivers), 'utf-8')

subject = 'my test'
message['Subject'] = Header(subject, 'utf-8')

print('start')
try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    print('smtpObj')
    smtpObj.login(mail_user, mail_pass)
    print('login')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('send')
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e :
    print(e)
