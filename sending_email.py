import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

'''with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_USER, EMAIL_PASS)

    subject = "website down"
    body = "your website is down"
    msg = f"subject: {subject} \n\n {body}"

    smtp.sendmail(EMAIL_USER, "tanvirchowdhury6465@gmail.com", msg)'''


msg = EmailMessage()
msg['Subject'] = 'website down'
msg['From'] = EMAIL_USER
msg['To'] = 'tanvirchowdhury6465@gmail.com'
msg.set_content('Look down here:')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style= "color:SlateGray">There is a csv file</h1>
    </body>
</html>    
""", subtype='html')

with open('names.csv', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_USER, EMAIL_PASS)
    smtp.send_message(msg)