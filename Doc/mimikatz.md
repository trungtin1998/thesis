<!--- The first time writes markdown kindly --->
# Mimikatz
Date: 25/06/2020

## LSASS
* SSO - Single Sign-On: Truy cập vào các resources mà không cần reauthenticate
* Cung cấp sự truy cập vào credentials đã xác thực và đang còn mở phiên
* Kể từ Windows 8.1 và Windows Server 2012 R2 trở lên, LSASS không còn lưu clear-text password tại memory [1]

## Mimikatz Defense
1.  Disable cleartext passwords in memory
* Nếu bạn đang sử dụng Windows 7 hoặc Windows Server 2008 trở xuống, LSASS vẫn sẽ lưu cleartext password tại memory. Đó là lý do tại sao ta cần không cho phép cleartext password được lưu tại memory.
* Ta có thể thủ công thực hiện quá trình này. Đó là lưu giá trị registry key `HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet /Control/SecurityProviders/WDigest /UseLogonCredential` thành 0

## Tài liệu tham khảo
[[1] Jim Mulder, "Mimikatz Overview, Defenses and Detection", February 18, 2016](https://www.sans.org/reading-room/whitepapers/detection/mimikatz-overview-defenses-detection-36780)

