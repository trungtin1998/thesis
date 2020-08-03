# Bảng kết quả thực nghiệm
* Ghi chú: 
  * Máy có địa chỉ IP 192.168.255.**100** là máy Server. Máy có địa chỉ IP 192.168.255.**129** là thành viên của domain. Máy Windows 7 có địa chỉ IP 192.168.255.**123** không tham gia vào domain.
  * Tài khoản **sv** là thành viên của administrator group, thành viên của domain WINSRV2008. Tài khoản **test** là standard user trong domain.

## Test case 1: PsExec
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Ghi chú | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|:-------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group |  | 3 | 3 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
| sv | 192.168.255.123 | Windows 7 | Thành viên của Administrator group | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator |  | 3 | 3 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
* Số lần thực hiện: 18
* Tỉ lệ thành công: 100%

## Test case 2: Powershell Empire
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 8 | 8 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 4 | 4 |
* Ở phần kiểm tra này, với các tài khoản đăng nhập trên máy Windows 7 có địa chỉ IP 192.168.255.129, các tấn công **chỉ được phát hiện** nếu log của máy client cũng được gửi về log server.
* Số lần thực hiện: 12
* Tỉ lệ thành công: 100%

## Test case 3: Invoke-Command
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 7 | 7 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 5 | 5 |
* Số lần thực hiện: 12
* Tỉ lệ thành coong: 100

## Test case 4: WinRS
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 10 | 10 |
* Số lần thực hiện: 15
* Tỉ lệ thành công: 100%

## Test case 5: WMIC
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 10 | 8 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 10 | 8 |
* Số lần thực hiện: 20
* Tỉ lệ thành công: 80%
* Với các lần thực hiện thu thập thông tin thông qua lệnh: `wmic bios get serialnumber` hoặc `wmic process get name, processid` thì không bắt được. Tuy nhiên nếu sử dụng wmic để thực thi lệnh nào đó trên command line, tức thực hiện các tấn công Remote Command Execution

### Với các tấn công WMIC có thực hiện các thử nghiệm sau:
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Câu lệnh thực thi | Loại tấn công | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | `wmic bios list /format:list` | Thu thập thông tin bios name, serialnumber | 1 | 0 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | `wmic computersystem list /format:list` | Thu thập thông tin về hostname, domain, username | 1 | 0 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | `wmic process get name,processid` | Thông tin về các tiến trình trong hệ thống | 1 | 0 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | `wmic useraccount list /format:list` | Thông tin về toàn bộ các tài khoản có trong hệ thống: username, SID | 2 | 0 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | `wmic bios list /format:list` | Thu thập thông tin bios name, serialnumber | 1 | 0 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | `wmic computersystem list /format:list` | Thu thập thông tin về hostname, domain, username | 1 | 0 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | `wmic process get name, processid` | Thông tin về các tiến trình trong hệ thống | 1 | 0 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | `wmic useraccount list /format:list` | Thông tin về toàn bộ các tài khoản có trong hệ thống: username, SID | 2 | 0 |
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | `wmic bios list /format:list` | Thu thập thông tin bios name, serialnumber | 1 | 0 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | `wmic bios list /format:list` | Thu thập thông tin bios name, serialnumber | 1 | 0 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | `wmic process call create "net user [username] [password] /add"` | Thêm một tài khoản vào hệ thống | 2 | 2 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | `wmic process call create "net user hacker /del"` | Xóa tài khoản khỏi hệ thống | 1 | 1 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | `wmic process call create "F:\HackingFolder\wce64.exe"` | Thực thi file trên hệ thống nạn nhân | 2 | 2 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | `wmic process call create "net user [username] [password] /add"` | Thêm một tài khoản vào hệ thống | 2 | 2 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | `wmic process call create "at [timestamp] [filename]"` | Chạy lập lịch file mã độc | 1 | 1 |
* Số lần thực hiện: 20
* Tỉ lệ thành c: 8/20 = 40%

## Test case 6: wmiexec.vbs
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 10 | 10 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 5 | 5 |
* Số lần thực hiện: 15
* Tỉ lệ thành công: 100%

