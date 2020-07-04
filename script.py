#!/usr/bin/python
import requests
import json
import datetime
from sys import argv
import smtplib
script = argv
script = str(script)[2:-5]

# Global Variables
DIR = "Testcase/"
BASEURL = "http://192.168.255.200:9200/_search"
HEADER = {"Content-Type" : "application/json"}
threats = ["Test case 1 PsExec", "Test case 2 Powershell", "Test case 3 WinRM", "Test case 4 WinRS", "Test case 5 WMIC", "Test case 6 vmiexec.vbs", "Test case 7 PWDump7", "Test case 8 Quarks PwDump", "Test case 9 WCE - Password and Hash Dump", "Test case 10 WCE Remote Login", "Test case 11 Golden Ticket", "Test case 12 SMB/PsExec", "Test case 13 AT Command", "Test case 14 RDP", "Test case 15 Mimikatz", "Test case 16 Ms14-058", "Test case 17 ntdsutil", "Test case 18 vssadmin", "Test case 19 net user", "Test case 20 ", "Test case 21 csvde", "Test case 22 ldifde", "Test case 23 Timestomp", "Test case 24 wevtutil"]
header = ""
body = ""

# Gmail Information
gmail_user = 'sonthantuvea@gmail.com'
gmail_password = 'trungtin1512'
send_to = 'nguyenvana310225@gmail.com'


# Get current time and get time before 5 minutes
def getTimestamp():
    test1 = datetime.datetime.now()
    # Convert from Asia/Ho_Chi_Minh to UTC+0 (minus 7 hours)
    test1 -= datetime.timedelta(hours=7)
    test2 = test1 - datetime.timedelta(minutes=5)
    s1 = test1.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    s2 = test2.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
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
    print(json.dumps(parsed, indent=4, sort_keys=True))

# Parsed JSON
def parsedJSON(response):
    parsed = json.loads(response.text)
    return parsed

# Send gmail using library smtplib
def sendGmail(body):
    subject = "ELK " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (gmail_user, send_to, subject, body)
    
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.starttls()
        smtpserver.login(gmail_user, gmail_password)
        smtpserver.sendmail(gmail_user, send_to, email_text)
        smtpserver.close()

        print('Email sent!')
    except Exception as e:
        print('Something went wrong... ' + str(e))

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

# Test case 8: QuarksPwDump
def quarksPwDump(res):
    result = []
    for tmp in res["hits"]["hits"]:
        s = tmp["_source"]["file"]["path"]
        # Check position of file.path that is C:\Users\[User Account]\AppData\Local\Temp\SAM-[RandomNumber].dmp
        if s.find("C:\\Users\\") < s.find("\\AppData\\Local\\Temp\\SAM") and s.find("dmp") != -1:
            result.append(tmp)
    return result

# Distinguish Test case 9: WCE - Password and Hash Dump and Test case 10: WCE - Remote Login
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

    tc9 = []        # Test case 9: WCE - Password and Hash Dump
    tc10 = []       # Test case 10: WCE - Remote Login
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

    return [tc9, tc10]

# Get response from server by loading query from file
## fname is filename of file containing Query DSL
def sendRequest(fname):
    with open(DIR + fname) as json_file:
        data = json.load(json_file)
        data = json.dumps(data)
    response = postRequest(data)
    try:
        res = parsedJSON(response)
        return res
    except Exception as e:
        print("cURL to ELK error")
        print(str(e))
        exit()

# Convert timestamp type JSON to timestamp type datetime
def convert2Datetime(time):
    return datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")

# Test case 11: Golden Ticket
def checkName(name):
    # Allow Computer
    if name.find("$") != -1:
        return True
    # Allow 2 user account sv and administrator to remote login
    if name == "sv" or name == "administrator":
        return True
    return False

def golden_ticket(response):
    # Catch all events 4769
    res = []
    for tmp in response["hits"]["hits"]:
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

