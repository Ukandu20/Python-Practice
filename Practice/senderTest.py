import smtplib
from email.message import EmailMessage

def send_email(name, email, subject, message):
    msg = EmailMessage()
    msg.set_content(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")
    
    msg['Subject'] = f"New Contact Form Submission: {subject}"
    msg['From'] = email
    msg['To'] = 'oukadu2000@gmail.com'  # Replace with your email address

    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your email provider's SMTP server
        server.starttls()
        server.login('oukandu2000@gmail.com', 'Apexgoldchain765')  # Replace with your email credentials
        server.send_message(msg)

if __name__ == '__main__':
    # Simulate form values (replace with your own logic)
    first_name = 'John'
    last_name = 'Doe'
    email = 'john@example.com'
    subject = 'Subject Example'
    message = 'This is the message content.'

    send_email(f"{first_name} {last_name}", email, subject, message)
