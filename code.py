import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
usermail = (input("Please Enter Your Gmail ID : \n"))
userpass = (input("Please Enter Your Gmail Password : \n"))

sender, receiver = usermail, "mohituiux@gmail.com"

server.starttls()  # Authentication

try:
    server.login(usermail, userpass)
    message = input("Please Enter Your Massage : \n")
    server.sendmail(sender, receiver, message)
    server.quit()
    print("Mail Sent")
except:
    print("Maill Sent Failed")