# Test case 21: csvde
def csvde_at_destination():
    #f = open("csvde", "w")
    # catch event 5156
    a = sendRequest("testcase21_catch5156")
    
    tam = json.dumps(a, indent=4, sort_keys=True)
    #f.write(tam)
    # catch event 4624
    b = sendRequest("testcase21_catch4624")
    tam = json.dumps(b, indent=4, sort_keys=True)
    #f.write(tam)

    res = []
    if a["hits"]["total"]["value"] == 0 or b["hits"]["total"]["value"] == 0:
        return res
    for ai in a["hits"]["hits"]:
        t1 = convert2Datetime(ai["_source"]["@timestamp"])
        for bj in b["hits"]["hits"]:
            t2 = convert2Datetime(bj["_source"]["@timestamp"])

            if timeSubstraction(t1,t2) >= 1:
                continue
            try:
                if ai["_source"]["winlog"]["event_data"]["DestAddress"] == bj["_source"]["source"]["ip"] and int(ai["_source"]["winlog"]["event_data"]["DestPort"]) == int(bj["_source"]["source"]["port"]):
                    if bj["_source"]["winlog"]["event_data"]["TargetUserName"] != "WINSRV$":
                        res.append(bj["_source"])
            except:
                print "ERROR: Can't parse"
                print(json.dumps(ai, indent=4, sort_keys=True))
                print(json.dumps(bj, indent=4, sort_keys=True))
    return res


def writeFull(i, n, res):
    global header
    global body 
    print("\tPhat hien su tan cong cua %s"%(threats[i - 1]))
    header += "Phat hien su tan cong cua %s\n"%(threats[i - 1])
    header += "\tTong event: %s\n"%(n)
    body += "\n-----------------------------------------------------------------------------------\n"
    body += threats[i - 1]
    body += "\n-----------------------------------------------------------------------------------\n"
    body += json.dumps(res, indent=4, sort_keys=True)
    body += "\n-----------------------------------------------------------------------------------\n"

def writeHalf(i, n, res):
    global header
    global body 
    print("\tPhat hien su tan cong cua %s"%(threats[i - 1]))
    header += "Phat hien su tan cong cua %s\n"%(threats[i - 1])
    header += "\tTong event: %s\n"%(n)
    body += "\n-----------------------------------------------------------------------------------\n"
    body += threats[i - 1]
    body += "\n-----------------------------------------------------------------------------------\n"
    for tmp in res:
        body += json.dumps(tmp, indent=4, sort_keys=True)
    body += "\n-----------------------------------------------------------------------------------\n"

if __name__ == "__main__":
    for i in range(1,25):
        if i != 10:
            print(threats[i - 1])
        if i == 4  or i == 10 or i == 12 or i == 15 or i == 16 or i == 20:
            continue
        fname = "testcase" + str(i)
        res = sendRequest(fname)
        if res["hits"]["total"]["value"] != 0 and i != 21:
            # Test case 8: Quarks PwDump
            if i == 8:
                res = quarksPwDump(res)
                if len(res) != 0:
                    writeHalf(i, len(res), res)
            # Distingush Test case 9 and Test case 10
            elif i == 9:
                res = wce(res)
                # Test case 9: WCE - Password and Hash Dump
                if len(res[0]) != 0:
                    writeHalf(9, len(res[0]), res)
                # Test case 10: WCE - Remote Login
                if len(res[1]) != 0:
                    print(threats[10 - 1])
                    writeHalf(10, len(res[1]), res)
            # Test case 11: Golden ticket
            elif i == 11:
                res = golden_ticket(res)
                if len(res) != 0:
                    writeHalf(i, len(res), res)
            else:
                writeFull(i, res["hits"]["total"]["value"], res)
        # Catch Event at Destination and Source

        elif i == 21:
            # "res" stored event at Source
            if res["hits"]["total"]["value"] != 0:
                writeFull(i, res["hits"]["total"]["value"], res)
                header += "\tTai nguon\n"
            # We need to catch event at Destination
            res = csvde_at_destination()
            if len(res) != 0:
                writeHalf(i, len(res), res)
                header += "\tTai dich\n"


    if header != "":
        #sendGmail(header + body)
        res = header+body
        print header
        print body
    else:
        print("Khong phat hien bat ki nguy co nao")

