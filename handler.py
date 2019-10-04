import json
import requests

# Main

def getIp2(event, context):
    url = "https://www.jsonip.com"
    resp = requests.get(url)
    respJson = json.loads(resp.text)

    response = {
        "statusCode": 200,
        "body": respJson['ip']
    }

    print(response)
    return response

seleniumTest("", "")