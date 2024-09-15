import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from decouple import config

# Email information from .env file
from_address = config('FROM_ADDRESS')
to_address = config('TO_ADDRESS')
app_password = config('APP_PASSWORD')
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
filename = "your_file.pdf"  # Name of the attached file
with open(filename, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={filename}")

msg.attach(part)

# Connect to Gmail SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the account using the application password
    server.login(from_address, app_password)

    # Send the email
    server.sendmail(from_address, to_address, msg.as_string())
    print("Email sent successfully.")

except Exception as e:
    print(f"Error sending email: {e}")

finally:
    server.quit()
