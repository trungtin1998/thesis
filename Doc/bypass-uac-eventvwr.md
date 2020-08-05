# Bypass UAC bằng cách sử dụng eventvwr.exe
Ngày: 05/08/2020

## Tổng quan
### Hive, key, value trong Registry
* Registry hive trong Windows Registry là tên được đặt cho một phần chính của registry có chứa registry key, registry subkey (khoá con registry) và registry value (giá trị registry).
* Tất cả các key được coi là hive bắt đầu bằng "HKEY" và nằm ở thư mục root hoặc trên cùng của hệ thống phân cấp trong registry, đó là lý do tại sao đôi khi chúng còn được gọi là key gốc hoặc các hive hệ thống cốt lõi.
* Dưới đây là danh sách các registry hive phổ biến trong Windows:
  * HKEY_CLASSES_ROOT (HKCR)
  * HKEY_CURRENT_USER (HKCU)
  * HKEY_LOCAL_MACHINE
  * HKEY_USERS
  * HKEY_CURRENT_CONFIG [4]
### Bypass UAC
* User Account Control (UAC) là 1 tính năng của Windows giúp ngăn chặn các sự thay đổi đến hệ thống mà không được cho phép.
* Bypass UAC là các kỹ thuật nhằm mục đích thực thi hoặc thực hiện các thay đổi với đặc quyền hệ thống mà không có bất kỳ cảnh báo nào.
* Chỉ có thể tiến hành bypass UAC đối với các tài khoản thuộc administrator group và kích hoạt UAC (enable UAC)
### Powershell Empire
* Là một công cụ thực thi hoàn toàn trên powershell và công dụng phần nhiều nằm ở các tính năng mà nó có thể khai thác ở máy nạn nhân sau xảy ra tấn công (post-exploitation), được xây dựng trên các giao tiếp bảo mật bằng mật mã và kiến trúc linh hoạt
* Đây là một công cụ mã nguồn mở, được sự đóng góp của nhiều người
* Sau khi thực hiện exploit thành công, các module có thể được triển khai một cách nhanh chóng, từ việc có thể sử dụng keylogger cho đến mimikatz và tất cả được gói gọn trong một framework.
* Powershell Empire hỗ trợ nhiều module để có thể thực hiện các tấn công Bypass UAC.
* bypassuac_eventvwr là một module của Powershell Empire. Nguyên lý hoạt động dựa trên việc khai thác lúc khởi chạy chương trình eventvwr.exe. 
Khi mở eventvwr.exe, tiến trình này sẽ kiểm tra giá trị registry HKCU\Software\Classes\mscfile\shell\open\command để tìm vị trí của chương trình mmc.exe, tiến trình được sử dụng để mở eventvwr.msc saved console file.
Nếu đường dẫn tới mmc.exe bị thay bởi một chương trình hoặc một đoạn script khác (thay đổi giá trị của registry HKCU\Software\Classes\mscfile\shell\open\command), nó sẽ được thực thi với quyền hệ thống mà không bị thông báo nhắc nhở cần nâng cao đặc quyền UAC hiển thị tại giao diện người dùng. [2]

## Thực hiện tấn công
### Cách hoạt động của Bypass UAC bằng cách khai thác lỗ hỏng của eventvwr.exe
* HKCR hive bao gồm sự kết hợp của HKLM:\Software\Classes and HKCU:\Software\Classes. Bởi vì sự sáp nhập bởi những hive này nên ta có thể hijack giá trị cho HKCR:\ bằng cách tạo chúng tại HKCU:\Software\Classes.
* Một user thường có quyền ghi vào key tại HKCU. Nếu một tiến trình với đặc quyền hệ thống tương tác với key mà ta thao tác, ta có khả năng can thiệp vào các hành động của các tiến trình hệ thống đang thực hiện.
* eventvwr.exe là một chương trình tự động nâng cao đặc quyền (auto-elevates) bởi vì file manifest của chương trình này thể hiện: [3]
![eventvwr.exe auto-elevates](../Images/eventvwr-auto-elevates.png)




## Tài liệu tham khảo
* [[1] "Empire"](https://attack.mitre.org/software/S0363/)
* [[2] Matt Nelson, Matt Graeber, "UAC bypass"](https://lolbas-project.github.io/lolbas/Binaries/Eventvwr/)
* [[3] enigma0x3, "FILELESS UAC BYPASS USING EVENTVWR.EXE AND REGISTRY HIJACKING"](https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/)
* [[4] "Registry Hive là gì?"](https://quantrimang.com/registry-hive-la-gi-165892#:~:text=Registry%20hive%20l%C3%A0%20m%E1%BB%99t%20th%C6%B0,v%C3%A0%20registry%20key%20c%C5%A9ng%20v%E1%BA%ADy.&text=S%E1%BB%B1%20kh%C3%A1c%20bi%E1%BB%87t%20duy%20nh%E1%BA%A5t,v%C3%A0%20nh%E1%BB%AFng%20registry%20key%20kh%C3%A1c.)
