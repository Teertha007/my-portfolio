import smtplib,ssl,socketserver


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "teertha.sarker.4@gmail.com"
    password = "vwyp ikih idsn qcrw"
    receiver = "teertha.sarker.3@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver,message)


#send_email()