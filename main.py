from csvreader import read_file
from fetchhead import fetch_header
from smtpmailer import email
import config



urllist = read_file(config.url_list)

urls = urllist[0]

dead_urls = {}
print("Checking the the following URLS: \n" + str(urls) + "\n -==========================-")
for url in urls:
	status_code = fetch_header(url)
	print(url + " - " + str(status_code))
	
	if config.email_list and status_code in config.status_codes:
		dead_urls[url] = status_code
	
print("-==========================-")
if dead_urls:
	print("The following URLS were caught" + str(dead_urls))

if config.email_list and dead_urls:
	email(dead_urls)
