def sendemail():
    import smtplib
    import getpass
    import speech_recognition as sr
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source :
            print('speak the subject.....')
            voice = listener.listen(source)
            sub = listener.recognize_google(voice)
        with sr.Microphone() as source1:
            print('speak the body of th mail....')
            voice1 = listener.listen(source1)
            body = listener.recognize_google(voice1)
    except:
        pass 
        
    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
    smtp_object.ehlo()
    smtp_object.starttls()
    email = input('email:')
    password = getpass.getpass('password:')
    smtp_object.login(email,password)
    from_ = email
    to = input('to whom you want to send')
    subject = sub
    content = body
    msg = 'Subject:' + subject + '\n' + content + '\n'+ "A EMAIL SENT USING voice RAUNAKS EMAILER APP!"
    smtp_object.sendmail(from_,to,msg)
    print ('email succesfuly sent !')
sendemail()
