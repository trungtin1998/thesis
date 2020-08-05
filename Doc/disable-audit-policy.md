# Làm sao để phát hiện hệ thống đã bị disable Audit Policy
# Ngày: 05/08/2020

## Tổng quan về Audit Policy
* Audit Policy là một tính năng của Microsoft, cho phép ta có thể giám sát hoạt động của hệ thống, theo dõi sự tạo các tiến trình, các kết nối đến máy tính với port cụ thể,... 
* Tất cả các sự kiện này sẽ được được Audit Policy giám sát sẽ được ghi nhận tại Security Log.
* Việc kích hoạt Audit Policy là điều cần thiết bởi vì với thiết lập mặc định, rất nhiều hoạt động của hệ thống sẽ không được ghi nhận lại. Do đó sẽ rất khó để quản trị viên có thể biết được chính xác những gì xảy ra trong hệ thống khi có sự cố xảy ra.

## Thực hiện disable Audit Policy
* Các server thường phải kích hoạt Audit Policy để giám sát toàn bộ các hoạt động diễn ra trên hệ thống. Mục đích là có thể phát hiện các tấn công có thể xảy đến. Do đó disable Audit Policy là một việc làm có thể được nhắm tới bởi các Attacker.
* Vậy ta cần giám sát hoạt động của Event Log khi có sự thay đổi cấu hình của Audit Policy.
* Khi ta thay đổi bất kì Policy nào của Audit Policy, một sự kiện sẽ được tạo ra trong Security Log, thông báo rằng việc thay đổi policy đã được diễn ra:
  * Event ID 4719 tại Security Log: (System audit policy was changed)
![Sensitive Privilege Use](/Images/sentitive_privilege_use.png)
![Non Sensitive Privilege Use](/Images/non_entitive_privilege_use.png)
![Other Privilege Use Events](/Images/other_privilege_use.png)
* Khi thấy các log này tại Event Viewer, ta có thể nhận biết được có sự disable policy của trường **Audit privilege use** tại Audit Policy. Do đó bằng chứng thực thi của disable Audit Policy là **Event ID 4719**
