# PsExec
Date: 27/07/2020</br>

## PsExec Overview
* PsExec nằm trong bộ công cụ quản trị hệ thống Sysinternals, được tạo bởi Mark Russinovich, cho phép ta có thể thực thi các tác vụ từ xa.

## How does PsExec work?
* Upload PSEXESVC.exe tới thư mục chia sẻ $Admin.
* Tạo từ xa một dịch vụ để có thể chạy PSEXESVC.exe.
* Khởi động dịch vụ này từ xa. [1]

## Module SMB/PsExec của Metasploit
* Chỉ có thể thực hiện với tài khoản Administrator trên domain, các tài khoản thuộc administrator group cũng không thể thực hiện.
* Ta có thể hiệu chỉnh về tên thư mục chia sẻ (mặc định là $Admin), có thể thay đổi cả service name (mặc định là PSEXESVC).
* Đăng nhập thẳng vào tài khoản NT Authority.
* Không thể thực hiện tấn công với đường mạng khác.
* **Không thể phát hiện** có tấn công PsExec trên máy victim nếu bắt bằng **Event ID 7045** có tiến trình **PSEXESVC** thực thi.
* Cách để phát hiện thủ công là tại máy victim 1 (máy client), dò tìm sự thực thi của **powershell** với tham số **-nop -w hidden -noni -c**

## Tài liệu tham khảo
[1] Daniel Muñoz, ["Lateral movement: A deep look into PsExec"](https://www.contextis.com/us/blog/lateral-movement-a-deep-look-into-psexec), Accessed 27/07/2020
