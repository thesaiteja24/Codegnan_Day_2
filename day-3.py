# email automation with OTP validation
import smtplib
import random
import math
from datetime import datetime, timedelta
from day_1 import BMI


def rock_paper_scissor():
    while (True):
        choice = input("\n1.Rock\n2.Papper\n3.Scissor\nEnter your choice:")
        system = random.choice(["Rock", "Paper", "Scissor"])
        if choice.lower() == system.lower():
            print("Congratulations You have won")
            break
        else:
            print("Please Try again!")


def validate_otp(user_input, OTP, generate_time):
    current_time = datetime.now()
    enlapsed_time = current_time-generate_time
    if enlapsed_time <= timedelta(seconds=60) and user_input == OTP:
        return True
    else:
        return False


def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random()*10)]
    return OTP, datetime.now()


def send_otp(sender, app_pass, receiver):

    OTP, generate_time = generate_otp()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, app_pass)
    otp_msg = f"#{OTP} Is your OTP for login."
    server.sendmail(sender, receiver, otp_msg)
    print("Done!")

    user_input = input("Enter OTP to validate:")
    if validate_otp(user_input, OTP, generate_time):
        print("Validated Successfuly")
        rock_paper_scissor()
    else:
        print("Invalid OTP or Time expired")
        print("Lets calculate your BMI ;)")
        BMI()


sender = ""  # Enter sender mail
app_pass = ""  # Enter google app password
receiver = ""  # Enter receiver mail
send_otp(sender=sender, receiver=receive, app_pass=app_pass)
