import smtplib


sender = 'ajukica01@gmail.com'
receiver = 'anteprojic@gmail.com'
password = input("Vasa lozinka")

message = "Ovo je testni mail"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, reciever, message)
    server.close()

    print ('Email uspješno poslan')
except:
    print ("Greška : Email nije poslan!")