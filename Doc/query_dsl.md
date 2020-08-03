# Query DSL trong Elasticsearch

## Tác dụng của Query DSL
* Chuyển bằng chứng thực thi bắt các tấn công thông qua Event Viewer sang dạng gửi truy vấn tới ELK, cụ thể là gửi tới Elasticsearch (port 9200) để có thể lọc ra đâu là các sự kiện xảy ra tấn công nào.

## Các thành phần của Query DSL
* `match` query: Tìm kiếm một string nào đó bằng cách parse thành các token (do cơ chế tự động analyze text), không phân biệt thứ tự các token đó. Không phân biệt chữ hoa chữ thường. Ví dụ tìm "s" thì "S" vẫn được trả về trong kết quả tìm kiếm.
* `match_phase` query: Giống `match` query nhưng có phân biệt thứ tự các token.
* `term`: Giá trị nhập vào không bị analyze và phân biệt hoa thường.
* `query string`: search t
