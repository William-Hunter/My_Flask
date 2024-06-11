import imaplib
import email
from email.header import decode_header

def fetch_emails():
    # 连接到邮箱服务器
    mail = imaplib.IMAP4_SSL('imap.126.com')

    # 登录到邮箱账户
    # mail.login('willliam113758', 'lonedon113758')
    # mail.login('willliam113758@126.com', 'lonedon113758')
    mail.login('willliam113758@126.com', 'CAWBCNFZXUBQZYHN')

    # 选择收件箱
    # mail.select('inbox')
    mail.select()

    # 获取邮件列表
    result, data = mail.search(None, 'ALL')
    if result == 'OK':
        email_ids = data[0].split()

        # 遍历每封邮件
        for email_id in email_ids:
            result, email_data = mail.fetch(email_id, '(RFC822)')
            if result == 'OK':
                msg = email.message_from_bytes(email_data[0][1])

                # 解码邮件主题和内容
                subject = decode_header(msg['Subject'])[0][0].decode('utf-8')
                content = ''
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        content += part.get_payload(decode=True).decode('utf-8')

                # 打印邮件信息
                print('Subject:', subject)
                print('Content:', content)

    # 关闭连接
    mail.close()
    mail.logout()

# 调用函数来获取邮件
fetch_emails()