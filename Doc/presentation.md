# Nội dung thuyết trình

## Giới thiệu đề tài
* Để biết được mục đích của đề tài này, chúng ta hãy cùng tìm hiểu về khái niệm của tấn công máy tính.
* Tấn công máy tính thường được người dùng biết đến ở dạng một chương trình độc hại, gây ra lỗi nghiêm trọng cho một hoặc nhiều máy tính cùng lúc nhằm phục vụ nhiều mục đích khác nhau của kẻ tấn công như: Đánh cắp thông tin, chiếm quyền điều khiển từ xa, phá hoại dữ liệu,… 
* Như vậy để đối phó với tấn công hay tìm ra được lỗ hổng nào đang có trên máy tính, thông thường quản trị viên sẽ tìm đến mục chứa log của máy bị tấn công và đọc thông tin log xem chuyện gì đang xảy ra. Vấn đề ở đây là làm sao để kiểm soát một số lượng máy nhất định bằng việc quản lý log tập trung (không cần phải đến từng máy xem log)?
* Đề tài này ra đời nhằm giải quyết cho vấn đề đó, nhóm đã thực hiện một mô hình hệ thống có thể quản lý và truy vấn log tập trung từ nhiều nguồn khác nhau để phát hiện tấn công mà không cần phải đến từng máy để xem log dựa trên bộ công cụ ELK Stack.
