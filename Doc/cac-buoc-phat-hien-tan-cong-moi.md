# Các bước phát hiện một tấn công mới
1. Tìm hiểu thông tin cơ bản của tấn công đó : Loại tấn công (**Command Execution**, **Pass the Hash** hay **Escalation to System Privileges**, ...), các thuật ngữ xung quanh tấn công này, cách thức hoạt động cơ bản của tấn công.
2. Tìm hiểu chi tiết về cách thức hoạt động của tấn công để có thể suy luận ra điểm khác biệt của tấn công với các loại tấn công khác (làm cơ sở cho việc phát hiện **bằng chứng thực thi**)
3. Thực hiện lại tấn công trên và xem lại log ghi được tại Event Viewer
4. Khi đã có các log thực thi, suy luận ra **bằng chứng thực thi**
5. Chuyển bằng chứng thực thi sang Query DSL, tiến hành truy vấn và xem kết quả trên Kibana. Nếu kiểm tra vài lần thành công thì lưu câu truy vấn Query DSL này vào chương trình phát hiện tấn công tự động.
6. Thực hiện các tấn công với địa chỉ IP khác (trên các máy khác), trên các tài khoản khác hoặc thay thế bằng các công cụ tương tự. Thống kê để biết được độ hiệu quả của câu lệnh Query DSL đưa ra. Nếu không hiệu quả thì quay lại tìm **bằng chứng thực thi** kh chặt chẽ hơn.
