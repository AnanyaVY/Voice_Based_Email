from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from google.oauth2 import service_account
import pyttsx3
import speech_recognition as sr
from datetime import date
from email.mime.text import MIMEText
import base64



SCOPES = ["https://www.googleapis.com/auth/gmail.readonly","https://www.googleapis.com/auth/gmail.send"]
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

# ... (previous code)

def get_audio(command=None):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening for a command...")
        if command:
            talk(command)
        audio = r.listen(source)
        said = ""

    try:
        said = r.recognize_google(audio)
        print(said)
    except:
        talk("Didn't get that")

    return said.lower()

# ... (rest of the code)


def authenticate_gmail():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def check_mails(service):
    today = date.today()
    today_main = today.strftime('%Y/%m/%d')

    results = service.users().messages().list(
        userId='me',
        labelIds=["INBOX", "UNREAD"],
        q="after:{0} and category:Primary".format(today_main)
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        talk('No messages found.')
    else:
        talk("{} new emails found".format(len(messages)))
        talk("Do you want to read, send, or skip an email?")
        choice = get_audio()
        print("You said:", choice)  # Debug print

        if "read" in choice:
            for message in messages:
                msg = service.users().messages().get(
                    userId='me',
                    id=message['id'],
                    format='metadata'
                ).execute()

                for add in msg['payload']['headers']:
                    if add['name'] == "From":
                        sender = str(add['value'].split("<")[0])
                        talk("Email from " + sender)
                        talk("Would you like to read this email?")
                        response = get_audio()
                        print("You said:", response)  # Debug print

                        if "yes" in response:
                            talk(msg['snippet'])
                        else:
                            talk("Email skipped.")
        
        elif "send" in choice:
            send_email(service)
        else:
            talk("No action taken.")

# ... (previous code)

# Define an email list as a dictionary where keys are names and values are email addresses
email_list = {
    'john': 'kruthin.cgnr@gmail.com',
    'jane': 'jane@example.com',
    # Add more names and email addresses as needed
}

def get_recipient_email():
    talk("Who is the recipient?")
    recipient_name = get_audio().lower()

    if recipient_name in email_list:
        recipient_email = email_list[recipient_name]
        return recipient_email
    else:
        talk("Recipient not found in the list.")
        return None

def send_email(service):
    recipient_email = get_recipient_email()

    if recipient_email:
        talk("What is the subject of the email?")
        email_subject = get_audio()
        talk("Please dictate the content of the email.")
        email_content = get_audio()

        # Create a message
        message = MIMEText(email_content)
        message['to'] = recipient_email
        message['subject'] = email_subject

        # Encode the message and send it using Gmail API
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        body = {'raw': raw_message}

        try:
            sent_message = service.users().messages().send(userId='me', body=body).execute()
            talk("Email sent successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
            talk("Email could not be sent. Please check the console for details.")

# ... (rest of the code)




def main():
    talk("Welcome to mail service")
    SERVICE2 = authenticate_gmail()

    while True:
        talk("Do you want to read an email or send an email?")
        choice = get_audio().lower()

        if "read" in choice:
            check_mails(SERVICE2)
        elif "send" in choice:
            send_email(SERVICE2)
        elif "stop" in choice:
            exit(0)
        else:
            talk("Invalid choice. Please say 'read' or 'send'.")

if __name__ == "__main__":
    main()


