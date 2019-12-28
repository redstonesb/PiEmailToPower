#code peaces put together and added onto by Sidney Bakken
#for raspberry pi


import imaplib, email, os
from gpiozero import LED
import time

#info for reading emails
user = '_____@gmail.com' #enter your email adress must be gmail
password = 'Password' #enter your email password
imap_url = 'imap.gmail.com'

lOn = "1111" #code to turn light on, must be 4 charicters long
lOff = "0000" #code to turn light off, must be 4 charicter long
led = LED(26) #pin light is attached to



#number of emails after last check
numOfE = 0

#code that cheks for a password
def check_for_password():

    #checking the email
    def get_body(msg):
        if msg.is_multipart():
            return get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None,True)

    #open email
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select("INBOX")

    #read email
    result, data = con.fetch((obj.select('Inbox')[1][0]),'(RFC822)')
    raw = email.message_from_bytes(data[0][1])

    #convert output to string
    writing = str(get_body(raw))

    #def pass code as the 4 letters in the string
    Passcode = writing[2:6]

    print(Passcode)

    #do what the pass code says or type wrong password if it doesnt match
    if Passcode == lOn:
        led.on()
        print("LIGHTS ON")

    elif Passcode == lOff:
        print("LIGHTS OFF")
        led.off()
    else:
        print("wrong password")


while True:

    #wate 5 secounds before checking again
    time.sleep(5)

    #tell the user the program is running
    print("running")

    # info for counting emails
    obj = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    obj.login(user, password)

    # isolate number of emails
    emailNum = str(obj.select('Inbox'))
    emailNum = emailNum[9:-1]
    emailNum = emailNum.replace("]","")
    emailNum = emailNum.replace("'","")
    print("email number we are on:",emailNum)

    #run the checking program if a email is receaved
    if int(numOfE) < int(emailNum):
        check_for_password()
        numOfE = emailNum
Email lights control SAFE.py
Displaying Email lights control SAFE.py.
