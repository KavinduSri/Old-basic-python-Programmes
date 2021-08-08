import requests as re
import bs4
from bs4 import BeautifulSoup as s
print("""

██╗░░██╗░█████╗░░██████╗████████╗  ██╗██████╗░
██║░░██║██╔══██╗██╔════╝╚══██╔══╝  ██║██╔══██╗
███████║██║░░██║╚█████╗░░░░██║░░░  ██║██████╔╝
██╔══██║██║░░██║░╚═══██╗░░░██║░░░  ██║██╔═══╝░
██║░░██║╚█████╔╝██████╔╝░░░██║░░░  ██║██║░░░░░
╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░  ╚═╝╚═╝░░░░░
                                            Created by ./Spy""")

print(" ")
while True:
#For enter host
    try:
        i = input("Enter Host: ")
        print(" ")
    
    
        url = "https://check-host.net/ip-info?host="+i
        hed = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
#for send get requests to the web site and get source of web site
        res = re.get(url, headers=hed).text
#pass web source to beauti full soup
        html_parser = s(res,"html.parser")
#get ekement tags
        find_tag = html_parser.find_all("td")
#print Its
#print(rc[0])
        tag_var = find_tag[0]
        l = tag_var.td.strong.text
        print("             IP ADDRESS IS " , l)
        print()

    except:
        print("              Unknow Host")
        print()
