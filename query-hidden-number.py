import requests
import time
import sys

LOWER_BOUND = 0
UPPER_BOUND = 1000

# Copied all request headers from chrome dev tools, just in case backend was looking for these
headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.9",
	"Authorization": "Basic cmVtZWV0aW5nOnF1aXo=",
	"Cache-Control": "no-cache",
	"Content-Length": "10",
	"Content-Type": "application/x-www-form-urlencoded",
	"Host": "remeeting.com",
	"Origin": "https://remeeting.com",
	"Pragma": "no-cache",
	"Referer": "https://remeeting.com/quiz/",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

# Check all numbers in the range (LOWER_BOUND, UPPER_BOUND)
for i in range(LOWER_BOUND, UPPER_BOUND):
	data = {
		"number": i
	}

	response = requests.post("https://remeeting.com/quiz/python_script.cgi", headers=headers, data=data)
	line_3 = response.text.split('\n')[2]
	sorry_check = line_3[:5]

	# Exit if we found the number, keep going otherwise
	if sorry_check != "Sorry":
		print("Response for {0} was{1}".format(i, response.text))
		print("Number found: " + str(data))		
		sys.exit(0)
	else:
		print("Incorrect number: " + str(data))

	time.sleep(0.1)

# Checked all numbers in the range (LOWER_BOUND, UPPER_BOUND), but they were all wrong
print("Number not found. Checked all numbers from {0} to {1}".format(LOWER_BOUND, UPPER_BOUND))
sys.exit(0)