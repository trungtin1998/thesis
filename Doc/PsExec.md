# Test case 1: PsExec
Date: 27/07/2020</br>

## Tổng quan về PsExec
* PsExec nằm trong bộ công cụ quản trị hệ thống Sysinternals, được tạo bởi Mark Russinovich, cho phép ta có thể thực thi các tác vụ từ xa.

## Tóm tắt cách hoạt động của PsExec
* Upload PSEXESVC.exe tới thư mục chia sẻ $Admin.
* Tạo từ xa một dịch vụ để có thể chạy PSEXESVC.exe.
* Khởi động dịch vụ này từ xa. [1]

## Chi tiết cách hoạt động của PsExec
* PSEXECSVC service thực thi file được chỉ định trên remote machine (chẳng hạn cmd.exe) và redirect input/output qua lại giữa các hosts thông qua các named pipe. Công cụ PsExec tại nguồn sẽ viết các lệnh cần thực thi vào \\client\pipe\PSEXESVC-stdin và đọc kết quả gửi về từ remote machine thông qua \\client\pipe\PSEXECSVC-stdout, \\client\pipe\PSEXECSVC-stderr. Ngược lại, remote machine (tại máy đích) sẽ chuyển output vào \\client\pipe\PSEXECSVC-stdout hoặc \\client\pipe\PSEXECSVC-stderr và đọc các lệnh cần thực thi từ \\client\pipe\PSEXESVC-stdin.
* Các bước thực hiện như sau:
  * Bước 1: Mở một phiên SMB thông qua credential được cung cấp để tiến hành xác thực.
  * Bước 2: Truy cập vào thư mục chia sẻ $ADMIN (alias là C:\Windows) thông qua giao thức SMB và tiến hành upload file PSEXESVC.exe
  * Bước 3: Mở một phiên xử lý tới \\client\pipe\svcctl để có thể giao tiếp với Service Control Manager, cho chúng ta khả năng tạo, start hoặc stop các service từ xa.
  * Bước 4: Gọi tới hàm CreateService, sử dụng file được upload gần đây (PSEXESVC) như một service binary.
  * Bước 5: Gọi tới hàm StartService để khởi động PSEXESVC từ xa.

## Module SMB/PsExec của Metasploit
* Chỉ có thể thực hiện với tài khoản Administrator trên domain, các tài khoản thuộc administrator group cũng không thể thực hiện.
* Ta có thể hiệu chỉnh về tên thư mục chia sẻ (mặc định là $Admin), có thể thay đổi cả service name (mặc định là PSEXESVC).
* Đăng nhập thẳng vào tài khoản NT Authority.
* Không thể thực hiện tấn công với đường mạng khác.
* **Không thể phát hiện** có tấn công PsExec trên máy victim nếu bắt bằng **Event ID 7045** có tiến trình **PSEXESVC** thực thi.
* Cách để phát hiện thủ công là tại máy victim 1 (máy client), dò tìm sự thực thi của **powershell** với tham số **-nop -w hidden -noni -c**

## Tài liệu tham khảo
[1] Daniel Muñoz, ["Lateral movement: A deep look into PsExec"](https://www.contextis.com/us/blog/lateral-movement-a-deep-look-into-psexec)</br>
