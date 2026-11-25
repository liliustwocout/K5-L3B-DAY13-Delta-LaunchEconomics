# Báo cáo cá nhân — TranDucDuy-2A202604071

## 1. Thông tin thành viên

- Họ tên: Trần Đức Duy
- MSSV: 2A202604071
- Email: tran85122@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (CP1–CP3) · Người viết code đổi vai trên máy thứ hai (CP4–E1)

## 2. Phần việc phụ trách

- Đọc đề, theo dõi điều kiện "Xong khi" và 5 quy tắc của lab ở từng checkpoint.
- CP3: tự gắn nhãn độc lập 20 ca lỗi ở cột `Nhãn người 1` trong `report/team/bang_loi.md` (không trao đổi trước khi so) và phối hợp so nhãn với người gắn nhãn 2.
- CP4–E1 (đổi vai viết code trên máy thứ hai): chạy kiểm chứng toàn bộ `src/lab13.py`, bổ sung đối chiếu `statsmodels` (`NormalIndPower`, `proportion_effectsize`), tính `power` ở `n = 859` khi tác động thật `0,05`, và viết hàm `in_nhiem_vu_e1(reqs)` tính thử 3 chỉ số đầu E1.
- CP5: hoàn thiện bảng E1 (3 chỉ số tính thử + 1 chỉ số dùng & 1 chỉ số an toàn đề xuất), danh sách 10 event có `trace_id` và mục kiểm tra chéo trong `report/team/chi_so.md`; tham gia rà soát trước Gate 2a (`report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`).

## 3. Đóng góp cụ thể

- **Chuẩn bị & kiểm chứng trên máy thứ hai:** Cài đặt `.venv` (Python 3.12.10) và các thư viện trong `src/requirements.txt`; chạy kiểm chứng toàn bộ `src/lab13.py` (3/3 phép thử A1 đạt `1,20 · 1,25 · 1,25` và khớp bảng A, B) đồng thời kiểm tra điều kiện "Xong khi", nhãn `simulated` và quy tắc ≤ 3 dòng trên `report/team/bang_chi_phi.md`.
- **CP3 (`report/team/bang_loi.md`):** Tự đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và tự gắn nhãn độc lập 20 ca vào cột `Nhãn người 1` theo nguyên nhân gốc (5 loại Google PAIR) trước khi so với người gắn nhãn 2 (Bùi Phước Anh); xử lý merge conflict khi gộp nhánh để giữ nguyên hai cột nhãn độc lập, ghi nhận tỉ lệ đồng thuận `19/20 = 95%` (chỉ lệch Ca 8 giữa `Hệ thống` và `Ngầm`).
- **CP4–E1 (`src/lab13.py`):** Pull code CP4 từ nhóm về máy thứ hai, bổ sung đối chiếu `statsmodels` cho câu D1 (`1.250` ở `MDE 0,05`; `858` ở `MDE 0,06`) và tính `power` thực tế ở `n = 859` nếu tác động thật chỉ `0,05` (`0,6417 ≈ 0,64`), đồng thời cài đặt hàm `in_nhiem_vu_e1(reqs)` tính thử 3 chỉ số chính/dùng/an toàn trên `1.200` yêu cầu.
- **CP5 (`report/team/chi_so.md`):** Giữ nguyên bảng 3 rủi ro kinh tế E2 của nhóm và hoàn thiện toàn bộ phần E1 (`82,83%`, `27,12%`, `4,25%`, riêng phạm vi pilot `3,97%`), đề xuất 1 chỉ số dùng (*tỉ lệ yêu cầu nhóm can thiệp được mở bằng trợ lý*) và 1 chỉ số an toàn (*tỉ lệ hoàn sai tiền trên mẫu kiểm tra hằng tuần & tỉ lệ ca hoàn trùng*), liệt kê 10 event đều có `trace_id` và viết kiểm tra chéo chỉ số–event; kiểm tra `yaml.safe_load` cho `pilot_plan.yaml`, quét dấu `?` và từ khóa cấm trong `report/team/`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- **Các commit đã đẩy lên `origin/main`:**
  - `7d5b52a`: `cp3(bang_loi): add independent labels for labeler 1` (cột `Nhãn người 1` cho 20 ca trong `report/team/bang_loi.md`).
  - `ed39e7d`: merge giữ nguyên cả hai bộ nhãn độc lập (`19/20 = 95%`).
  - `31f07a6`: `cp5(chi_so): complete E1 metrics, 10 trace_id events, and cross-check` (`report/team/chi_so.md`).
  - `d746294` & `ff76670`: `cp4-e1(lab13): add statsmodels power check at MDE 0.06 and E1 metrics` + merge đồng bộ `origin/main` (`src/lab13.py`).
