#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import json
import datetime
from sys import argv
script = argv
script = str(script)[2:-5]

# Global Variables
BASEURL = "http://192.168.255.200:9200/_search"
QUERY =json.dumps({
    "query": {
        "bool": {
            "filter": [{
                "match_all": {}
            }, {
                "match_phrase": {
                    "event.code": "7045"
                }
            }, {
                "match_phrase": {
                    "winlog.event_data.ImagePath": "%SystemRoot%\\PSEXESVC.exe"
                }
            }, {
                "range": {
                    "@timestamp": {
                        "gte": "AAAAAAAAAAAA",
                        "lte": "BBBBBBBBBBBB",
                        "format": "strict_date_optional_time"
                    }
                }
            }]
        }
    }
})
HEADER = {"Content-Type" : "application/json"}

# Get current time and get time before 5 minutes
def getTimestamp():
    test1 = datetime.datetime.now()
    test2 = test1 - datetime.timedelta(minutes=5)
    s1 = test1.strftime("%Y-%m-%dT%H:%M:%S.888Z")
    s2 = test2.strftime("%Y-%m-%dT%H:%M:%S.888Z")
    return [s2, s1]

# Send Post Request to ELK
def TestCase1():
    try:
        # Send Query to ELK
        l = getTimestamp()
        tmp = QUERY.replace("AAAAAAAAAAAA", l[0])
        tmp = tmp.replace("BBBBBBBBBBBB", l[1])
        response = requests.post(BASEURL, headers = HEADER, data = tmp)
        return response
    except:
        print("Error when create Post Request")
        exit()

# Print Response as prettyprint Format
def printResponse(response):
    parsed = json.loads(response.text)
    print(json.dumps(parsed, indent=4, sort_keys=True))

# Recognize attack
def recognizeAttack(response):
    parsed = json.loads(response.text)
    print("Tong so event trong %s la: %s"%(script, parsed["hits"]["total"]["value"]))


if __name__ == "__main__":
    response = TestCase1()
    try:
        printResponse(response)
        recognizeAttack(response)
    except:
        print("cURL to ELK error")
        exit()


