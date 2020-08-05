# Bypass UAC bằng cách sử dụng eventvwr.exe
Ngày: 05/08/2020

## Tổng quan

### Bypass UAC
* User Account Control (UAC) là 1 tính năng của Windows giúp ngăn chặn các sự thay đổi đến hệ thống mà không được cho phép.
* Bypass UAC là các kỹ thuật nhằm mục đích thực thi hoặc thực hiện các thay đổi với đặc quyền hệ thống mà không có bất kỳ cảnh báo nào.
* Chỉ có thể tiến hành bypass UAC đối với các tài khoản thuộc administrator group và kích hoạt UAC (enable UAC)

### Powershell Empire
* Là 1 công cụ thực thi hoàn toàn trên powershell và công dụng phần nhiều nằm ở các tính năng mà nó có thể khai thác ở máy nạn nhân sau xảy ra tấn công (post-exploitation), được xây dựng trên các giao tiếp bảo mật bằng mật mã và kiến trúc linh hoạt
* Đây là 1 công cụ mã nguồn mở, được sự đóng góp của nhiều người
* Sau khi thực hiện exploit thành công, các modules có thể được triển khai 1 cách nhanh chóng, từ việc có thể sử dụng keylogger cho đến mimikatz và tất cả được gói gọn trong một framework.
* Powershell Empire hỗ trợ nhiều module để có thể thực hiện các tấn công Bypass UAC.
* bypassuac_eventvwr là một module của Powershell Empire. Nguyên lý hoạt động dựa trên việc khai thác lúc khởi chạy chương trình eventvwr.exe. 
Khi mở eventvwr.exe, tiến trình này sẽ kiểm tra giá trị registry HKCU\Software\Classes\mscfile\shell\open\command để tìm vị trí của chương trình mmc.exe, tiến trình được sử dụng để mở eventvwr.msc saved console file.
Nếu đường dẫn tới mmc.exe bị thay bởi một chương trình hoặc một đoạn script khác được thay vào giá trị của registry này, nó sẽ được thực thi với quyền hệ thống mà không bị thông báo nhắc nhở cần nâng cao đặc quyền UAC hiển thị tại giao diện người dùng..


### 


## Tài liệu tham khảo
[[1] "Empire"](https://attack.mitre.org/software/S0363/)
[[2] Matt Nelson, Matt Graeber, "UAC bypass"](https://lolbas-project.github.io/lolbas/Binaries/Eventvwr/)
[[3] enigma0x3, "FILELESS UAC BYPASS USING EVENTVWR.EXE AND REGISTRY HIJACKING"](https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/)
