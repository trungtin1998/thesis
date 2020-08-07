# Thesis: Phát hiện các tấn công máy tính và sự di chuyển giữa các node bằng hệ thống ELK Stack
Author: Phạm Trung Tín - Trần Vĩ Hùng.</br>
Date: 07/08/2020.</br>
Description: Capturing the Windows's threats using ELK Stack and Python Script.

## Luận văn sẽ khảo sát 24 threats sau:
* Test case 1 PsExec
* Test case 2 Powershell Empire
* Test case 3 Invoke-Command cmdlet
* Test case 4 WinRS
* Test case 5 WMIC
* Test case 6 vmiexec.vbs
* Test case 7 PWDump7
* Test case 8 Quarks PwDump
* Test case 9 WCE - Password and Hash Dump
* Test case 10 WCE Remote Login
* Test case 11 Golden Ticket
* Test case 12 AT Command
* Test case 13 RDP
* Test case 14 Mimikatz
* Test case 15 Bypass UAC
* Test case 16 ntdsutil
* Test case 17 vssadmin
* Test case 18 net user
* Test case 19 csvde
* Test case 20 ldifde
* Test case 21 timestomp
* Test case 22 wevtutil
* Test case 23 Bypass UAC khai thác eventvwr.exe
* Test case 24 Disable Audit Policy
## Mô tả hệ thống
* Các máy trong hệ thống bao gồm: Máy attacker, các máy Windows Server,
log server, Alert System và quản trị viên.
  * Máy attacker sẽ tấn công vào các máy sử dụng hệ điều
hành Windows Server bằng cách sử dụng các công cụ, phương pháp đã nêu ở trên.
  * Các máy Windows Server đóng vai trò là victim. Các máy này sẽ bật Audit Policy và cài đặt Sysmon để thu thập được chi tiết về các hoạt động trong hệ thống hơn. Ngoài ra chúng sẽ được cài đặt Winlogbeat, có vai trò đẩy log từ các máy Windows Server về Log Server.
  * Toàn bộ log từ các máy victim này sẽ được đẩy về Log Server - nơi lưu trữ log tập trung. Chúng cũng sẽ thực hiện nhiệm vụ trả về kết quả các câu truy vấn DSL từ Alert System gửi lên. Log server cài đặt ELK, được dùng đánh chỉ mục sau đó đưa vào lưu trữ. Ngoài ra Elasticsearch còn cung cấp Query DSL, bộ ngôn ngữ cung cấp khả năng filter log tuyệt vời.
  * Alert System là hệ thống giám sát, gửi liên tục các câu truy vấn DSL tới Log Server một phút một lần bằng cách sử dụng crontab. Kết quả trả về từ Log Server sẽ được phân tích, xử lý để đánh giá rằng có các tấn công máy tính đến hệ thống Windows Server hay không. Nếu có gửi cảnh báo thời gian thực đến mail của quản trị viên
![Mô tả thực nghiệm](./Images/mo-ta-thuc-nghiem.png)
