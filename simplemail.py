#email automation
#otp authentication
import random
import math
import smtplib#simple mail transfer protocol library
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+" "+"is your otp"
msg=otp
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("sowmyapotharlanka1319@gmail.com","rmrg nrrh qeow bnsg")
user="sowmyapotharlanka1319@gmail.com"
email=input("enter the email:")
s.sendmail(user,email,msg)
while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("incorrect otp")
