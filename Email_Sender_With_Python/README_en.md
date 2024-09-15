### Instructions:

1. **Email Information**: You need to specify the sender's email, recipient's email, subject, and body of the email.
2. **File Attachment**: The file attachment is added to the email using `MIMEBase`.
3. **Connect to SMTP Server**: We use Gmail’s SMTP server to send the email. Port 587 is used for TLS.
4. **Login to the Account**: You need to enter your password or **App password**, which is recommended for added security.
5. **Send the Email**: The email is sent to the recipient using `sendmail`.

To get the **App password**, follow these steps:

### Step 1: Sign in to your Google Account

1. Go to [myaccount.google.com](https://myaccount.google.com/).
2. Sign in to your Gmail account (the account you wish to use for sending the email).

### Step 2: Enable 2-Step Verification

Before you can create an App password, you need to enable **2-Step Verification** for your account.

1. **Go to the Security section**:
    
    - In your Google Account dashboard, select **Security** from the left-hand menu.
2. **Enable 2-Step Verification**:
    
    - In the **Signing in to Google** section, find **2-Step Verification** and click on it.
    - Click on the **Get Started** button.
    - Follow the instructions to enable 2-Step Verification using your mobile number or the Google Authenticator app.

### Step 3: Generate an App Password

Once 2-Step Verification is enabled, you can generate an App password.

1. **Go back to the Security section**:
    
    - Navigate back to the **Security** section.
2. **Create an App password**:
    
    - In the **Signing in to Google** section, after enabling 2-Step Verification, you will see an option called **App passwords**. Click on it.

If you do not see this option, go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

Now that you’ve reached the App password generation page, follow these steps:

1. In the box where it asks for a name, enter a name for your App password. This can be anything.

A 16-character password will be generated for you. Copy the password. The password will look something like this:

```python
abcd efgh ijkl mnop
```



Use this password in your Python code in place of your actual Gmail password.

Now, with this App password, you can send your email without any issues.

**Note:** Your App password will only be shown once, so make sure to save it securely or enter it directly into your code.