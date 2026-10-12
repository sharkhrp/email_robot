
import smtplib
from email.message import EmailMessage



SENDER = "ammar537balouch@gmail.com"

PASSWORD = "your_password"



def send(recipient, content):

    
	msg = EmailMessage()
    
	msg.set_content(content)

    
	msg["Subject"] = "Notification"
    
	msg["From"] = SENDER
    
	msg["To"] = recipient


    
	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        
		smtp.login(SENDER, PASSWORD)
        
		smtp.send_message(msg)
