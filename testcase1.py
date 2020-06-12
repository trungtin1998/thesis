#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import json
import datetime

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

# Get current time and time after 5 minutes
def getTimestamp():
    test1 = datetime.datetime.now()
    test2 = test1 + datetime.timedelta(minutes=5)
    s1 = test1.strftime("%Y-%m-%dT%H:%M:%S.888Z")
    s2 = test2.strftime("%Y-%m-%dT%H:%M:%S.888Z")
    return [s1,s2]

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

if __name__ == "__main__":
    response = TestCase1()
    try:
        printResponse(response)
    except:
        print("cURL to ELK error")
        resp_text = error


