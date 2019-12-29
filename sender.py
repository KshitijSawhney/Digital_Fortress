import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


def sendmessage(user,password,rec,body):
        fromaddr = user
        msg = MIMEMultipart()
        toaddr = rec
        msg['From'] = user
        msg['To'] =rec
        msg['Subject'] = "Your latest encrypted message is here ...."
         
        msg.attach(MIMEText(body, 'plain'))
         
        filename = "tester.txt"
        attachment = open("tester.txt", "rb")
         
        part = MIMEBase('application', 'octet-stream')
        encoders.encode_base64(part)
         
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, password)
        text = msg.as_string()
        server.sendmail(user, rec, text)
        print 'sent'
        server.quit()
