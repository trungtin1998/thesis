<!--- The first time writes markdown kindly --->
# Mimikatz
Date: 25/06/2020.</br>
Tool: [The Mimikatz GitHub repository](https://github.com/gentilkiwi/mimikatz)

## Mimikatz Overview
* Mimikatz là một công cụ dùng để thu thập credential từ hệ thống Windows.
* Mimikatz là 1 chương trình x32/x64 được lập trình bằng ngôn ngữ C bởi Benjamin Delpy. Có 2 lựa chọn cấu thành cung cấp các tính năng bổ sung:
  * mimidrv: driver được dùng để tương tác với kernel của Windows.
  * mimilib: "AppLocker bypass, Auth package/SSP, password filter, and sekurlsa for WinDBG". [3]
* Mimikatz yêu cầu **quyền admin** hoặc **quyền hệ thống** và thông thường là **quyền debug** để thực hiện một số hành động nhất định, cụ thể là **tương tác với tiến trình LSASS** (ví dụ: Để sử dụng lệnh: `sekurlsa:logonpasswords`, cần chạy `privilege::debug`). 

## How does mimikatz work?
* Sau khi user đăng nhập vào hệ thống, các thông tin về credential (username, domain, SID, cleartext password, hash password, có thể có Kerberos ticket, ...) sẽ được lưu trữ bên trong LSASS (Local Security Authority Subsystem Service), tiến trình lưu trữ thông tin tại memory (RAM).
* 

## LSASS
* SSO - Single Sign-On: Truy cập vào các resources mà không cần reauthenticate
* Cung cấp sự truy cập vào credentials đã xác thực và đang còn mở phiên
* Kể từ Windows 8.1 và Windows Server 2012 R2 trở lên, LSASS không còn lưu clear-text password tại memory, tuy nhiên NTLM hash vẫn được LSASS lưu.

## Mimikatz Defense
1.  Disable cleartext passwords in memory
* Nếu bạn đang sử dụng Windows 7 hoặc Windows Server 2008 trở xuống, LSASS vẫn sẽ lưu cleartext password tại memory. Đó là lý do tại sao ta cần không cho phép cleartext password được lưu tại memory.
* Ta có thể thủ công thực hiện quá trình này. Đó là lưu giá trị registry key `HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Control/SecurityProviders/WDigest/UseLogonCredential` thành 0

2. Change the krbtgt account password
* Tài khoản krbtgt cũng có thể được thay đổi password như các loại tài khoản khác. Hash password của krbtgt có thể được sử dụng để làm Golden Ticket, loại ticket có thời hạn mặc định 10 năm khi được mimikatz tạo ra. Có nghĩa là nếu ta không thay đổi password của krbtgt thường xuyên, attacker có thể sử dụng Golden Ticket được tạo thành công ở lần tấn công trước để có thể tái truy cập vào hệ thống bạn.
* Bởi vì Active Directory duy trì password trước đây và password hiện tại, do đó cần **thay đổi password cho Kerberos 2 lần**.

3. LSASS.exe protected mode
* Vì mimikatz lấy các thông tin từ LSASS nên ta có thể phòng chống mimikatz attack bằng cách không cho phép tiến trình mimikatz gọi đến và truy vấn thông tin từ LSASS.
* Từ Windows 8.1 và cao hơn, có thể chạy LSASS với protected mode, chỉ cho phép các tiến trình cũng ở chế độ protected mode khác gọi đến. Ta có thể set DWORD registry key `HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Control/Lsa = 1`

## Mimikatz Detection
1.  Monitor for unusual accounts 
* Lập ra Whitelist các tài khoản thuộc domain hoặc local group. Nếu có sự đăng nhập thành công từ các tài khoản không thuộc Whitelist này, chứng tỏ rằng có sự tấn công.
* Điểm hạn chế của phương pháp này là, nếu tên tài khoản mà attacker đăng nhập vào hệ thống nằm trong Whitelist thì không thể phát hiện được.

2. Monitor các lần đăng nhập thất bại
* Các lần đăng nhập sai do các tấn công mimikatz pass-the-hash thì xuất hiện Event ID 4769 với Result Code 0x1F với mô tả rằng "failed integrity check on a decrypted field" (Có thể do krbtgt bị thay đổi hoặc sai 1 thông số nào đó của hệ thống nạn nhân).
* Với các lần đăng nhập sai này sẽ để lại địa chỉ IP của attacker, ta có thể sử dụng địa chỉ IP này mà chặn chúng.

## Tài liệu tham khảo
[1] Jim Mulder, ["Mimikatz Overview, Defenses and Detection"](https://www.sans.org/reading-room/whitepapers/detection/mimikatz-overview-defenses-detection-36780), February 18, 2016.</br>
[2] Jake Liefer, ["Detecting In-Memory Mimikatz"](https://securityriskadvisors.com/blog/detecting-in-memory-mimikatz/), Accessed July 25, 2020.</br>
[3] Sean Metcalf, ["Unofficial Guide to Mimikatz & Command Reference"](https://adsecurity.org/?page_id=1821), Accessed July 26, 2020.

