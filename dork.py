import subprocess                                                                                      
subprocess.call('clear', shell=True)                                                                   
                                                                                                       
print(" ▄▀ █▀▀▄ ▄▀▄ ▄▀▀ █░░     ▄▀▀ ▀ ▀█▀ █▀▀ ▄▀▀ ")                                                   
print(" █░ █▐█▀ █▀█ ░▀▄ █▀▄     ░▀▄ █ ░█░ █▀▀ ░▀▄ ")                                                   
print(" ░▀ ▀░▀▀ ▀░▀ ▀▀░ ▀░▀     ▀▀░ ▀ ░▀░ ▀▀▀ ▀▀░ ")                                                   
print("                  ")                                                                            
print("                                   MAKE BY ./Spy")                                          
                                                                                                       
                                                                                                       
while True:                                                                                            
    import requests as r                                                                               
    import socket                                                                                      
    from bs4 import BeautifulSoup as b                                                                 
    try:                                                                                               
        ip = socket.gethostbyname("www.google.com")                                                    
        print("---------------------     ")                                                            
        print("[@] Internet: Active")                                                                  
        print("________________________________________________________________________")              
        print("               ")                                                                       
        inp = input("Enter Dork:  ")                                                                   
        if inp == "close()":                                                                           
            close()                                                                                    
        url = "https://www.google.com/search?q="+inp                                                   
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189"}                                     
        res = r.get(url, headers=headers)                                                              
        soup = b(res.content, 'html.parser')                                                           
        results = soup.find_all("div",{"class":"yuRUbf"})                                              
        h = []                                                                                         
        for i in range(len(results)):                                                                  
            h.append(results[i].find('a')['href'])                                                     
            for k in h:                                                                                
                print(k)                                                                               
    except:                                                                                            
        print("[@] Internet: Not Active")                                                              
        exit()  
