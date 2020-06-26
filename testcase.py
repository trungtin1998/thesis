#!/usr/bin/python
import requests
import json
import datetime
from sys import argv
script = argv
script = str(script)[2:-5]

# Global Variables
DIR = "Testcase/"
BASEURL = "http://192.168.255.200:9200/_search"
HEADER = {"Content-Type" : "application/json"}
threats = ["Test case 1 PsExec", "Test case 2 Powershell", "Test case 3 WinRS"]

# Get current time and get time before 5 minutes
def getTimestamp():
    test1 = datetime.datetime.now()
    # Convert from Asia/Ho_Chi_Minh to UTC+0 (minus 7 hours)
    test1 -= datetime.timedelta(hours=7)
    test2 = test1 - datetime.timedelta(minutes=5)
    s1 = test1.strftime("%Y-%m-%dT%H:%M:%S.327Z")
    s2 = test2.strftime("%Y-%m-%dT%H:%M:%S.327Z")
    return [s2, s1]

# Send Post Request to ELK
def postRequest(data):
    try:
        # Send Query to ELK
        l = getTimestamp()
        tmp = data.replace("AAAAAAAAAAAA", l[0])
        tmp = tmp.replace("BBBBBBBBBBBB", l[1])
        response = requests.post(BASEURL, headers = HEADER, data = tmp)
        return response
    except:
        print("Error when create Post Request")
        exit()

# Print Response as prettyprint Format
def printResponse(response):
    parsed = json.loads(response.text)
    #print(json.dumps(parsed, indent=4, sort_keys=True))

# Recognize attack
def recognizeAttack(response):
    parsed = json.loads(response.text)
    #print("Tong so event la: %s"%(parsed["hits"]["total"]["value"]))
        #print(json.dumps(parsed, indent=4, sort_keys=True))
    return parsed

if __name__ == "__main__":
    fname = "Testcase/" + str(argv[1])
    print(fname)
    with open(fname) as json_file:
        data = json.load(json_file)
        data = json.dumps(data)

    response = postRequest(data)
    try:
        printResponse(response)
        res = recognizeAttack(response)
        print("Tong so event la: %d"%(res["hits"]["total"]["value"]))
        if res["hits"]["total"]["value"] != 0:
            print("Co su tan cong tu %s"%(argv[1]))
            print("\n--------------------------\n")
            print(json.dumps(res, indent=4, sort_keys=True))
        else:
            print("Khong co tan cong")
    except Exception as e:
        print("cURL to ELK error")
        print(e)
        exit()