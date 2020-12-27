import smtplib
import os

EMAIL_USER = "tanvirvlogger@gmail.com"
EMAIL_PASS = ""

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_USER, EMAIL_PASS)

    subject = "website down"
    body = "your website is down"
    msg = f"subject: {subject} \n\n {body}"

    smtp.sendmail(EMAIL_USER, "tanvirchowdhury6465@gmail.com", msg)