# Các định nghĩa cơ bản

## NTLM Authentication
* Windows Challenge/Response (NTLM) là giao thức xác thực qua đường mạng được sử dụng trên các hệ điều hành Windows.
* NTLM credentials bao gồm các thông tin về phiên đăng nhập: domain name, user name và mã hash của password.
* NTLM là giao thức mã hóa challenge/response, dùng để xác thực người dùng mà không cần gửi cleartext password qua mạng.
* Xác thực NTLM thông qua mạng thường bao gồm 2 hệ thống: Client và Domain Controller
  * Client: Nơi người dùng yêu cầu xác thực
  * Domain Controller: Nơi lưu trữ password của người dùng
* Các bước xác thực khi người dùng đăng nhập vào domain sử dụng NTLM Authentication
  1. Người dùng đăng nhập vào máy tính client, điền vào các thông tin domain name, username và password. Client sẽ mã hóa password và discard cleartext password.
  2. Client gửi username cho Server. (plaintext)
  3. Server phát sinh ra một số ngẫu nhiên 16-byte, được gọi là challenge hoặc là nonce, và gửi chúng cho client.
  4. Client mã hóa số nonce này bằng NTLM hash password của user rồi gửi lại cho server. Kết quả được tính toán gọi là response.
  5. Server gửi 3 items cho Domain Controller:
    * username
    * Challenge gửi tới cho Client
    * Response - kết quả hash Challenge của Client
   6. Domain Controller sử dụng username mà Server gửi tới để tìm ra hash password tương ứng tại Security Account Manager database. 
   7. Sử dụng hash password này để mã hóa Challenge của Server và đối chiếu với Response. Nếu giống nhau thì xác thực thành công. [1]
   

## Tài liệu tham khảo
[1] Microsoft, [Microsoft NTLM](https://docs.microsoft.com/en-us/windows/win32/secauthn/microsoft-ntlm?redirectedfrom=MSDN)
https://www.varonis.com/blog/closer-look-pass-hash-part-one/
