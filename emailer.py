def sendemail():
    import smtplib
    import getpass
    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
    smtp_object.ehlo()
    smtp_object.starttls()
    email = input('email:')
    password = getpass.getpass('password:')
    smtp_object.login(email,password)
    from_ = email
    to = input('to whom you want to send')
    subject = input('subject:')
    content = input('content :')
    msg = 'Subject:' + subject + '\n' + content + '\n'+ "A EMAIL SENT USING RAUNAKS EMAILER APP!"
    smtp_object.sendmail(from_,to,msg)
    print ('email succesfuly sent !')
