from django.conf import settings
from django.core.mail import send_mail



def send_email_token(email, token):
    """
    Sends a verification email to the user.
    In development, prints the email in console.
    """
    verification_link = f"http://127.0.0.1:8000/verify/{token}/"
    
    subject = "Verify your account"
    message = f"Hello!\n\nClick the link below to verify your account:\n\n{verification_link}"
    from_email = settings.EMAIL_HOST_USER

    try:
        send_mail(subject, message, from_email, [email])
        # Print a clean link for easy copy-paste
        print(f"Verification link for {email}: {verification_link}")
        return True
    except Exception as e:
        print("Failed to send email:", e)
        return False