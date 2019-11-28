import requests
url="https://www.fast2sms.com/dev/bulk"

headers = {'authorization': "YOUR_AUTH_KEY",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}

def SendSms(message,phone_no_list):
    payload = "sender_id=FSTSMS&message=%s&language=english&route=p&numbers=%s",(message,phone_no_list)
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
