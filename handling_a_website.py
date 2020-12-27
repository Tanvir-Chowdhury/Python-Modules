import smtplib
import os
import requests

EMAIL_USER = os.environ.get("EMAIL_USER")
#Email_address = "tanvirvlogger@gmail.com"
EMAIL_PASS = os.environ.get("EMAIL_PASS")
#Email_pass = 

print(EMAIL_USER)
print(EMAIL_PASS)

r = requests.get("https://coreyms.com", timeout=5)
if r.status_code != 200:
    with  smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_USER, EMAIL_PASS)
        subject = "Website down"
        body = "your website is down"
        msg = f"subject: {subject} \n\n {body}"

        smtp.sendmail(EMAIL_USER, "tanvirvlogger@gmail.com", msg)
