# Bypass UAC

## UAC là gì?
* User Account Control (UAC) là 1 tính năng của Windows giúp ngăn chặn các sự thay đổi đến hệ thống mà không được cho phép. 
* UAC hiện diện từ Windows Vista và Windows Server 2008 trở đi với mục đích giúp cho người dùng có thể nhận biết rằng có sự thay đổi liên quan đến hệ thống được kích hoạt
* Chúng hoạt động bằng cách hiển thị cửa sổ popup, yêu cầu người dùng tương tác đưa ra lựa chọn giữa việc chấp nhận hay không, được liệt kê bằng cách ghi rõ tên chương trình và nhà phát hành chương trình đang cố gắng thực hiện các hành động thay đổi liên quan đến hệ thống
* UAC là 1 biện pháp bảo mật có thể ngăn chặn các phần mềm độc hại, các người dùng không mong muốn hoặc các ứng dụng muốn thay đổi các cấu hình liên quan đến hệ thống

## Bypass UAC là gì?
* Bypass UAC là các kỹ thuật nhằm mục đích thực thi hoặc thực hiện các thay đổi với đặc quyền hệ thống mà không có bất kỳ cảnh báo nào
* Chỉ có thể tiến hành bypass UAC đối với các tài khoản thuộc administrator group và cho phép UAC (enable UAC)
* Có nhiều cách để có thể tiến hành bypass UAC như Thông qua GUI, DLL hijacking, registry manipulation, ...

## How does Bypass UAC work?
* Khi 1 máy tính bị mắc phải 1 phần mềm độc hại do metasploit tạo ra, ta có thể sử dụng module exploit/windows/local/bypassuac được cài đặt sẵn trong metasploit để tiến hành bypass UAC
* Cách thức bypass UAC hoạt động (Giả sử phần mềm độc hại có tên là PlugX):
![Dridex Infection Flow](/)
  * Bước 1: PlugX tạo 1 DLL (giả sử trỏ đến UAC.TMP)
  * Bước 2: PlugX chèn code vào chương trình đang chạy explorer.exe, để chương trình explorer.exe di chuyển UAC.TMP vào C:\Windows\System32\sysprep\cryptbase.dll
  * Bước 3: C:\Windows\System32\sysprep\sysprep.exe được thực thi và sysprep.exe tải C:\Windows\System32\sysprep\cryptbase.dll với quyền admin
  * Bước 4: C:\Windows\System32\sysprep\cryptbase.dll thực thi PlugX với quyền admin [1]
* Với phương pháp này, việc nâng cao đặc quyền sẽ không hề hiển thị các cảnh báo UAC

## Tài liệu tham khảo
[[1] A New UAC Bypass Method that Dridex Uses](https://blogs.jpcert.or.jp/en/2015/02/a-new-uac-bypass-method-that-dridex-uses.html)
