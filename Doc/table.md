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
| Administrator | 192.168.255.100 | Windows Server 2008 | Domain Administrator | Sử dụng -s để nâng cao đặc quyền | 1 | 1 |
| Administrator | 192.168.255.129 | Windows 7 | Local Administrator |  | 1 | 1 |
| Administrator | 192.168.255.129 | Windows 7 | Domain Administrator |  | 1 | 1 |
| Administrator | 192.168.255.129 | Windows 7 | Domain Administrator | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |

* Số lần thực hiện: 16
* Tỉ lệ thành công: 100%

## Test case 2: Powershell Empire
* Ở phần kiểm tra này, với các tài khoản đăng nhập trên máy Windows 7 có địa chỉ IP 192.168.255.129, các tấn công sẽ chỉ được phát hiện log của máy client cũng được gửi về log server.
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|
| test | 192.168.255.100 | Windows Server 2008 | Standard User | 3 | 3 |
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | 3 | 3 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Domain Administrator | 3 | 3 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Local Administrator | 3 | 3 |

* Số lần thực hiện: 12
* Tỉ lệ thành công: 100%
