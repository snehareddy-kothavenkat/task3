f = open("/root/task3/accuracy.txt", "r")
acc = f.readlines()
f.close()
accuracy = str(acc[0])
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from_addr = 'testuser2352@gmail.com'
to_addr= 'kvsnehareddy772@gmail.com'
text = ''' Hello Developer !!! Your MNIST Model has reached the desired accuracy - ''' accuracy

username = 'testuser2352@gmail.com'
password = '#testuser2352#'

msg = MIMEMultipart()

msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Accuracy of your mnist model"
msg.attach(MIMEText(text, 'plain'))


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
