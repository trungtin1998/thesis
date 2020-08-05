# Làm sao để phát hiện hệ thống đã bị disable Audit Policy
# Ngày: 05/08/2020

## Tổng quan về Audit Policy
* Audit Policy là một tính năng của Microsoft, cho phép ta có thể giám sát hoạt động của hệ thống, theo dõi sự tạo các tiến trình, các kết nối đến máy tính với port cụ thể,... 
* Tất cả các sự kiện này do Audit Policy giám sát và được ghi nhận tại Security Log.
* Việc kích hoạt Audit Policy là điều cần thiết bởi vì với thiết lập mặc định, rất nhiều hoạt động của hệ thống sẽ không được ghi nhận lại. Do đó sẽ rất khó để quản trị viên có thể biết được chính xác những gì xảy ra trong hệ thống khi có sự cố xảy ra.

## Thực hiện disable Audit Policy
* Các server thường phải kích hoạt Audit Policy để giám sát toàn bộ các hoạt động diễn ra trên hệ thống. Mục đích là có thể phát hiện các tấn công có thể xảy đến. Do đó disable Audit Policy là một việc làm có thể được nhắm tới bởi các Attacker.
* Vậy ta cần giám sát hoạt động của Event Log khi có sự thay đổi cấu hình của Audit Policy.
* Khi ta thay đổi bất kì policy nào của Audit Policy, một sự kiện sẽ được tạo ra trong Security Log, thông báo rằng việc thay đổi policy đã được diễn ra:
  * Event ID 4719 tại Security Log: (System audit policy was changed)
![Sensitive Privilege Use](/Images/sentitive_privilege_use.png)
![Non Sensitive Privilege Use](/Images/non_entitive_privilege_use.png)
![Other Privilege Use Events](/Images/other_privilege_use.png)
* Khi thấy các log này tại Event Viewer, ta có thể nhận biết được có sự disable policy của trường **Audit privilege use** tại Audit Policy. Do đó bằng chứng thực thi của **disable Audit Policy** là **Event ID 4719**

## Chuyển sang Query DSL
* Đoạn Query DSL gửi về Log server để phát hiện sự kiện disable Audit Policy là:
  * `event.code: 4719`
```
{
  "version": true,
  "size": 500,
  "sort": [
    {
      "@timestamp": {
        "order": "asc",
        "unmapped_type": "boolean"
      }
    }
  ],
  "aggs": {
    "2": {
      "date_histogram": {
        "field": "@timestamp",
        "fixed_interval": "30s",
        "time_zone": "Asia/Ho_Chi_Minh",
        "min_doc_count": 1
      }
    }
  },
  "query": {
    "bool": {
      "filter": [
        {
          "match_phrase": {
            "event.code": "4719"
          }
        }
      ]
    }
  }
```

## Cảnh báo cho quản trị viên
* Khi có tấn công disable Audit Policy
  * Tại kibana sẽ hiển thị:
![Kibana](/Images/kibana_audit_policy.png)
  * Tại mail của quản trị viên sẽ có cảnh báo:
![Mail Alert](/Images/alert_audit_policy.png)

## Bảng thống kê
| Username | Địa chỉ IP | Hệ điều hành | Vai trò của tài khoản | Hành động thực hiện | Số lần thực hiện | Số lần thành công |
|:-------:|:------:|:------:|:------:|:------:|:------:|:-------:|
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | Disable policy "Audit privilege use" | 2 | 2 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | Thêm policy "Audit privilege use" | 2 | 2 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | Disable policy "Audit logon events" | 1 | 1 |
| Administrator | 192.168.255.100 | Windows Server 2008 | Administrator | `auditpol /set /Category:"Account Logon" /success:disable /failure:disable` | 1 | 1 |
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | `auditpol /set /Category:"System" /failure:disable` | 1 | 1 |
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | `auditpol /set /Category:"DS Access" /success:disable /failure:disable` | 1 | 1 |
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | Disable policy "Audit account management" | 1 | 1 |
| sv | 192.168.255.100 | Windows Server 2008 | Thành viên của Administrator group | Thêm policy "Audit system event" | 1 | 1 |
* Số lần thực hiện: 10
* Tỉ lệ thành công: 100%
* Khóa luận đã thực hiện kiểm tra disable Audit Policy thủ công (Trong Local Security Policy) và thực hiện qua command line với sự hỗ trợ của công cụ `auditpol` 

## Tài liệu tham khảo
[[1] Windows Security Log Event ID 4719](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4719)
