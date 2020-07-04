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
    test2 = test1 - datetime.timedelta(hours = 2)
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
        print tmp
        response = requests.post(BASEURL, headers = HEADER, data = tmp)
        return response
    except:
        print("Error when create Post Request")
        exit()

# Print Response as prettyprint Format
def printResponse(response):
    parsed = json.loads(response)
    print(json.dumps(parsed, indent=4, sort_keys=True))

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
            elif s.find("C:\\Windows\\system32") != -1 and s[-4:] == ".exe":
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

# Get response from server by loading query from file
## fname is filename of file containing Query DSL
def sendRequest(fname):
    with open(DIR + fname) as json_file:
        data = json.load(json_file)
        data = json.dumps(data)
    response = postRequest(data)
    res = parsedJSON(response)
    return res

# Convert timestamp type JSON to timestamp type datetime
def convert2Datetime(time):
    return datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")

def csvde_at_destination():
    if 1== 1:
        # catch event 5156
        a = sendRequest("testcase21_catch5156")
        # catch event 4624
        b = sendRequest("testcase21_catch4624")
        
        ok = 0
        res = []
        for ai in a["hits"]["hits"]:
            t1 = convert2Datetime(ai["_source"]["@timestamp"])
            for bj in b["hits"]["hits"]:
                t2 = convert2Datetime(bj["_source"]["@timestamp"])
                
                if timeSubstraction(t1,t2) >= 1:
                    continue
                if ai["_source"]["winlog"]["event_data"]["DestAddress"] == bj["_source"]["source"]["ip"] and int(ai["_source"]["winlog"]["event_data"]["DestPort"]) == int(bj["_source"]["source"]["port"]):
                    print bj["_source"]["winlog"]["event_data"]["TargetUserName"]
                    if bj["_source"]["winlog"]["event_data"]["TargetUserName"] != "WINSRV$":
                        ok += 1
                        res.append(bj["_source"])
        if ok != 0:
            print res
        print "Khong co tan cong"

def checkName(name):
    # Allow Computer
    if name.find("$") != -1:
        return True
    # Allow 2 user account sv and administrator to remote login
    if name == "sv" or name == "administrator":
        return True
    return False

def golden_ticket():
    # Catch all events 4769
    response = sendRequest("testcase11")
    print response["hits"]["total"]["value"]
    index = 1
    res = []
    for tmp in response["hits"]["hits"]:
        print index
        index+=1
        try:
            i = tmp["_source"]["winlog"]["event_data"]["TargetUserName"].find("@")
            if i != -1:
                name = tmp["_source"]["winlog"]["event_data"]["TargetUserName"][:i]
                domain = tmp["_source"]["winlog"]["event_data"]["TargetUserName"][i+1:]
                if checkName(name) == False or domain.isupper() == False:
                   res.append(tmp)
        except:
            # Filter all event having blank user account name
            continue
    return res

def quarksPwDump(res):
    result = []
    for tmp in res["hits"]["hits"]:
        s = tmp["_source"]["file"]["path"]
        if s.find("C:\\Users\\") < s.find("\\AppData\\Local\\Temp\\SAM") and s.find("dmp") != -1:
            result.append(tmp)
    return result


if __name__ == "__main__":
    res = sendRequest("testcase8")
    res = quarksPwDump(res)
    for tmp in res:
        print(json.dumps(tmp, indent=4, sort_keys=True))