import smtplib
import re
import config

def email(message):
	server = smtplib.SMTP(config.smtp_server, config.smtp_port)
	server.starttls()
	server.login(config.user_name, config.password)
	msg = "Your URL's have been scaned \n"
	msg += "The following dead URLs have been found\n"
	message = (str(message))
	message = re.sub('[\\{\\}]', '', message)
	msg += message
	server.sendmail(config.email_address, config.email_dest_address, msg)
	print("email sent")
	server.quit()