import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"

# Add the websites you want to block in this list.
website_to_block = ["www.youtube.com", "youtube.com", "www.netflix.com", "netflix.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
		print("Working hours...")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_to_block:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_to_block):
					file.write(line)
			file.truncate()
		print("Fun hours...")
	time.sleep(5)