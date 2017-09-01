#coding:utf8
'''
发送文本邮件
'''
from email.mime.text import MIMEText
import smtplib

mailto_list = [ # 发送目的邮箱
    'liqirong1701python@163.com',
    'liqirong1701python@163.com',
]

me = 'liqirong1701python@163.com' # 从哪发
mail_host = 'smtp.163.com' # 邮箱服务器
mail_user = 'liqirong1701python' # 登录服务器的用户名
mail_pass = 'python1701'  # 163授权码


def send_mail(to_list, sub, content):
    msg = MIMEText(content,format,'utf-8') # 初始化 mime对象
    # msg["Accept-Language"] = "zh-CN"
    # msg["Accept-Charset"] = "ISO-8859-1,utf-8"
    msg['Subject'] = sub # 邮件标题
    msg['From'] = me # 从哪里发 发件地址
    msg['To'] = ';'.join(to_list) # 发到哪里
    try:
        s = smtplib.SMTP_SSL(mail_host, 465)   # 初始化stmp_ssl 对象   465邮件服务器端口
        s.connect(mail_host)  # 连接stmp邮件服务器
        s.login(mail_user, mail_pass) # 登陆smtp服务器 用qq号 和  授权码登陆
        s.sendmail(me, to_list, msg.as_string())  # 登陆成功  发送邮件
        s.close() # 关闭smtp 连接
        return True
    except Exception, e:
        print e
        return False

if __name__ == '__main__':
    if send_mail(mailto_list, '标题', '我是内容'):
        print '发送成功'
    else:
        print '发送失败'
