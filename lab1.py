import requests  # εισαγωγή της βιβλιοθήκης
import re
import datetime

# URL χρήστη
url = input ("Please give me the url you want (e.g. http://google.com ) : ")
try :
    # Αίτημα HTTP στο URL του χρήστη
    with requests.get(url) as response: 
        #Headers της απόκρισης HTTP
        print(f"\nThe Headers for this URL < {url}> are : \n\n  {response.headers} \n\n")

        ## τροποποίηση

        #server
        server= response.headers.get("Server")
        
        if server :
            print(f"Server : {server}")
        else:
            print("no server has been found")
        
        # cookies and exp date
        cookies = response.cookies
        if cookies :
            for cookie in cookies:
                print(f"Cookies <name=value> : {cookie.name} = {cookie.value}")
                #print("Cookie Value:", cookie.value)
                try:
                    print("Cookie Exp date:", datetime.datetime.fromtimestamp(cookie.expires).strftime('%d-%m-%Y'))
                except :
                    print("No date has been found")
        else :
            print("No Cookies has been found")
except : print("Wrong URL ... Bye...")