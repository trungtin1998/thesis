# Bảng kết quả thực nghiệm

## Test case 1: PsExec
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Ghi chú | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|:-------:|
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group |  | 3 | 3 |
| sv | 192.168.255.129 | Windows 7 | Thành viên của Administrator group | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
| sv | 192.168.255.123 | Windows 7 | Thành viên của Administrator group | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
| administrator | 192.168.255.100 | Windows Server 2008 | Administrator | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
| administrator | 192.168.255.129 | Windows 7 | Administrator |  | 3 | 3 |
| administrator | 192.168.255.129 | Windows 7 | Administrator | Sử dụng -s để nâng cao đặc quyền | 3 | 3 |
* Ghi chú: Máy có địa chỉ IP 192.168.255.100 là máy Server. Máy có địa chỉ IP 192.168.255.129 là thành viên của domain. Máy Windows 7 có địa chỉ IP 192.168.255.123 không gia vào domain.
* Số lần thực hiện: 21
* Tỉ lệ thành công: 100%
