import time
import requests
import json

count = 0


def line_notification(alert_message):
    headers = {'authorization': 'Bearer kHAuKPObW0Bc2kt2ltt1TEQhgbsXmfkAL1LR97OOUXh'}
    url = 'https://notify-api.line.me/api/notify'
    data = {'message': alert_message}
    r = requests.post(url, headers=headers, data=data)


def executeSomething():
    global count

    #code here
    count = count + 1
    print("Executing for : ", count)
    response = requests.get("https://bx.in.th/api/")
    json_data = json.loads(response.text)
    # print("response is ",json_data)
    # print("type of json data is : ", type(json_data))
    current_btc_price = json_data["1"]["last_price"]


    if(current_btc_price>249000):
        line_notification("HIGHER THAN 249000")
    elif(current_btc_price<221000):
        line_notification("LOWER THAN 221000")
    else:
        print("not aleart")

    time.sleep(60)

while True:
    executeSomething()