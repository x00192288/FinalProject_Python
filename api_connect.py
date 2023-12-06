import requests
import json

def GetDublin(): #schedule this to be run every x mins and write to table in database, probably mariadb or mysql 
    try:
         
        response = requests.get("http://api.waqi.info/feed/dublin/?token=404010c7adc3ea4857f096fd18785435b4da0d44")

        #print(response.content)
    except:
        raise Exception("Error returning Dublin search")
    
    return response.content 




def printDublin():
    response = GetDublin()
    loaded = json.loads(response)
    data = (loaded["data"])

    aqi = (data["aqi"])
    idx = (data["idx"])
    attributionslist = []
    attributions = (data["attributions"])
    for i in attributions:
        attributionslist.append(i["url"])


    city = data["city"]
    longitude = city["geo"][0]
    latitude = city["geo"][1]
    location = city["name"]
    dominentpol = (data["dominentpol"])

    iaqi = data["iaqi"]
    humidity = iaqi["h"]["v"]
    no2 = iaqi["no2"]["v"]
    o3 = iaqi["o3"]["v"]
    pressure = iaqi["p"]["v"]
    pm10 = iaqi["pm10"]["v"]
    pm25 = iaqi["pm25"]["v"]
    temperature = iaqi["t"]["v"]
    wind = iaqi["w"]["v"]
    watergauge = iaqi["wg"]["v"]

    timefull = data["time"]["s"]
    timezone = data["time"]["tz"]
    date = timefull.split()[0]
    time = timefull.split()[1]
    print(date)

    

def parseDublin():
    response = GetDublin()
    loaded = json.loads(response)
    data = (loaded["data"])

    aqi = (data["aqi"])
    idx = (data["idx"])
    attributionslist = []
    attributions = (data["attributions"])
    for i in attributions:
        attributionslist.append(i["url"])


    city = data["city"]
    longitude = city["geo"][0]
    latitude = city["geo"][1]
    location = city["name"]
    dominentpol = (data["dominentpol"])

    iaqi = data["iaqi"]
    humidity = iaqi["h"]["v"]
    no2 = iaqi["no2"]["v"]
    o3 = iaqi["o3"]["v"]
    pressure = iaqi["p"]["v"]
    pm10 = iaqi["pm10"]["v"]
    pm25 = iaqi["pm25"]["v"]
    temperature = iaqi["t"]["v"]
    wind = iaqi["w"]["v"]
    watergauge = iaqi["wg"]["v"]

    timefull = data["time"]["s"]
    timezone = data["time"]["tz"]
    date = timefull.split()[0]
    time = timefull.split()[1]
    #print(response)
    tupleSend = tuple([response,location,temperature,time,date])
    return tupleSend

    




    

printDublin()
