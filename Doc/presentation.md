# Nội dung thuyết trình

## Giới thiệu đề tài
* Để biết được mục đích của đề tài này, chúng ta hãy cùng tìm hiểu về khái niệm của tấn công máy tính.
* Tấn công máy tính thường được người dùng biết đến ở dạng một chương trình độc hại, gây ra lỗi nghiêm trọng cho một hoặc nhiều máy tính cùng lúc nhằm phục vụ nhiều mục đích khác nhau của kẻ tấn công như: Đánh cắp thông tin, chiếm quyền điều khiển từ xa, phá hoại dữ liệu,… 
* Như vậy để đối phó với tấn công hay tìm ra được lỗ hổng nào đang có trên máy tính, thông thường quản trị viên sẽ tìm đến mục chứa log của máy bị tấn công và đọc thông tin log xem chuyện gì đang xảy ra. Vấn đề ở đây là làm sao để kiểm soát một số lượng máy nhất định bằng việc quản lý log tập trung (không cần phải đến từng máy xem log)?
* Đề tài này ra đời nhằm giải quyết cho vấn đề đó, nhóm đã thực hiện một mô hình hệ thống có thể quản lý và truy vấn log tập trung từ nhiều nguồn khác nhau để phát hiện tấn công mà không cần phải đến từng máy để xem log dựa trên bộ công cụ ELK Stack.

### Tóm tắt đề tài
* Bước 1: Thử nghiệm các tấn công máy tính trong môi trường Windows
* Bước 2: 
  * Đưa ra bằng chứng thực thi của từng tấn công dựa vào Event Log
  * Áp dụng kết quả vào để thực hiện truy vấn trên ELK
* Bước 3: Viết chương trình tự động gửi cảnh báo về email cho quản trị viên khi có tấn công
* Bước 4: Đánh giá về mô hình thực nghiệm và đề xuất thêm hướng phát triển cho hệ thống

## Ví dụ tấn công: PsExec
* Thể loại: Command Execution
* Tổng quan: Công cụ này nằm trong bộ công cụ quản trị hệ thống Sysinternals, được tạo bởi Mark Russinovich, cho phép ta có thể thực thi các tác vụ từ xa. 
### Tóm tắt cách hoạt động của PsExec
* Upload PSEXESVC.exe tới thư mục chia sẻ $Admin.
* Tạo từ xa một dịch vụ để có thể chạy PSEXESVC.exe.
* Khởi động dịch vụ này từ xa. [1]

### Chi tiết cách hoạt động của PsExec
* PSEXECSVC service thực thi file được chỉ định trên remote machine (chẳng hạn cmd.exe) và redirect input/output qua lại giữa các hosts thông qua các named pipe. Công cụ PsExec tại nguồn sẽ viết các lệnh cần thực thi vào \\client\pipe\PSEXESVC-stdin và đọc kết quả gửi về từ remote machine thông qua \\client\pipe\PSEXECSVC-stdout, \\client\pipe\PSEXECSVC-stderr. Ngược lại, remote machine (tại máy đích) sẽ chuyển output vào \\client\pipe\PSEXECSVC-stdout hoặc \\client\pipe\PSEXECSVC-stderr và đọc các lệnh cần thực thi từ \\client\pipe\PSEXESVC-stdin.
* Các bước thực hiện như sau:
  * Bước 1: Mở một phiên SMB thông qua credential được cung cấp để tiến hành xác thực.
  * Bước 2: Truy cập vào thư mục chia sẻ $ADMIN (alias là C:\Windows) thông qua giao thức SMB và tiến hành upload file PSEXESVC.exe
  * Bước 3: Mở một phiên xử lý tới \\client\pipe\svcctl để có thể giao tiếp với Service Control Manager, cho chúng ta khả năng tạo, start hoặc stop các service từ xa.
  * Bước 4: Gọi tới hàm CreateService, sử dụng file được upload gần đây (PSEXESVC) như một service binary.
  * Bước 5: Gọi tới hàm StartService để khởi động PSEXESVC từ xa.
