import requests


def GetDublin(): #schedule this to be run every x mins and write to table in database, probably mariadb or mysql 
    try:
        response = requests.get("https://api.waqi.info/search/?keyword=dublin&token=404010c7adc3ea4857f096fd18785435b4da0d44")

        print(response.content)
    except:
        raise Exception("Error returning Dublin search")
    
    return response.content 




