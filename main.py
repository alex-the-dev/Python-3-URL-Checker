import csv
import requests
import smtplib
import re
import config


def get_urls(cvs_list):
	with open(cvs_list, 'r') as f:
		reader = csv.reader(f)
		urllist = list(reader)
		
	return(urllist)
	
def check_url(url):
	try:
		r = requests.head(url)
		
		return r.status_code
		#print(url + "-" + str(r.status_code))

	except requests.ConnectionError:
		#print(url + "failed to connect")
		return "Failed to connect"

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

	
	
urllist = get_urls(config.url_list)
urls = urllist[0]

dead_urls = {}
print("Checking the the following URLS: \n" + str(urls) + "\n -==========================-")
for url in urls:
	status_code = check_url(url)
	print(url + " - " + str(status_code))
	
	if config.email_list and status_code in config.status_codes:
		dead_urls[url] = status_code
	
print("-==========================-")	

if config.email_list and dead_urls:

	email(dead_urls)