## Test case 7: PwDump7
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 2 | 2 |
| SYSTEM | 192.168.255.100 | Windows Server 2008 | System Account | 3 | 3 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 3 | 3 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 2 | 2 |
* Số lần thực hiện: 15
* Tỉ lệ thành công: 100%

## Test case 8: Quarks PwDump
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 2 | 2 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 3 | 3 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 2 | 2 |
* Số lần thực hiện: 12
* Tỉ lệ thành công: 100%

## Test case 9: WCE Password and Hash Dump
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 5 | 5 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 5 | 5 |
* Số lần thực hiện: 20
* Tỉ lệ thành công: 100%

## Test case 10: WCE Remote Login
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 6 | 6 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 2 | 2 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 6 | 6 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 2 | 2 |
* Số lần thực hiện: 16
* Tỉ lệ thành công: 100%

## Test case 11: Golden Ticket
| Username | Địa chỉ IP | Hệ điều hành | Sid | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | 500 | 3 | 3 |
| FakeAdmin | 192.168.255.129 | Windows 7 | 500 | 5 | 5 |
| hacker | 192.168.255.129 | Windows 7 | 500 | 3 | 3 |
| sv | 192.168.255.129 | Windows 7 | 500 | 3 | 3 |
| Administrator | 192.168.255.129 | Windows 7 | 500 | 2 | 2 |
| FakeAdmin | 192.168.255.123 | Windows 7 | 500 | 2 | 2 |
* Số lần thực hiện: 20
* Tỉ lệ thành công: 100%

## Test case 12: AT Command
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 4 | 4 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 2 | 2 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 4 | 4 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 2 | 2 |
* Số lần thực hiện: 12
* Tỉ lệ thành công: 100%

## Test case 13: RDP
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| test | 192.168.255.129 | Windows 7 | standard user | 2 | 2 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 10 | 10 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 2 | 2 |
* Số lần thực hiện: 14
* Tỉ lệ thành công: 100%
* Ở phần cảnh báo cho tấn công này, khi hệ điều hành yêu cầu restart để tiến hành cập nhật cũng sẽ sinh ra Event ID 21 với `winlog.task` là `Automatic Updates`. Do đó cần thêm điều kiện này để tránh xảy ra tình trạng cảnh báo giả.
* Nếu muốn cho standard user được phép RDP thì thêm vào user này vào **Remote Desktop Services** và  **Allow log on through Remote Desktop Services**

## Test case 14: Mimikatz

## Test case 15: Bypass UAC
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 14 | 14 |
| trungtin | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 4 | 4 |
* Số lần thực hiện: 18
* Tỉ lệ thành công: 100%

## Test case 16: ntdsutil
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 8 | 8 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 3 | 3 |
| SYSTEM | 192.168.255.100 | Windows Server 2008 | System Account | 5 | 5 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 2 | 2 |
* Kết hợp PsExec và ntdsutil từ máy windows 7 để tạo shadow copy.
* Khi start ntdsutil tại nhiều vị trí khác nhau thì luôn gọi đến C:\Windows\System32. Copy file đó sang 1 vị trí khác thực thi thì không được
* Số lần thực hiện: 18
* Tỉ lệ thành công: 100%

## Test case 17: vssadmin
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 8 | 8 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 4 | 4 |
| SYSTEM | 192.168.255.100 | Windows Server 2008 | System Account | 4 | 4 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 2 | 2 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 2 | 2 |
* Số lần thực hiện: 20
* Tỉ lệ thành công: 100%

## Test case 18: net user
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 5 | 5 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 5 | 5 |
* Số lần thực hiện: 20
* Tỉ lệ thành công: 100%

## Test case 19: csvde

## Test case 20: ldifde

## Test case 21: timestomp
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 8 | 8 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 3 | 3 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 6 | 6 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 3 | 3 |
* Số lần thực hiện: 20
* Tỉ lệ thành công: 100%
* Sự tạo ra file mới (cụ thể là mở file word trong test case 2 Powershell Empire hoặc test case 16 kkhi tạo shadow copy, mục đích file ntds.dit sang C:\temp) cũng sẽ bị cảnh báo bởi test case 21.

## Test case 22: wevtutil
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 6 | 6 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 2 | 2 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 2 | 2 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 2 | 2 |
* Số lần thực hiện: 12
* Tỉ lệ thành công: 100%
