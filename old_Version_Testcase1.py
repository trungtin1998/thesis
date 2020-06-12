#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import requests
import json

BASEURL = "http://192.168.255.200:9200/_search"
QUERY = json.dumps({
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
                        "gte": "2020-05-10T15:59:56.888Z",
                        "lte": "2020-06-09T15:59:56.888Z",
                        "format": "strict_date_optional_time"
                    }
                }
            }]
        }
    }
})

HEADER = {"Content-Type" : "application/json"}

def TestCase1():
    try:
        # Send Query to ELK
        response = requests.post(BASEURL, headers = HEADER, data = QUERY)
        return response
    except:
        print("Error when create Post Request")
        exit()

if __name__ == "__main__":
    response = TestCase1()
    try:
        resp_text = json.loads(response.text)
        print(resp_text)
    except:
        print("cURL to ELK error")
        resp_text = error
