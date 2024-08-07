# VOICE BASED EMAIL FOR BLIND PEOPLE

# Introduction 
In a world increasingly driven by digital communication, the visually impaired face unique challenges in accessing and managing email, 
a fundamental tool for personal and professional correspondence. Recognizing the need for inclusivity and accessibility, our project aims 
to bridge this gap by developing a Voice-Based Email System tailored specifically for individuals with visual impairments.

# Scope

## 1. User - Friendly Interface: 

Develop an intuitive and user-friendly interface that relies on voice commands, ensuring individuals with visual 
impairments can efficiently navigate and interact with the email system.

## 2. Speech Recognition Technology: 

Implement advanced speech recognition technology to accurately interpret and
respond to natural language commands, enabling users to compose emails, manage their inbox, and perform other 
essential tasks through voice input.

## 3. Text-to-Speech (TTS) Integration:

Integrate high-quality Text-to-Speech (TTS) technology to convert email content into spoken words, providing 
auditory feedback that enables users to listen to their messages.

## 4. Command Customization:

Allow users to customize voice commands based on their preferences, enhancing the personalization of the system 
and accommodating individual needs.

# Problem Statement:

 Visually impaired individuals face significant challenges in managing emails through traditional graphical user interfaces, 
 which are often not fully accessible or user-friendly for them.

# Solution Statement:

The project provides a voice-based email system that allows blind users to manage their emails using voice commands, 
utilizing speech recognition for command input and text-to-speech for email content output. This system ensures a 
more accessible and convenient way for visually impaired users to interact with their email accounts.

# Assumptions: 

•	Users have internet access.

•	Users possess devices with voice input/output capabilities.

•	Email providers will maintain APIs for email management.

•	Users are proficient with voice technology.

•	Users trust the system with data privacy and legal compliance.

•	Ongoing advancements in speech recognition and synthesis technology.

# Dependencies: 

•	Reliable speech recognition and text-to-speech (TTS) synthesis technologies.

•	Stability and compatibility of email service provider APIs.

•	Stable internet connectivity.

•	Users' devices with compatible hardware and software.

•	Compliance with accessibility standards and regulations.

•	Security protocols of email providers.

•	Robust natural language processing (NLP) libraries.

•	User feedback and testing for continuous improvement

# Technologies Used:

1. Python

2. Google Gmail API

3. pyttsx3 (text-to-speech)
   
4. speech_recognition
   
5. pickle
   
6. os.path
    
7. date
    
8. base64

# Summary:

The code begins by importing essential libraries: pickle for data serialization, os.path for file path operations,
googleapiclient for interacting with the Gmail API, pyttsx3 for text-to-speech synthesis, speech_recognition for 
voice recognition, date for handling date-related operations, and base64 for encoding email messages. Global variables 
include the Gmail API scopes (SCOPES), a listener object for speech recognition, and an engine object for text-to-speech
synthesis. Key functions are defined for text-to-speech conversion (talk(text)), capturing and transcribing audio (get_audio(command=None)),
Gmail authentication (authenticate_gmail()), checking emails (check_mails(service)), looking up recipient emails (get_recipient_email()), and 
sending emails (send_email(service)). The main loop (main()) welcomes the user and continuously prompts them to read an email, send an email, 
or stop the program, invoking the corresponding actions based on the user's voice commands.

# Outputs

## 1. Asking the user to say commands
   ![VBS](https://github.com/user-attachments/assets/dfa6ed96-5393-458f-824a-771e3a03f254)

## 2. The mail is sent to the specified person.
   ![VBS1](https://github.com/user-attachments/assets/4651f428-9781-49d9-86f7-97a13cc735bc)

## 3. Cancelling the send email process.
   ![VBS2](https://github.com/user-attachments/assets/54145c33-dbe5-4d05-94d8-3684f27d3858)
