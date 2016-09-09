Python Email
============

Example::

    import os
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from .config import Config
    from .utils import Logger
    from .git import Git

    class RREmail(object):
        def __init__(self, user=None, from_email=None, to_email=None, cc_email=None):
            super(RREmail, self).__init__()
            self.from_email = from_email or Git.get_user_email()
            self.to_email = to_email or Config.GateKeeper
            self.cc_email = cc_email or Config.CHECK_IN_CC
            self.user = user or Config.EMAIL_USER
            self.server = Config.EMAIL_SMTP_SERVER
            self.port = Config.EMAIL_PORT
            self.sm = smtplib.SMTP(self.server, self.port, timeout=20)

        # Not neccessary
        def login(self, user='', password=''):
            #self.sm.set_debuglevel(1)
            #self.sm.ehlo()
            #self.sm.starttls()
            #self.sm.ehlo()
            self.sm.login(user or self.user,
                          password or raw_input('Please input the email password: ').strip())

        def send(self, subject, body, body_html=None, attachments=None, in_reply_to=None):
            message = MIMEMultipart('related')
            message['Subject'] = subject
            message['From'] = self.from_email
            message['To'] = self.to_email
            if self.cc_email.strip():
                message['CC'] = self.cc_email
            if in_reply_to is not None:
                message['In-Reply-To'] = in_reply_to

            msg_body = MIMEMultipart('alternative')
            message.attach(msg_body)

            body_plain = MIMEText(body, 'plain')
            msg_body.attach(body_plain)

            if body_html is not None:
                body_html = MIMEText(body_html, 'html', 'utf-8')
                msg_body.attach(body_html)

            if attachments is not None:
                for patch in attachments:
                    f = open(patch)
                    att = MIMEText(f.read(), 'plain', 'utf-8')
                    att["Content-Type"] = 'text/plain'
                    att["Content-Disposition"] = 'attachment;filename="%s"' % os.path.basename(patch)
                    message.attach(att)
                    f.close()

            return self.sm.sendmail(self.from_email,
                                    self.to_email,
                                    message.as_string())

        def quit(self):
            self.sm.quit()


References:

- http://www.jb51.net/article/49219.htm

