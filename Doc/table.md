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
| test | 192.168.255.100 | Windows Server 2008 | Standard User | 3 | 3 |
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 4 | 4 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 3 | 3 |
* Ở phần kiểm tra này, với các tài khoản đăng nhập trên máy Windows 7 có địa chỉ IP 192.168.255.129, các tấn công **chỉ được phát hiện** nếu log của máy client cũng được gửi về log server.
* Số lần thực hiện: 10
* Tỉ lệ thành công: 100%

## Test case 3: Invoke-Command
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 5 | 5 |
* Số lần thực hiện: 10
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
* Với các lần thực hiện thu thập thông tin thông qua lệnh: `wmic bios get serial` hoặc `wmic process get name,processid` thì không bắt được. Tuy nhiên nếu sử dụng wmic để thực thi lệnh nào đó trên command line, tức thực hiện các tấn công Remote Command Execution

## Test case 6: wmiexec.vbs
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.129 | Windows 7 | Administrator | 5 | 5 |
* Số lần thực hiện: 10
* Tỉ lệ thành công: 100%

## Test case 7: PwDump7
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 5 | 5 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | 2 | 2 |
| NT Authority | 192.168.255.100 | Windows Server 2008 | System Account | 3 | 3 |
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
