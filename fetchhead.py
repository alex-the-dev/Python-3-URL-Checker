import requests

def fetch_header(url):
	try:
		r = requests.head(url)
		return r.status_code
	except requests.ConnectionError:
		return "Failed to connect"