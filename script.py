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
            elif s.find("C:\Windows\system32") != -1 and s[-4:] == ".exe":
                ok += 1
        if ok == 2:
            return True
    return False

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

def writeFull(i, n, header, body, res):
    print("\tPhat hien su tan cong cua %s"%(threats[i - 1]))
    header += "Phat hien su tan cong cua %s\n"%(threats[i - 1])
    header += "\tTong event: %s\n"%(n)
    body += "---------------------------------------------------------------------------------------"
    body += threats[9]
    body += "---------------------------------------------------------------------------------------"
    body += json.dumps(res, indent=4, sort_keys=True)

def writeHalf(i, n, header, body, res):
    print("\tPhat hien su tan cong cua %s"%(threats[i - 1]))
    header += "Phat hien su tan cong cua %s\n"%(threats[i - 1])
    header += "\tTong event: %s\n"%(n)
    body += "---------------------------------------------------------------------------------------"
    body += threats[9]
    body += "---------------------------------------------------------------------------------------"
    for tmp in res:
        body += json.dumps(tmp, indent=4, sort_keys=True)

if __name__ == "__main__":
    header = ""
    body = ""
    for i in range(1,25):
        fname = DIR + "testcase" + str(i)
        if i != 10:
            print(threats[i - 1])
        if i == 4  or i == 7 or i == 8 or i == 10 or i == 11 or i == 15 or i == 12 or i == 16 or i == 19 or i ==20:
            continue
        with open(fname) as json_file:
            data = json.load(json_file)
            data = json.dumps(data)
        
        # recognize Attack by sending query to ELK
        response = postRequest(data)
        try:
            res = parsedJSON(response)
            if res["hits"]["total"]["value"] != 0:
                if i == 9:
                    res = wce(res)
                    # Test case 9: WCE - Password and Hash Dump
                    if len(res[0]) != 0:
                        writeHalf(9, len(res[0]), header, body, res)
                    # Test case 10: WCE - Remote Login
                    elif len(res[1]) != 0:
                        print(threats[10 - 1])
                        writeHalf(10, len(res[1]), header, body, res)
                else:
                    writeFull(i, res["hits"]["total"]["value"], header, body, res)
                
                header += "\n"
                body += "\n\n-----------------------------------------------\n\n\n"
        except Exception as e:
            print("cURL to ELK error")
            print(str(e))
            exit()
    if header != "":
        #sendGmail(header + body)
        res = header+body
        print header
    else:
        print("Khong phat hien bat ki nguy co nao")

