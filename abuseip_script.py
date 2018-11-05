import requests
from bs4 import BeautifulSoup
import validators

page_number = 1
continue_condition = True

ip_list = []

while continue_condition:
    print("Current page number is: " + str(page_number))
    url = 'https://www.abuseipdb.com/sitemap?page={}'.format(str(page_number))

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "lxml")

    href_tags = soup.find_all(href=True)

    for item in href_tags:
        if validators.ipv4(item.text):
            ip_list.append(item.text)

    continue_condition = False

    for item in href_tags:
        if item.text == "Next »":
            continue_condition = True
    page_number += 1


with open("ip.txt", "w") as text_file:
    for item in ip_list:
        text_file.write("%s\n" % item)

