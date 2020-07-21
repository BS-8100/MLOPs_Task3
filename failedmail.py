import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 465) 
# start SSl for security 
s.startssl()   
# Authentication 
s.login("sender-mail", "password") 
# message to be sent 
message = "Hey Developer, you need to check your code once. Might be this have some error. "
# sending the mail 
s.sendmail("sender-mail", "developer_mail", message) 
# terminating the session 
s.quit()
