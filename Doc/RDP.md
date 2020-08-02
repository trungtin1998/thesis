# Remote Desktop Protocol

## Tổng quan
* Remote Desktop Protocol (RDP) là giao thức cho phép thiết lập các kết nối, có khả năng tương tác với giao diện người dùng ở các máy tính khác. 
* Chức năng cơ bản của RDP là truyền tải giao diện (output devices) trên các remote server tới client và sự nhập liệu tương tác với bàn phím, chuột (input devices) từ client tới remote server.
* Giao tiếp trong suốt kết nối RDP hầu hết dữ liệu sẽ được truyền từ máy server tới client.
* Giao tiếp sẽ được mã hóa bằng RSA’s RC4 block cipher theo mặc định.
* Remote Desktop Protocol hoạt động ở 3389/tcp hoặc 3389/udp.
* Thông thường, RDP sẽ chỉ cho phép các tài khoản thuộc administrators group được thiết lập Remote Desktop Connection. Tuy nhiên các standard user vẫn được mở các kết nối tới bằng cách thêm các tài khoản này vào tính năng remote tại Server.
