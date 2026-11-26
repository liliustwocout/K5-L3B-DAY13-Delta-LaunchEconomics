# Báo cáo cá nhân — LeBaNguyen-2A202604100

## 1. Thông tin thành viên

- Họ tên: Lê Bá Nguyên
- MSSV: 2A202604100
- Email: nguyenbropmt@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số

## 2. Phần việc phụ trách

- Tính tay đối chiếu số liệu từ trace và công thức cho nhiệm vụ A, B, D1.
- Điền và kiểm tra bảng số liệu, câu trả lời trong `report/team/bang_chi_phi.md` (bảo đảm nhãn `simulated` và quy tắc ≤ 3 dòng).
- Tham gia đổi vai viết code sau giải lao và chạy kiểm tra chéo `src/lab13.py` trên máy khác trong nhóm.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A (CP1):**
  - Tính tay độc lập 3 phép thử đáp án biết trước A1 ($p=0,8$): $1,20$ (tối đa 2 lần); $1,25$ (chạy đến khi đúng); $1,25$ (hệ số chi phí tối đa 3 lần).
  - Tính tay kiểm tra mẫu một số trace để xác nhận code tính đúng công thức token và tool (chia 1.000 trước khi nhân đơn giá); đối chiếu kết quả mô hình A2 (chi phí mỗi việc thành công $4.472$ đ `simulated`, gấp $16,3$ lần hoá đơn token + tool; làm lại chiếm $51,8\%$, xem lại $40,7\%$).
  - Đối chiếu bảng A3 theo 4 loại yêu cầu, xác nhận `quoc_te` ($22.515$ đ, $1,88\times$ tự làm) và `doi_tac` ($10.215$ đ, $0,85\times$) không hiệu quả để đưa vào pilot; tính tay bảng A4 chi phí cố định ($4.599$ đ ở quy mô full và $5.784$ đ ở quy mô nửa).
- **Nhiệm vụ B (CP2):**
  - Kiểm tra tính đối xứng của 9 kịch bản độ nhạy B1 (mỗi kịch bản giảm một nửa làm giảm đúng một nửa mức tăng của kịch bản nhân đôi).
  - Xác nhận kịch bản cặp đôi B2 ($+46,3\%$) và xếp hạng 3 yếu tố nhạy nhất: 1. Làm lại ($+51,8\%$), 2. Xem lại ($+40,7\%$), 3. Lương nhân viên ($+23,1\%$).
  - Tính toán chi phí cả hệ thống ở B3, chỉ ra giới hạn 2 lần chạy là rẻ nhất cho công ty ($6.901.220$ đ `simulated`), dù giới hạn 1 lần cho cps thấp nhất ($4.111$ đ).
  - Phân tích kịch bản xem lại 100% ở B4, tính điểm hòa vốn xem lại $\le 4,8–5,1$ phút.
- **Nhiệm vụ D (CP4) & E (CP5):**
  - Kiểm tra chéo 5 con số cỡ mẫu D1 ($1.251$ YC/nhóm; nhân viên $m=75$ cần 84 người; tối đa hiệu dụng 20 nhân viên là $1.000$; MDE 6 điểm cần $m \ge 299$ YC/người, power ở mức 5 điểm là $0,64$).
  - Soạn thảo và hoàn thiện bảng **E2 · Rủi ro kinh tế** trong `report/team/chi_so.md` gồm 3 rủi ro kinh tế lớn rút ra từ bảng độ nhạy.
  - Rà soát toàn bộ các file hồ sơ để bảo đảm quy tắc: mọi con số từ cột giả lập đều có nhãn `simulated`, mỗi câu trả lời $\le 3$ dòng và có số, không dùng thuật ngữ bị cấm trong quy tắc lab.

## 4. Bằng chứng

- Các commit cập nhật số liệu và hồ sơ:
  - Commit `80afbc3`: Cập nhật bảng rủi ro kinh tế E2 và các mục chi phí CP1/CP2 vào `chi_so.md` và `ho_so_launch_v0.md`.
  - Commit `553d283`: Hoàn thành `pilot_plan.yaml`, bổ sung tính cỡ mẫu D1 trong `lab13.py` và cập nhật mục 6 hồ sơ launch v0.
- Kết quả chạy `src/lab13.py` thành công trên máy cá nhân, khớp $100\%$ đáp án:
  - 3 phép thử A1 in ra `ĐẠT` ($1,20$ · $1,25$ · $1,25$).
  - Chi phí mỗi việc thành công $4.472$ đ `simulated`, hệ thống $5.865$ đ ($0,49\times$).
  - Bảng độ nhạy B1 đủ 9 dòng, chi phí hệ thống k=2 rẻ nhất ($6.901.220$ đ).
  - Cỡ mẫu D1: $n=1.251$ (chia YC), $m \ge 299$ (chia NV MDE 6 điểm).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Antigravity / Claude / Gemini).
- **Mục đích sử dụng:**
  - Tra cứu công thức giải phương trình tìm cỡ cụm $m$ khi biết cỡ mẫu hiệu dụng và ICC trong Cluster Randomized Trial.
  - Soát lỗi cú pháp YAML và soát lỗi định dạng checklist (kiểm tra không còn thuật ngữ bị cấm, kiểm tra nhãn `simulated`).
- **Cách tự kiểm tra:** Tự tay bấm máy tính giải phương trình và tính lại các phép nhân chia trên dữ liệu mẫu trước khi điền vào báo cáo; chạy trực tiếp script Python kiểm tra YAML và hàm thống kê để đối chiếu kết quả.

## 6. Tự đánh giá

- Mức độ hoàn thành: **100%**.
- Hoàn thành đúng vai trò Người kiểm số: độc lập kiểm tra, đối chiếu số liệu tính toán từ trace với lý thuyết, bảo đảm tính liêm chính và độ chính xác của mọi con số trong toàn bộ hồ sơ Gate 2a của nhóm Delta.
