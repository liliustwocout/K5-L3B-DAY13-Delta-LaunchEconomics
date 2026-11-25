# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Delta · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (gấp 16,3× hoá đơn token + tool 274,7 đ) `simulated` | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương NV (+23,1%) `simulated` | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống **5.865 đ/yêu cầu** (**0,49×** của 12.000 đ); trong phạm vi pilot `noi_dia` + `hang_nang` là **3.414 đ** (**0,28×**, cộng cố định 40tr là **4.599 đ = 0,38×**) `simulated` | Giả lập | Người viết code |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính **82,83%** (994/1.200 đóng 24 giờ, không mở lại 7 ngày) · dùng: bỏ qua gợi ý **27,12%** (48/177) · an toàn: mở lại 7 ngày **4,25%** (51/1.200; phạm vi pilot 3,97%); 10 event có `trace_id` | Xong, có bằng chứng | Người gắn nhãn 1 |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận **19/20 = 95%** (ngưỡng 80%); 5 cách khắc phục đủ 5 loại PAIR, mỗi dòng có ngưỡng phát hiện và một vai phụ trách | Xong, có bằng chứng | Người gắn nhãn 1 và Người gắn nhãn 2 |
| 6 · Pilot plan | 20 NV/nhóm (đối chứng song song), m ≥ 299 YC/NV, MDE 6 điểm (859/nhóm, DE=6,96), 3 luật dừng NẾU-TRONG-THÌ-KHÔNG THÌ | Xong, có bằng chứng | Người viết code |
| 7 · Rủi ro kinh tế | 3 rủi ro: Làm lại tăng x2 (+51,8%), Xem lại 100% (1,03× tự làm), Khối lượng giảm nửa (+2.370 đ/việc) `simulated` | Giả lập | Người kiểm số |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
