import csv
import requests

#Location of the csv file containing the URLS
url_list ="urls.csv"

def get_urls(cvs_list):
	with open(cvs_list, 'r') as f:
		reader = csv.reader(f)
		urllist = list(reader)
		
	return(urllist)
	
def check_url(url):
	try:
		r = requests.head(url)
		
		print(url + "-" + str(r.status_code))

	except requests.ConnectionError:
		print(url + "failed to connect")


urllist = get_urls(url_list)
urls = urllist[0]


print("Checking the the following URLS: \n" + str(urls) + "\n -==========================-")
for url in urls:
	check_url(url)
	
print("-==========================-")