- **Kết quả chạy `.\.venv\Scripts\python.exe lab13.py` trong `src/` trên máy cá nhân:**
  - A1: `Ba phép thử đáp án biết trước: ĐẠT` (`1.20 · 1.25 · 1.25`).
  - A2–B4: `cps = 4.472 đ` (`simulated`, `16,3×` hoá đơn `274,7 đ`), `978` việc thành công, cả hệ thống `5.865 đ` (`0,49×`), phạm vi `noi_dia + hang_nang` cộng cố định `4.599 đ` (`0,38×`), B3 tối ưu hệ thống ở 2 lần (`6.901.220 đ`), B4 hòa vốn xem lại `≤ 4,8–5,1` phút (`simulated`).
  - D1 & an toàn hiện tại: `a) 1.251`, `b) 3.103` (`42` NV/nhóm > `40`), `c) 1.000`, `d) 300`, `e) m ≥ 299` (`859`/nhóm, `DE = 6,96`); `statsmodels`: `1.250` và `858`, `power` ở `n = 859` khi tác động thật `0,05` = `0.64 (0.6417)`; `mo_lai_trong_7_ngay` = `4.25%` (toàn bộ) và `3.97%` (phạm vi pilot).
  - E1: Chính `994/1200 = 82.83%`, Dùng `48/177 = 27.12%`, An toàn `51/1200 = 4.25%` (phạm vi `39/982 = 3.97%`).

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Công cụ:** Trợ lý AI (Gemini qua Antigravity IDE).
- **Dùng vào việc gì:** Giải thích định nghĩa và ranh giới phân loại 5 loại lỗi Google PAIR theo nguyên nhân gốc; gợi ý cấu trúc code đối chiếu `statsmodels` (`NormalIndPower`, `proportion_effectsize`) và hàm `in_nhiem_vu_e1` trong `src/lab13.py`; hỗ trợ định dạng markdown, xử lý merge conflict Git và chạy lệnh kiểm tra checklist (`yaml.safe_load`, quét dấu `?`, nhãn `simulated`, quét từ khóa cấm).
- **Cách tự kiểm tra:** Tự đọc 20 ca lỗi và tự chọn độc lập 20 nhãn trước khi so với Phước Anh (không dùng AI gắn thay hay sửa bộ nhãn sau khi so, tuân thủ `RULES.md`); tự chạy `.\.venv\Scripts\python.exe lab13.py` kiểm chứng toàn bộ số liệu A, B, D, E1 trên `logix_runs.csv` và `logix_requests.csv` (`keep_default_na=False`); đối chiếu từng chỉ số, danh sách event có `trace_id` và nhãn `simulated` trong `chi_so.md` và `bang_loi.md` với quy định của đề bài.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ cả hai phần việc được giao (Người gắn nhãn 1 ở CP3 và đổi vai Người viết code ở CP4–E1 trên máy thứ hai), phối hợp đồng bộ Git sạch sẽ với các thành viên trước mốc Gate 2a lúc 17:00.
- Bài học chính: gắn nhãn lỗi cần phân biệt rõ nguyên nhân gốc giữa `Hệ thống`, `Ngữ cảnh` và `Ngầm`; khi lập kế hoạch pilot phải kiểm tra cả dữ liệu nền (`mo_lai_trong_7_ngay = 4,25%`) và phần đánh đổi `power` (`0,64`) nếu nới `MDE` từ `5` lên `6` điểm.
