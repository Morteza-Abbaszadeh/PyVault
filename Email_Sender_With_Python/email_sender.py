import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email information
from_address = "FROM_ADDRESS"
to_address = "TO_ADDRESS"
subject = "Hi"
body = "How are you? What's up?"

# Construct the email
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject

# Add text to the email
msg.attach(MIMEText(body, 'plain'))

# File attachment
filename = "your_file"
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename={filename}")

msg.attach(part)

# Connect to Gmail SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    server.login(from_address, "app password")
    
    # Send the email
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    print("Email sent successfully.")
    
except Exception as e:
    print(f"Error sending email: {e}")
    
finally:
    server.quit()
