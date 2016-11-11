import sys
import requests
import json
import re

#Error check
if len(sys.argv) < 5:
    sys.exit("Please enter the image URL!")
elif len(sys.argv) > 5:
    sys.exit("Entered too much argument!")

SrcLat = sys.argv[-4]
SrcLong = sys.argv[-3]
DesLat = sys.argv[-2]
DesLong = sys.argv[-1]

url = "https://maps.googleapis.com/maps/api/distancematrix/json"

querystring = {"units":"imperial","origins": SrcLat + "," + SrcLong, "destinations": DesLat + "," + DesLong,"key":"AIzaSyAUktj-M9l_ABfXV9HrZYol94sH15gtn_k"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "4c0f31a1-c428-152f-d439-d893922eae53"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

jsonData = json.loads(response.text)

data = jsonData['rows'][0]['elements'][0]['duration']['text']
time = re.search(r'\d+', data)
timeNum = int(time.group())

fo = open('stimulation2016 v2.txt','a')
fo.write(DesLat + "\t" + DesLong + "\t" + timeNum + '\n')
fo.close()
