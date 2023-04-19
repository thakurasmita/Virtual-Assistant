import requests
import json
def chatbot(text):
    try :
    
            url = "https://ai-chatbot.p.rapidapi.com/chat/free"

            querystring = {"message":text,"uid":"user1"}

            headers = {
                "X-RapidAPI-Key": "1f145e5d5cmsh5097b62c4a1a99fp14107ejsnd068aac2b9f6",
                "X-RapidAPI-Host": "ai-chatbot.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            d = json.loads(response.text)
            data = d['chatbot']['response']
            return data
    except:
        url = "https://aeona3.p.rapidapi.com/"

        querystring = {"text":f"{text}? ","userId":"12312312312"}

        headers = {
            "X-RapidAPI-Key": "1f145e5d5cmsh5097b62c4a1a99fp14107ejsnd068aac2b9f6",
            "X-RapidAPI-Host": "aeona3.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        d = json.loads(response.text)
        data = d['chatbot']['response']
        return data