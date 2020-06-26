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
    #print(json.dumps(parsed, indent=4, sort_keys=True))

# Recognize attack
def recognizeAttack(response):
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


if __name__ == "__main__":
    body1 = ""
    body2 = ""
    for i in range(1,25):
        fname = DIR + "testcase" + str(i)

        if i == 4  or i == 7 or i == 8 or i == 11 or i == 15 or i == 12 or i == 16 or i == 19 or i ==20:
            continue
        print(threats[i - 1])
        with open(fname) as json_file:
            data = json.load(json_file)
            data = json.dumps(data)

        response = postRequest(data)
        try:
            printResponse(response)
            res = recognizeAttack(response)
            if res["hits"]["total"]["value"] != 0:
                print("\tPhat hien su tan cong cua %s"%(threats[i - 1]))
                body1 += "Phat hien su tan cong cua %s\n"%(threats[i - 1])
                body1 += "\tTong event: %s\n"%(res["hits"]["total"]["value"])
                body1 += "\n"
                body2 += json.dumps(res, indent=4, sort_keys=True)
                body2 += "\n\n-----------------------------------------------\n\n\n"
        except Exception as e:
            print("cURL to ELK error")
            print(str(e))
            exit()
    if body1 != "":
        sendGmail(body1 + body2)
    else:
        print("Khong phat hien bat ki nguy co nao")

