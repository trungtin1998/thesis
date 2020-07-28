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
