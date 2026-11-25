# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Đức Duy (2A202604071) · Người gắn nhãn 2: Bùi Phước Anh (2A202604102) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Ngầm |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Quy tắc phân biệt (từ ca 8):** Khi hệ thống làm sai so với thiết kế hoặc chính sách, xét xem lỗi có bị phát hiện không. Nếu khách hàng, nhân viên hoặc cảnh báo của hệ thống đã phát hiện ra lỗi thì gắn nhãn **Hệ thống** (ca 2, 7, 15, 20). Nếu không ai nhận ra thì gắn nhãn **Ngầm** (ca 5, 8, 12, 17). Ở ca 8, trợ lý trích dẫn một điều khoản không có trong chính sách, nhưng số tiền hoàn vẫn đúng nên cả khách lẫn hệ thống đều không phát hiện. Vì vậy ca này là Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ngân hàng trả lỗi "số tài khoản không hợp lệ"; log tool hoàn tiền ghi nhận lệnh bị từ chối; cảnh báo khi tỉ lệ lệnh hoàn bị ngân hàng từ chối vượt 2% mỗi ngày | Kiểm tra định dạng và độ dài số tài khoản ngay lúc nhập; đọc lại tên chủ tài khoản để khách xác nhận trước khi tạo lệnh hoàn | Team sản phẩm (UX form nhập) |
| 7 | Hệ thống | Đối soát giữa log API (503, không có bản ghi hoàn) và tin nhắn "đã hoàn tiền thành công" gửi khách; khách khiếu nại vì chưa nhận tiền; đối soát hằng giờ, cảnh báo khi có ≥ 1 tin "thành công" mà không có mã giao dịch | Chỉ báo thành công khi API trả 2xx và có mã giao dịch; sau 3 lần thử lỗi thì báo "đang xử lý", đưa vào hàng đợi và chuyển nhân viên; thêm test cho nhánh lỗi API | Kỹ sư backend |
| 3 | Ngữ cảnh | Khách báo "chưa được hoàn"; theo dõi tỉ lệ ticket có nội dung "chưa nhận tiền" trong khi giao dịch vào ví đã thành công; cảnh báo khi ticket "chưa nhận tiền" chiếm hơn 5% số đơn đã hoàn vào ví trong tuần | Tin nhắn hoàn tiền nêu rõ "đã hoàn vào ví LogiX" kèm hướng dẫn kiểm tra hoặc rút về ngân hàng; cho khách chọn nơi nhận tiền hoàn | Product owner |
| 11 | Giới hạn hệ thống | Log loại đầu vào: tin nhắn thoại bị trả lời "vui lòng nhập bằng chữ"; đếm số khách rời đi sau phản hồi đó; đếm số tin nhắn thoại mỗi tuần, ưu tiên làm speech-to-text khi vượt 3% số yêu cầu | Trước mắt: chuyển tin nhắn thoại cho nhân viên hoặc gửi kèm nút gõ nhanh các yêu cầu phổ biến. Lâu dài: thêm speech-to-text | Product owner |
| 17 | Ngầm | Đối soát định kỳ phí đã tính so với bảng giá đang hiệu lực; cảnh báo khi phiên bản bảng giá trong tool khác với bản mới nhất; chạy đối soát mỗi ngày, cảnh báo khi phiên bản bảng giá lệch ≥ 1 ngày hoặc ≥ 10 đơn bị tính sai | Gắn phiên bản và ngày hiệu lực cho bảng giá, tool từ chối dùng bảng hết hạn; tính lại 212 đơn và hoàn phần chênh; thêm job đối soát hằng ngày | Data/ops engineer |
