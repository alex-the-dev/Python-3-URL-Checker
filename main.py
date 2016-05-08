import csv
import requests

#Location of the csv file containing the URLS
url_list ="urls.csv"

#If you want to email of dead urls change 1 to 0.
email_list = 1
dead_codes = [404]

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


urllist = get_urls(url_list)
urls = urllist[0]

dead_urls = {}
print("Checking the the following URLS: \n" + str(urls) + "\n -==========================-")
for url in urls:
	status_code = check_url(url)
	print(url + " - " + str(status_code))
	
	if email_list and status_code in dead_codes:
		dead_urls[url] = status_code
	
print("-==========================-")	

