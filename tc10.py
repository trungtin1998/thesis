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
def parsedJSON(response):
    parsed = json.loads(response.text)
    return parsed

# Time Substration
def timeSubstraction(t1, t2):
    if (t1 >= t2):
        return (t1 - t2).total_seconds()
    else:
        return (t2 - t1).total_seconds()

# Detect test case 10: WCE Remote Login
def recognizeWCERemoteLogin(listArgs):
    # Kiem tra co phai dang: wce.exe -s sv:WINSRV2008:NT:LM
    ok = 0
    if listArgs.count("-s") != 0 and len(listArgs) == 3:
        for s in listArgs:
            # Kiem tra xem co phai dang sv:WINSRV2008:NT:LM
            if s.count(":") == 3:
                ok += 1
            # Kiem tra xem co phai la file exe va duoc thuc thi tai C:\Windows\System32
            elif s.find("C:\Windows\system32") != -1 and s[-4:] == ".exe":
                ok += 1
        if ok == 2:
            return True
    return False

# Distinguish WCE - Password and Hash Dump and WCE - Remote Login
def wce(a):
    with open(DIR + "testcase10_auxiliary") as json_file:
        data = json.load(json_file)
        data = json.dumps(data)
    response = postRequest(data)
    b = parsedJSON(response)
    # a is list of event wceaux.dll
    # b is list of event 1 at sysmon (catch wce.exe -s) 
    n = a["hits"]["total"]["value"]
    m = b["hits"]["total"]["value"]

    tc9 = []
    tc10 = []
    j = 0

    for i in range(n):
        t1 = a["hits"]["hits"][i]["_source"]["@timestamp"]
        t1 = datetime.datetime.strptime(t1, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        t2 = b["hits"]["hits"][j]["_source"]["@timestamp"]
        t2 = datetime.datetime.strptime(t2, "%Y-%m-%dT%H:%M:%S.%fZ")
        if timeSubstraction(t1, t2) < 1 and recognizeWCERemoteLogin(b["hits"]["hits"][j]["_source"]["process"]["args"]):
            tc10.append(b["hits"]["hits"][j])
            j += 2
            continue
        else:
            tc9.append(a["hits"]["hits"][i])
            j += 1
            continue
    print "Test case 9\n\n\n\n"
    print len(tc9)
    for tmp in tc9:
        print tmp["_source"]["process"]
    print "Test case 10\n\n\n\n"
    print len(tc10)
    for tmp in tc10:
        print tmp["_source"]["process"]["args"]


if __name__ == "__main__":
    fname = "Testcase/" + str(argv[1])
    print(fname)
    with open(fname) as json_file:
        data = json.load(json_file)
        data = json.dumps(data)

    response = postRequest(data)
    if 1==1:
        printResponse(response)
        res = parsedJSON(response)
        print("Tong so event la: %d"%(res["hits"]["total"]["value"]))
        if res["hits"]["total"]["value"] != 0:
            wce(res)
            #print("Co su tan cong tu %s"%(argv[1]))
            #print("\n--------------------------\n")
            #print(json.dumps(res, indent=4, sort_keys=True))
        else:
            print("Khong co tan cong")
    #except Exception as e:
        #print("cURL to ELK error")
        #print(e)
        #exit()
