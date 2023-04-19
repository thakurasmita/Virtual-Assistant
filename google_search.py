import googlesearch
import requests
import json


def google_search(query):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    
    # to search
    
    
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        if(j.startswith('https://en.wikipedia.org/wiki/')):
            content = j.replace('https://en.wikipedia.org/wiki/','')
            content = content.replace('_(film)','')
            print(content)
            break
    url = "https://online-movie-database.p.rapidapi.com/auto-complete"

    querystring = {"q":content}

    headers = {
        "X-RapidAPI-Key": "1f145e5d5cmsh5097b62c4a1a99fp14107ejsnd068aac2b9f6",
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    d = json.loads(response.text)
    data = d['d']
    actors = ''
    for i in data:
        if(i['s']!=""):
            actors+=i['s']
            break
    # print(actors)
    return actors





