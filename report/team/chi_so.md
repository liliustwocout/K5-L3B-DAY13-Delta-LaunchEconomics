# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (`994/1.200`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (`48/177`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (`51/1.200`; trong phạm vi `noi_dia + hang_nang` là **3,97%**, `39/982`) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu nhóm can thiệp được mở bằng trợ lý | Số yêu cầu phạm vi pilot ở nhánh can thiệp có ít nhất 1 `agent_run_completed` (`attempt = 1`), chia tổng yêu cầu nhánh can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền trên mẫu kiểm tra hằng tuần & tỉ lệ ca hoàn trùng | Số đơn lệch `so_tien_da_hoan != so_tien_dung` chia tổng mẫu kiểm tra hằng tuần; và số đơn có ≥ 2 `refund_ledger_write` thành công | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id, loai, so_tien_vnd, depot, arm, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id, staff_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiện lên cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id, staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai, trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id, staff_id, phut_lam_lai, ly_do, trace_id` | Khi nhân viên xử lý làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id, idempotency_key, so_tien_vnd, ket_qua, trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `request_id, reason, tom_tat, trace_id` | Khi chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id, closed_at, dong_trong_24h, trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách / CSKH | `request_id, reopened_at, mo_lai_trong_7_ngay, reason, trace_id` | Khi yêu cầu bị mở lại |
| `audit_sample_checked` | Kế toán / QA | `request_id, so_tien_da_hoan, so_tien_dung, lech_vnd, trace_id` | Khi kiểm tra mẫu đối soát hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (`% đóng trong 24 giờ và không mở lại trong 7 ngày`):** tính từ `refund_request_created` + `ticket_closed` (`dong_trong_24h = 1`) đối chiếu loại trừ `ticket_reopened` (`mo_lai_trong_7_ngay = 1`) theo `request_id`/`trace_id` → **đo được**.
- **Chỉ số dùng (`Tỉ lệ bỏ qua gợi ý`):** tính từ `staff_review_decision` (`quyet_dinh` là `sua` hoặc `bo`) chia tổng `agent_suggestion_shown` (hoặc tổng `staff_review_decision`) → **đo được**.
- **Chỉ số an toàn (`Tỉ lệ lỗi lọt đến khách`):** tính từ `ticket_reopened` (`mo_lai_trong_7_ngay = 1`) chia tổng `refund_request_created` → **đo được**.
- **Chỉ số dùng tự đề xuất (`Tỉ lệ mở bằng trợ lý ở nhóm can thiệp`):** tính từ `agent_run_completed` (`attempt = 1`) chia `refund_request_created` (`arm = treatment`) → **đo được**.
- **Chỉ số an toàn tự đề xuất (`Hoàn sai tiền trên mẫu tuần & hoàn trùng`):** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung`) và `refund_ledger_write` (lọc `request_id` có ≥ 2 bản ghi thành công) → **đo được**.
- *(Ghi chú chi phí thật sau tuần 1: `agent_run_completed` ghi `tokens_in/out, tool_calls`; `staff_review_decision` và `staff_rework_completed` ghi `phut_xem_lai`, `phut_lam_lai` đo thật để thay thế số `simulated`.)*

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, lên **6.787 đ** (`simulated`) | Tỉ lệ làm lại theo tuần vượt **7%** số yêu cầu trong phạm vi (đợt chạy thử: 4,9%) | Thu hẹp phạm vi về `noi_dia`, rà soát 20 trace làm lại gần nhất để sửa prompt/tool | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí lên **11.743 đ = 0,98×** (hoặc **12.415 đ = 1,03×** nếu ca làm lại 15,3 phút như dữ liệu), hòa vốn xem lại chỉ còn **≤ 4,8–5,1** phút (`simulated`) | Tỉ lệ xem lại vẫn còn **> 50%** vào cuối tuần thứ 2 của bước rollout 0.25 | Kích hoạt lộ trình giảm xem lại theo bậc (chỉ xem lại ca nghi ngờ) khi tỉ lệ sửa+bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng làm đội thêm **1.185 đ/việc** ở 45k YC/tháng và **2.370 đ/việc** nếu chỉ còn một nửa (`simulated`) | Số lượng yêu cầu thành công theo tuần thấp hơn **50%** dự báo | Tạm hoãn mở rộng pilot, đàm phán lại chi phí hạ tầng/hợp đồng cố định | PM trợ lý hoàn phí |
