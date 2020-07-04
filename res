Test case 1 PsExec
Test case 2 Powershell
Test case 3 WinRM
Test case 4 WinRS
Test case 5 WMIC
	Phat hien su tan cong cua Test case 5 WMIC
Test case 6 vmiexec.vbs
	Phat hien su tan cong cua Test case 6 vmiexec.vbs
Test case 7 PWDump7
Test case 8 Quarks PwDump
Test case 9 WCE - Password and Hash Dump
Test case 11 Golden Ticket
	Phat hien su tan cong cua Test case 11 Golden Ticket
Test case 12 SMB/PsExec
Test case 13 AT Command
Test case 14 RDP
Test case 15 Mimikatz
Test case 16 Ms14-058
Test case 17 ntdsutil
Test case 18 vssadmin
Test case 19 net user
Test case 20 
Test case 21 csvde
Test case 22 ldifde
Test case 23 Timestomp
Test case 24 wevtutil
Phat hien su tan cong cua Test case 5 WMIC
	Tong event: 2
Phat hien su tan cong cua Test case 6 vmiexec.vbs
	Tong event: 2
Phat hien su tan cong cua Test case 11 Golden Ticket
	Tong event: 2


-----------------------------------------------------------------------------------
Test case 5 WMIC
-----------------------------------------------------------------------------------
{
    "_shards": {
        "failed": 0, 
        "skipped": 0, 
        "successful": 94, 
        "total": 96
    }, 
    "aggregations": {
        "2": {
            "buckets": [
                {
                    "doc_count": 2, 
                    "key": 1593855960000, 
                    "key_as_string": "2020-07-04T16:46:00.000+07:00"
                }
            ]
        }
    }, 
    "hits": {
        "hits": [
            {
                "_id": "ULs4GXMB1uvUeW0ZAxtP", 
                "_index": "winlogbeat-7.7.0-2020.07.04", 
                "_score": 0.0, 
                "_source": {
                    "@timestamp": "2020-07-04T09:46:04.702Z", 
                    "@version": "1", 
                    "agent": {
                        "ephemeral_id": "be1a1a61-adaa-4020-9bd9-8ed7dc7e8f8b", 
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
                        "created": "2020-07-04T09:46:07.248Z", 
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
                            "build": "7601.24525", 
                            "family": "windows", 
                            "kernel": "6.1.7601.24520 (win7sp1_ldr_escrow.190828-1732)", 
                            "name": "Windows Server 2008 R2 Datacenter", 
                            "platform": "windows", 
                            "version": "6.1"
                        }
                    }, 
                    "log": {
                        "level": "information"
                    }, 
                    "message": "Process Create:\nRuleName: \nUtcTime: 2020-07-04 09:46:04.702\nProcessGuid: {F4BE2742-4FDC-5F00-0000-0010A65C5900}\nProcessId: 3848\nImage: C:\\Windows\\System32\\cmd.exe\nFileVersion: 6.1.7601.17514 (win7sp1_rtm.101119-1850)\nDescription: Windows Command Processor\nProduct: Microsoft\u00ae Windows\u00ae Operating System\nCompany: Microsoft Corporation\nOriginalFileName: Cmd.Exe\nCommandLine: cmd.exe /c net user > C:\\windows\\temp\\wmi.dll 2>&1\nCurrentDirectory: C:\\Windows\\system32\\\nUser: WINSRV2008\\Administrator\nLogonGuid: {F4BE2742-4FDC-5F00-0000-0020855A5900}\nLogonId: 0x595a85\nTerminalSessionId: 0\nIntegrityLevel: High\nHashes: MD5=5746BD7E255DD6A8AFA06F7C42C1BA41,SHA256=DB06C3534964E3FC79D2763144BA53742D7FA250CA336F4A0FE724B75AAFF386,IMPHASH=D0058544E4588B1B2290B7F4D830EB0A\nParentProcessGuid: {F4BE2742-26BE-5F00-0000-001065DF0200}\nParentProcessId: 2540\nParentImage: C:\\Windows\\System32\\wbem\\WmiPrvSE.exe\nParentCommandLine: C:\\Windows\\system32\\wbem\\wmiprvse.exe -secured -Embedding", 
                    "process": {
                        "args": [
                            "cmd.exe", 
                            "/c", 
                            "net", 
                            "user", 
                            ">", 
                            "C:\\windows\\temp\\wmi.dll", 
                            "2>&1"
                        ], 
                        "entity_id": "{F4BE2742-4FDC-5F00-0000-0010A65C5900}", 
                        "executable": "C:\\Windows\\System32\\cmd.exe", 
                        "name": "cmd.exe", 
                        "parent": {
                            "args": [
                                "C:\\Windows\\system32\\wbem\\wmiprvse.exe", 
                                "-secured", 
                                "-Embedding"
                            ], 
                            "entity_id": "{F4BE2742-26BE-5F00-0000-001065DF0200}", 
                            "executable": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe", 
                            "name": "WmiPrvSE.exe", 
                            "pid": 2540
                        }, 
                        "pid": 3848, 
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
                            "LogonGuid": "{F4BE2742-4FDC-5F00-0000-0020855A5900}", 
                            "LogonId": "0x595a85", 
                            "OriginalFileName": "Cmd.Exe", 
                            "Product": "Microsoft\u00ae Windows\u00ae Operating System", 
                            "TerminalSessionId": "0"
                        }, 
                        "event_id": 1, 
                        "opcode": "Info", 
                        "process": {
                            "pid": 2268, 
                            "thread": {
                                "id": 2892
                            }
                        }, 
                        "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}", 
                        "provider_name": "Microsoft-Windows-Sysmon", 
                        "record_id": 45052, 
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
                "_type": "_doc"
            }, 
            {
                "_id": "ars4GXMB1uvUeW0ZExt2", 
                "_index": "winlogbeat-7.7.0-2020.07.04", 
                "_score": 0.0, 
                "_source": {
                    "@timestamp": "2020-07-04T09:46:09.800Z", 
                    "@version": "1", 
                    "agent": {
                        "ephemeral_id": "be1a1a61-adaa-4020-9bd9-8ed7dc7e8f8b", 
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
                        "created": "2020-07-04T09:46:11.274Z", 
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
                            "build": "7601.24525", 
                            "family": "windows", 
                            "kernel": "6.1.7601.24520 (win7sp1_ldr_escrow.190828-1732)", 
                            "name": "Windows Server 2008 R2 Datacenter", 
                            "platform": "windows", 
                            "version": "6.1"
                        }
                    }, 
                    "log": {
                        "level": "information"
                    }, 
                    "message": "Process Create:\nRuleName: \nUtcTime: 2020-07-04 09:46:09.800\nProcessGuid: {F4BE2742-4FE1-5F00-0000-001005635900}\nProcessId: 4004\nImage: C:\\Windows\\System32\\cmd.exe\nFileVersion: 6.1.7601.17514 (win7sp1_rtm.101119-1850)\nDescription: Windows Command Processor\nProduct: Microsoft\u00ae Windows\u00ae Operating System\nCompany: Microsoft Corporation\nOriginalFileName: Cmd.Exe\nCommandLine: cmd.exe /c del C:\\windows\\temp\\wmi.dll /F > nul 2>&1\nCurrentDirectory: C:\\Windows\\system32\\\nUser: WINSRV2008\\Administrator\nLogonGuid: {F4BE2742-4FDC-5F00-0000-0020855A5900}\nLogonId: 0x595a85\nTerminalSessionId: 0\nIntegrityLevel: High\nHashes: MD5=5746BD7E255DD6A8AFA06F7C42C1BA41,SHA256=DB06C3534964E3FC79D2763144BA53742D7FA250CA336F4A0FE724B75AAFF386,IMPHASH=D0058544E4588B1B2290B7F4D830EB0A\nParentProcessGuid: {F4BE2742-26BE-5F00-0000-001065DF0200}\nParentProcessId: 2540\nParentImage: C:\\Windows\\System32\\wbem\\WmiPrvSE.exe\nParentCommandLine: C:\\Windows\\system32\\wbem\\wmiprvse.exe -secured -Embedding", 
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
                        "entity_id": "{F4BE2742-4FE1-5F00-0000-001005635900}", 
                        "executable": "C:\\Windows\\System32\\cmd.exe", 
                        "name": "cmd.exe", 
                        "parent": {
                            "args": [
                                "C:\\Windows\\system32\\wbem\\wmiprvse.exe", 
                                "-secured", 
                                "-Embedding"
                            ], 
                            "entity_id": "{F4BE2742-26BE-5F00-0000-001065DF0200}", 
                            "executable": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe", 
                            "name": "WmiPrvSE.exe", 
                            "pid": 2540
                        }, 
                        "pid": 4004, 
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
                            "LogonGuid": "{F4BE2742-4FDC-5F00-0000-0020855A5900}", 
                            "LogonId": "0x595a85", 
                            "OriginalFileName": "Cmd.Exe", 
                            "Product": "Microsoft\u00ae Windows\u00ae Operating System", 
                            "TerminalSessionId": "0"
                        }, 
                        "event_id": 1, 
                        "opcode": "Info", 
                        "process": {
                            "pid": 2268, 
                            "thread": {
                                "id": 2892
                            }
                        }, 
                        "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}", 
                        "provider_name": "Microsoft-Windows-Sysmon", 
                        "record_id": 45056, 
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
                "_type": "_doc"
            }
        ], 
        "max_score": 0.0, 
        "total": {
            "relation": "eq", 
            "value": 2
        }
    }, 
    "timed_out": false, 
    "took": 6
}
-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------
Test case 6 vmiexec.vbs
-----------------------------------------------------------------------------------
{
    "_shards": {
        "failed": 0, 
        "skipped": 0, 
        "successful": 94, 
        "total": 96
    }, 
    "hits": {
        "hits": [
            {
                "_id": "N7s4GXMB1uvUeW0ZAxtL", 
                "_index": "winlogbeat-7.7.0-2020.07.04", 
                "_score": 0.0, 
                "_source": {
                    "@timestamp": "2020-07-04T09:46:04.733Z", 
                    "@version": "1", 
                    "agent": {
                        "ephemeral_id": "be1a1a61-adaa-4020-9bd9-8ed7dc7e8f8b", 
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
                        "created": "2020-07-04T09:46:07.263Z", 
                        "kind": "event", 
                        "module": "sysmon", 
                        "provider": "Microsoft-Windows-Sysmon"
                    }, 
                    "file": {
                        "path": "C:\\Windows\\Temp\\wmi.dll"
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
                            "build": "7601.24525", 
                            "family": "windows", 
                            "kernel": "6.1.7601.24520 (win7sp1_ldr_escrow.190828-1732)", 
                            "name": "Windows Server 2008 R2 Datacenter", 
                            "platform": "windows", 
                            "version": "6.1"
                        }
                    }, 
                    "log": {
                        "level": "information"
                    }, 
                    "message": "File created:\nRuleName: DLL\nUtcTime: 2020-07-04 09:46:04.733\nProcessGuid: {F4BE2742-4FDC-5F00-0000-0010A65C5900}\nProcessId: 3848\nImage: C:\\Windows\\system32\\cmd.exe\nTargetFilename: C:\\Windows\\Temp\\wmi.dll\nCreationUtcTime: 2020-07-04 09:46:04.733", 
                    "process": {
                        "entity_id": "{F4BE2742-4FDC-5F00-0000-0010A65C5900}", 
                        "executable": "C:\\Windows\\system32\\cmd.exe", 
                        "name": "cmd.exe", 
                        "pid": 3848
                    }, 
                    "tags": [
                        "beats_input_codec_plain_applied"
                    ], 
                    "winlog": {
                        "api": "wineventlog", 
                        "channel": "Microsoft-Windows-Sysmon/Operational", 
                        "computer_name": "WINSRV.winsrv2008.local", 
                        "event_data": {
                            "CreationUtcTime": "2020-07-04 09:46:04.733", 
                            "RuleName": "DLL"
                        }, 
                        "event_id": 11, 
                        "opcode": "Info", 
                        "process": {
                            "pid": 2268, 
                            "thread": {
                                "id": 2892
                            }
                        }, 
                        "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}", 
                        "provider_name": "Microsoft-Windows-Sysmon", 
                        "record_id": 45053, 
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
                "_type": "_doc"
            }, 
            {
                "_id": "ars4GXMB1uvUeW0ZExt2", 
                "_index": "winlogbeat-7.7.0-2020.07.04", 
                "_score": 0.0, 
                "_source": {
                    "@timestamp": "2020-07-04T09:46:09.800Z", 
                    "@version": "1", 
                    "agent": {
                        "ephemeral_id": "be1a1a61-adaa-4020-9bd9-8ed7dc7e8f8b", 
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
                        "created": "2020-07-04T09:46:11.274Z", 
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
                            "build": "7601.24525", 
                            "family": "windows", 
                            "kernel": "6.1.7601.24520 (win7sp1_ldr_escrow.190828-1732)", 
                            "name": "Windows Server 2008 R2 Datacenter", 
                            "platform": "windows", 
                            "version": "6.1"
                        }
                    }, 
                    "log": {
                        "level": "information"
                    }, 
                    "message": "Process Create:\nRuleName: \nUtcTime: 2020-07-04 09:46:09.800\nProcessGuid: {F4BE2742-4FE1-5F00-0000-001005635900}\nProcessId: 4004\nImage: C:\\Windows\\System32\\cmd.exe\nFileVersion: 6.1.7601.17514 (win7sp1_rtm.101119-1850)\nDescription: Windows Command Processor\nProduct: Microsoft\u00ae Windows\u00ae Operating System\nCompany: Microsoft Corporation\nOriginalFileName: Cmd.Exe\nCommandLine: cmd.exe /c del C:\\windows\\temp\\wmi.dll /F > nul 2>&1\nCurrentDirectory: C:\\Windows\\system32\\\nUser: WINSRV2008\\Administrator\nLogonGuid: {F4BE2742-4FDC-5F00-0000-0020855A5900}\nLogonId: 0x595a85\nTerminalSessionId: 0\nIntegrityLevel: High\nHashes: MD5=5746BD7E255DD6A8AFA06F7C42C1BA41,SHA256=DB06C3534964E3FC79D2763144BA53742D7FA250CA336F4A0FE724B75AAFF386,IMPHASH=D0058544E4588B1B2290B7F4D830EB0A\nParentProcessGuid: {F4BE2742-26BE-5F00-0000-001065DF0200}\nParentProcessId: 2540\nParentImage: C:\\Windows\\System32\\wbem\\WmiPrvSE.exe\nParentCommandLine: C:\\Windows\\system32\\wbem\\wmiprvse.exe -secured -Embedding", 
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
                        "entity_id": "{F4BE2742-4FE1-5F00-0000-001005635900}", 
                        "executable": "C:\\Windows\\System32\\cmd.exe", 
                        "name": "cmd.exe", 
                        "parent": {
                            "args": [
                                "C:\\Windows\\system32\\wbem\\wmiprvse.exe", 
                                "-secured", 
                                "-Embedding"
                            ], 
                            "entity_id": "{F4BE2742-26BE-5F00-0000-001065DF0200}", 
                            "executable": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe", 
                            "name": "WmiPrvSE.exe", 
                            "pid": 2540
                        }, 
                        "pid": 4004, 
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
                            "LogonGuid": "{F4BE2742-4FDC-5F00-0000-0020855A5900}", 
                            "LogonId": "0x595a85", 
                            "OriginalFileName": "Cmd.Exe", 
                            "Product": "Microsoft\u00ae Windows\u00ae Operating System", 
                            "TerminalSessionId": "0"
                        }, 
                        "event_id": 1, 
                        "opcode": "Info", 
                        "process": {
                            "pid": 2268, 
                            "thread": {
                                "id": 2892
                            }
                        }, 
                        "provider_guid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}", 
                        "provider_name": "Microsoft-Windows-Sysmon", 
                        "record_id": 45056, 
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
                "_type": "_doc"
            }
        ], 
        "max_score": 0.0, 
        "total": {
            "relation": "eq", 
            "value": 2
        }
    }, 
    "timed_out": false, 
    "took": 5
}
-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------
Test case 11 Golden Ticket
-----------------------------------------------------------------------------------
{
    "_id": "L7s3GXMB1uvUeW0Z-xsP", 
    "_index": "winlogbeat-7.7.0-2020.07.04", 
    "_score": null, 
    "_source": {
        "@timestamp": "2020-07-04T09:46:04.609Z", 
        "@version": "1", 
        "agent": {
            "ephemeral_id": "be1a1a61-adaa-4020-9bd9-8ed7dc7e8f8b", 
            "hostname": "WINSRV", 
            "id": "b002425b-af48-4008-8d0a-9e3014604a59", 
            "type": "winlogbeat", 
            "version": "7.7.0"
        }, 
        "ecs": {
            "version": "1.5.0"
        }, 
        "event": {
            "action": "Kerberos Service Ticket Operations", 
            "code": 4769, 
            "created": "2020-07-04T09:46:04.811Z", 
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
                "build": "7601.24525", 
                "family": "windows", 
                "kernel": "6.1.7601.24520 (win7sp1_ldr_escrow.190828-1732)", 
                "name": "Windows Server 2008 R2 Datacenter", 
                "platform": "windows", 
                "version": "6.1"
            }
        }, 
        "log": {
            "level": "information"
        }, 
        "message": "A Kerberos service ticket was requested.\n\nAccount Information:\n\tAccount Name:\t\tAdministrator@WINSRV2008.LOCAL\n\tAccount Domain:\t\tWINSRV2008.LOCAL\n\tLogon GUID:\t\t{37AEECBF-B01A-9BF7-1075-93D6F6C70223}\n\nService Information:\n\tService Name:\t\tWINSRV$\n\tService ID:\t\tS-1-5-21-4220747943-3152432350-320651364-1001\n\nNetwork Information:\n\tClient Address:\t\t::ffff:192.168.255.113\n\tClient Port:\t\t49206\n\nAdditional Information:\n\tTicket Options:\t\t0x40810000\n\tTicket Encryption Type:\t0x12\n\tFailure Code:\t\t0x0\n\tTransited Services:\t-\n\nThis event is generated every time access is requested to a resource such as a computer or a Windows service.  The service name indicates the resource to which access was requested.\n\nThis event can be correlated with Windows logon events by comparing the Logon GUID fields in each event.  The logon event occurs on the machine that was accessed, which is often a different machine than the domain controller which issued the service ticket.\n\nTicket options, encryption types, and failure codes are defined in RFC 4120.", 
        "tags": [
            "beats_input_codec_plain_applied"
        ], 
        "winlog": {
            "api": "wineventlog", 
            "channel": "Security", 
            "computer_name": "WINSRV.winsrv2008.local", 
            "event_data": {
                "IpAddress": "::ffff:192.168.255.113", 
                "IpPort": "49206", 
                "LogonGuid": "{37AEECBF-B01A-9BF7-1075-93D6F6C70223}", 
                "ServiceName": "WINSRV$", 
                "ServiceSid": "S-1-5-21-4220747943-3152432350-320651364-1001", 
                "Status": "0x0", 
                "TargetDomainName": "WINSRV2008.LOCAL", 
                "TargetUserName": "Administrator@WINSRV2008.LOCAL", 
                "TicketEncryptionType": "0x12", 
                "TicketOptions": "0x40810000", 
                "TransmittedServices": "-"
            }, 
            "event_id": 4769, 
            "keywords": [
                "Audit Success"
            ], 
            "opcode": "Info", 
            "process": {
                "pid": 544, 
                "thread": {
                    "id": 1196
                }
            }, 
            "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}", 
            "provider_name": "Microsoft-Windows-Security-Auditing", 
            "record_id": 1178017, 
            "task": "Kerberos Service Ticket Operations"
        }
    }, 
    "_type": "_doc", 
    "sort": [
        1593855964609
    ]
}{
    "_id": "Qrs4GXMB1uvUeW0ZAxtP", 
    "_index": "winlogbeat-7.7.0-2020.07.04", 
    "_score": null, 
    "_source": {
        "@timestamp": "2020-07-04T09:46:04.655Z", 
        "@version": "1", 
        "agent": {
            "ephemeral_id": "be1a1a61-adaa-4020-9bd9-8ed7dc7e8f8b", 
            "hostname": "WINSRV", 
            "id": "b002425b-af48-4008-8d0a-9e3014604a59", 
            "type": "winlogbeat", 
            "version": "7.7.0"
        }, 
        "ecs": {
            "version": "1.5.0"
        }, 
        "event": {
            "action": "Kerberos Service Ticket Operations", 
            "code": 4769, 
            "created": "2020-07-04T09:46:06.877Z", 
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
                "build": "7601.24525", 
                "family": "windows", 
                "kernel": "6.1.7601.24520 (win7sp1_ldr_escrow.190828-1732)", 
                "name": "Windows Server 2008 R2 Datacenter", 
                "platform": "windows", 
                "version": "6.1"
            }
        }, 
        "log": {
            "level": "information"
        }, 
        "message": "A Kerberos service ticket was requested.\n\nAccount Information:\n\tAccount Name:\t\tAdministrator@WINSRV2008.LOCAL\n\tAccount Domain:\t\tWINSRV2008.LOCAL\n\tLogon GUID:\t\t{37AEECBF-B01A-9BF7-1075-93D6F6C70223}\n\nService Information:\n\tService Name:\t\tWINSRV$\n\tService ID:\t\tS-1-5-21-4220747943-3152432350-320651364-1001\n\nNetwork Information:\n\tClient Address:\t\t::ffff:192.168.255.113\n\tClient Port:\t\t49211\n\nAdditional Information:\n\tTicket Options:\t\t0x40810000\n\tTicket Encryption Type:\t0x12\n\tFailure Code:\t\t0x0\n\tTransited Services:\t-\n\nThis event is generated every time access is requested to a resource such as a computer or a Windows service.  The service name indicates the resource to which access was requested.\n\nThis event can be correlated with Windows logon events by comparing the Logon GUID fields in each event.  The logon event occurs on the machine that was accessed, which is often a different machine than the domain controller which issued the service ticket.\n\nTicket options, encryption types, and failure codes are defined in RFC 4120.", 
        "tags": [
            "beats_input_codec_plain_applied"
        ], 
        "winlog": {
            "api": "wineventlog", 
            "channel": "Security", 
            "computer_name": "WINSRV.winsrv2008.local", 
            "event_data": {
                "IpAddress": "::ffff:192.168.255.113", 
                "IpPort": "49211", 
                "LogonGuid": "{37AEECBF-B01A-9BF7-1075-93D6F6C70223}", 
                "ServiceName": "WINSRV$", 
                "ServiceSid": "S-1-5-21-4220747943-3152432350-320651364-1001", 
                "Status": "0x0", 
                "TargetDomainName": "WINSRV2008.LOCAL", 
                "TargetUserName": "Administrator@WINSRV2008.LOCAL", 
                "TicketEncryptionType": "0x12", 
                "TicketOptions": "0x40810000", 
                "TransmittedServices": "-"
            }, 
            "event_id": 4769, 
            "keywords": [
                "Audit Success"
            ], 
            "opcode": "Info", 
            "process": {
                "pid": 544, 
                "thread": {
                    "id": 1196
                }
            }, 
            "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}", 
            "provider_name": "Microsoft-Windows-Security-Auditing", 
            "record_id": 1178031, 
            "task": "Kerberos Service Ticket Operations"
        }
    }, 
    "_type": "_doc", 
    "sort": [
        1593855964655
    ]
}
-----------------------------------------------------------------------------------

