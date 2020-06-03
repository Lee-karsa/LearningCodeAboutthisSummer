import smtplib
from email.mime.text import MIMEText
from email.header import Header

def set_pic_file():
    print ("邮件发送中")
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "***@qq.com"  # 用户名
    mail_pass = "***"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
    sender = '***@qq.com'
    receivers = ['***@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText('python发送邮件', 'plain', 'utf-8')
    message['From'] = Header("***@qq.com", 'utf-8')
    message['To'] = Header("***@qq.com", 'utf-8')
    subject = "我爱你，亲爱的宝贝"
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print (u"邮件发送成功")
    except smtplib.SMTPException as e:
        print (e)
if __name__ == '__main__':
    set_pic_file()
