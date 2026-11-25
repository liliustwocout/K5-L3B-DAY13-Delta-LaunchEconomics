# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, lên **6.787 đ** (`simulated`) | Tỉ lệ làm lại theo tuần vượt **7%** số yêu cầu trong phạm vi (đợt chạy thử: 4,9%) | Thu hẹp phạm vi về `noi_dia`, rà soát 20 trace làm lại gần nhất để sửa prompt/tool | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí lên **11.743 đ = 0,98×** (hoặc **12.415 đ = 1,03×** nếu ca làm lại 15,3 phút như dữ liệu), hòa vốn xem lại chỉ còn **≤ 4,8–5,1** phút (`simulated`) | Tỉ lệ xem lại vẫn còn **> 50%** vào cuối tuần thứ 2 của bước rollout 0.25 | Kích hoạt lộ trình giảm xem lại theo bậc (chỉ xem lại ca nghi ngờ) khi tỉ lệ sửa+bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng làm đội thêm **1.185 đ/việc** ở 45k YC/tháng và **2.370 đ/việc** nếu chỉ còn một nửa (`simulated`) | Số lượng yêu cầu thành công theo tuần thấp hơn **50%** dự báo | Tạm hoãn mở rộng pilot, đàm phán lại chi phí hạ tầng/hợp đồng cố định | PM trợ lý hoàn phí |
