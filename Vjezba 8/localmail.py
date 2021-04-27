import smtplib
from smtplib import SMTPException

sender = 'ante.jukica@aspira.hr'
receivers = 'ante.jukica@aspira.hr'

message = "Ovo je testni mail"

try:
   smtpObj = smtplib.SMTP('localhost:1025')
   smtpObj.sendmail(sender, receivers, message)         
   print ("E-mail uspješno poslan..")
except SMTPException:
   print ("Error: E-mail nije uspješno poslan")