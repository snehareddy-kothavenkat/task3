f = open("/root/task3/accuracy.txt", "r")
acc = f.readlines()
f.close()
accuracy = str(acc[0])
import smtplib
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
	smtp.ehlo()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = 'jenkins@gmail.com'
to_addr = 'onlytesting2119@gmail.com'
text = accuracy

username = 'onlytesting2119@gmail.com'
password = 'Testing@123'

msg = MIMEMultipart()

msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Accuracy"
msg.attach(MIMEText(text))


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()