# Python-3-URL-Checker
A URL status checker built with python 3

<h2>About</h2>
This project will read a list of URLs from a CSV file and return the status of the site.

<h2>Dependancies</h2>
This script requires the Python 3 modules: requests and csv

<h2>How to Use</h2>
Enter the URLS that you wish to check into the urls.csv file seperated by commas.<br>
e.g.<br>
http://www.google.com, http://www.github.com, http://www.python.com
<br>
Please note that all urls <strong>must</strong> have http:// included in the url.
<br>
If you wish to email the results change the settings in config.py.
Run the script from the command line by typing python main.py while in the same directory as the script.

<h2>Config.py</h2>
will email report of urls, change to 0 to disable email reporting.<br>
```
email_list
```
 This is a list of status codes you want the script to report on.
```
status_codes
```
your SMTP email user name. This is the username you are sending the email from.
```
user_name
```
SMTP password
```
password
```
SMTP email address
```
email_address
```
The email address smtp e.g. smtp.google.com
```
smtp_server
```
The email address smtp port e.g. 25, 587
```
smtp_port
```
The destonation email address for the URL report
```
email_dest_address
```

<h2> Status Codes </h2>
<ul>
<li>1×× Informational</li>
<li>100 Continue</li>
<li>101 Switching Protocols</li>
<li>102 Processing</li>
<li>2×× Success</li>
<li>200 OK</li>
<li>201 Created</li>
<li>202 Accepted</li>
<li>203 Non-authoritative Information</li>
<li>204 No Content</li>
<li>205 Reset Content</li>
<li>206 Partial Content</li>
<li>207 Multi-Status</li>
<li>208 Already Reported</li>
<li>226 IM Used</li>
<li>3×× Redirection</li>
<li>300 Multiple Choices</li>
<li>301 Moved Permanently</li>
<li>302 Found</li>
<li>303 See Other</li>
<li>304 Not Modified</li>
<li>305 Use Proxy</li>
<li>307 Temporary Redirect</li>
<li>308 Permanent Redirect</li>
<li>4×× Client Error</li>
<li>400 Bad Request</li>
<li>401 Unauthorized</li>
<li>402 Payment Required</li>
<li>403 Forbidden</li>
<li>404 Not Found</li>
<li>405 Method Not Allowed</li>
<li>406 Not Acceptable</li>
<li>407 Proxy Authentication Required</li>
<li>408 Request Timeout</li>
<li>409 Conflict</li>
<li>410 Gone</li>
<li>411 Length Required</li>
<li>412 Precondition Failed</li>
<li>413 Payload Too Large</li>
<li>414 Request-URI Too Long</li>
<li>415 Unsupported Media Type</li>
<li>416 Requested Range Not Satisfiable</li>
<li>417 Expectation Failed</li>
<li>418 I'm a teapot</li>
<li>421 Misdirected Request</li>
<li>422 Unprocessable Entity</li>
<li>423 Locked</li>
<li>424 Failed Dependency</li>
<li>426 Upgrade Required</li>
<li>428 Precondition Required</li>
<li>429 Too Many Requests</li>
<li>431 Request Header Fields Too Large</li>
<li>444 Connection Closed Without Response</li>
<li>451 Unavailable For Legal Reasons</li>
<li>499 Client Closed Request</li>
<li>5×× Server Error</li>
<li>500 Internal Server Error</li>
<li>501 Not Implemented</li>
<li>502 Bad Gateway</li>
<li>503 Service Unavailable</li>
<li>504 Gateway Timeout</li>
<li>505 HTTP Version Not Supported</li>
<li>506 Variant Also Negotiates</li>
<li>507 Insufficient Storage</li>
<li>508 Loop Detected</li>
<li>510 Not Extended</li>
<li>511 Network Authentication Required</li>
<li>599 Network Connect Timeout Error</li>
</ul>

list from [https://httpstatuses.com/](https://httpstatuses.com/). For More infomation on HTTP status codes checkout the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
