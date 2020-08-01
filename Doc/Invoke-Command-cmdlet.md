# Invoke-Command cmdlet

## Tổng quan
* Windows Powershell Remoting sử dụng giao thức WS-Management cho phép thực hiện bất kì lệnh nào của Windows Powershell tại một hoặc nhiều máy. Ngoài ra còn có thể thiết lập các kết nối được duy trì (persistent connections khi xử dụng `New-PSSession cmdlet`), khởi tạo các phiên tương tác (`Enter-PSSession`) hoặc chạy các lệnh từ xa.
  * Chú thích: Giao thức WS-Management được phát triển bởi một nhóm các nhà sản xuất phần cứng và phần mềm như một tiêu chuẩn chung để quản lý việc trao đổi dữ liệu từ xa với bất kỳ thiết bị nào thực hiện giao thức.
* Invoke-Command cmdlet là một Powershell cmdlet sử dụng các tính năng của Powershell Remoting, có thể chạy các lệnh trên máy local hoặc từ xa và trả về toàn bộ đầu ra trên giao diện dòng lệnh, bao gồm cả các thông báo lỗi.
* Để Invoke-Command có thể hoạt động, Powershell Remoting phải được kích hoạt và khả dụng trên máy server. Trên máy Windows Server 2008 có thể kích hoạt Powershell Remoting thông qua lệnh `winrm quickconfig` hoặc `Enable-PSRemoting`.
* Nếu máy server có kích hoạt Powershell Remoting, attacker có thể sử dụng Invoke-Command để tiến hành các tấn công Remote Command Execution với tham số **-ComputerName** là hostname của máy Windows Server 2008 và các dòng lệnh được đặt trong tham số **-ScriptBlock**.

## How does Invoke-Command work?
* Khi nhập vào một câu lệnh, câu lệnh đó sẽ được chuyển qua mạng tới và khởi chạy bên trong powershell client của remote computer. Kết quả sẽ được gửi tới và xuất hiện tại phiên Powershell trên local computer.
* Để có thể chuyển lệnh và nhận kết quả, powershell sử dụng WS-Management protocol.
* Khi local computer kết nối tới remote computer, WS-Management thiết lập một kết nối và sử dụng một plug-in cho Powershell để start **Powershell host process (Wsmprovhost.exe)** tại remote computer. 
