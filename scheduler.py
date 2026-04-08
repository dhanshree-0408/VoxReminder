import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def trigger_notifications(task_name, receiver_email):
    """
    Version 2.0: Universal Email-Only Alerts.
    Works on Windows, Mac, and Linux Cloud Servers.
    """
    
    # 1. LOGGING (Instead of a popup, we print to the server console)
    print(f"⏰ Timer triggered for task: {task_name}")

    # 2. EMAIL ALERT (SMTP) - This is the universal part!
    if receiver_email and "@" in receiver_email:
        try:
            if not SENDER_EMAIL or not SENDER_PASSWORD:
                raise ValueError("Credentials missing in .env")

            em = EmailMessage()
            em['From'] = SENDER_EMAIL
            em['To'] = receiver_email
            em['Subject'] = f"⏰ VoxReminder: {task_name}"
            em.set_content(f"Hi! This is your AI assistant. It is time for: {task_name}")

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
                smtp.send_message(em)
            print(f"📧 SUCCESS: Email alert sent to {receiver_email}")
        except Exception as e:
            print(f"❌ EMAIL ERROR: {e}")