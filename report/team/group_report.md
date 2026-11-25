# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Delta
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

- Mục tiêu: dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để bảo vệ trước hội đồng Gate 2a (chỉ duyệt kế hoạch pilot), trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.
- Cách tiếp cận: tính chi phí mỗi việc thành công từ trace (1.200 yêu cầu, 1.624 lần chạy) bằng `src/lab13.py`, người kiểm số tính tay đối chiếu; hai người gắn nhãn độc lập 20 ca lỗi; người giữ hồ sơ điền dần `ho_so_launch_v0.md` từ CP1.
- Chia vai: người viết code (Đạt) · người kiểm số (Nguyên) · người gắn nhãn 1 (Duy) · người gắn nhãn 2 kiêm giữ hồ sơ (Phước Anh). Mỗi người chỉ sửa file mình phụ trách để tránh conflict Git.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | Tử số cộng token, tool của mọi lần chạy (kể cả lỗi) cùng phút xem lại, làm lại (`simulated`); mẫu số chỉ đếm 978 việc `thanh_cong`; tách theo `loai`; cộng cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` | [bang_chi_phi.md](bang_chi_phi.md), `src/lab13.py` |
| B · Bảng độ nhạy | Đổi từng yếu tố, đổi một cặp, so giới hạn chạy lại 1–3 lần theo chi phí cả hệ thống, kịch bản xem lại 100% | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Hai bộ nhãn độc lập theo 5 loại Google PAIR, tính đồng thuận, quy tắc cho ca không trùng, bảng khắc phục 5 ca | [bang_loi.md](bang_loi.md) |
| D · Pilot plan | Tính cỡ mẫu theo 3 cách chia (yêu cầu, nhân viên, depot), chọn chia theo nhân viên 20 + 20 vì đủ 20 cụm và chia ngẫu nhiên; chấp nhận MDE 6 điểm; viết 3 luật dừng an toàn, chi phí, mức dùng theo mẫu NẾU–TRONG–THÌ–KHÔNG THÌ | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Chỉ số, rủi ro, hồ sơ | Tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, 10 event có `trace_id` và kiểm tra chéo từng chỉ số; 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy; hồ sơ một trang đủ 7 mục | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** (`simulated`), gấp **16,3×** hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm **92,5%** tổng chi phí, lớn nhất là làm lại **51,8%** (`simulated`).
- So với nhân viên tự làm (12.000 đ): cả hệ thống **5.865 đ/yêu cầu = 0,49×**; phạm vi `noi_dia` + `hang_nang` cộng cố định **4.599 đ = 0,38×** (`simulated`). Loại `quoc_te` (**1,88×**) và `doi_tac` (**0,85×**, điều khoản riêng) khỏi pilot.
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%) · tỉ lệ xem lại (+40,7%) · lương nhân viên (+23,1%) (`simulated`). Xem lại 100% đẩy chi phí lên **0,98–1,03×** (`simulated`).
- Bảng lỗi: tỉ lệ đồng thuận **19/20 = 95%** (ngưỡng 80%); ca lệch duy nhất là ca 8, thống nhất **Ngầm** theo quy tắc "sai mà chưa ai nhận ra là Ngầm, đã lộ ra mới là Hệ thống"; bảng khắc phục đủ 5 loại.
- Chỉ số trong đợt chạy thử: chính **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200; phạm vi pilot 3,97%). Đợt chạy thử không có nhóm đối chứng nên chưa kết luận được tác động.
- Pilot: chia theo nhân viên **20 + 20**, ngẫu nhiên, đối chứng song song; chia theo yêu cầu cần **1.251/nhóm**, theo nhân viên m = 75 cần 84 người > 40 nên không đủ; chọn MDE **6 điểm** (859/nhóm, DE 6,96, m ≥ 299 yêu cầu mỗi người); 3 luật dừng; ngày quyết định 2027-01-05.
- Đề xuất cuối của `ho_so_launch_v0.md`: **Go có điều kiện** cho `noi_dia` + `hang_nang`, với 4 điều kiện: sửa ca 7 và ca 20 (hoàn trùng), Giám đốc vận hành ký chấp nhận MDE 6 điểm (power khoảng 0,64 ở mức 5 điểm), bật đủ event và thay phút `simulated` bằng phút đo thật sau tuần 1, giảm xem lại theo bậc về ≤ 4,8 phút mỗi ca.
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: *(điền sau buổi duyệt chéo: điểm / 30, quyết định, câu hỏi của hội đồng)*

## 5. Khó khăn và cách xử lý

- Hai người cùng sửa `ho_so_launch_v0.md` lúc CP1–CP2: người giữ hồ sơ pull bản của người kiểm số về, giữ nguyên số, chỉ bổ sung nhãn `simulated` và người phụ trách (commit `31fd268`); từ đó chỉ người giữ hồ sơ sửa file này.
- Pull bị conflict khi người viết code cập nhật mục 6 cùng lúc người giữ hồ sơ cập nhật mục 5 (hai dòng liền nhau): gộp tay, giữ cả hai dòng, không mất nội dung (commit `7746d43`).
- Ở mức chênh 5 điểm, chia theo nhân viên 20 + 20 chỉ đạt tối đa 1.000 cỡ mẫu hiệu dụng < 1.251: nhóm chấp nhận MDE 6 điểm và đưa việc ký chấp nhận thành một điều kiện của đề xuất.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập (`simulated`); cần thay bằng phút đo thật sau tuần đầu pilot.
- Pilot chỉ thấy được mức chênh 6 điểm; nếu tác động thật là 5 điểm thì power chỉ khoảng 0,64, dễ bỏ sót.
- Các ngưỡng phát hiện trong bảng khắc phục và ngày kiểm tra của đề xuất là giả định của nhóm (lấy mốc bắt đầu pilot 2026-12-07), cần xác nhận với LogiX-VN.
- Chưa xử lý `quoc_te` (1,88×, `simulated`) và `doi_tac`; cần thiết kế riêng nếu muốn mở rộng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
