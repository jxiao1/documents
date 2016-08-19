Python Email
============

Example::

    import smtplib
    from email.message import Message

    username = 'username@gmail.com'
    password = 'password'

    message = Message()
    message['Subject'] = 'Mail Subject'
    message['From'] = 'from@gmail.com'
    message['To'] = 'to@test.com'
    message['Cc'] = 'cc@test.com'
    message.set_payload('mail content for test!')
    msg = message.as_string()

    sm = smtplib.SMTP('smtp.gmail.com', port=587, timeout=20)
    sm.set_debuglevel(1)
    sm.ehlo()
    sm.starttls()
    sm.ehlo()

    sm.login(username, password)

    sm.sendmail(from_addr, to_addr, msg)
    sm.quit()


References:

- http://www.jb51.net/article/49219.htm

