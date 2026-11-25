# Team

## Thông tin nhóm

- Tên nhóm: Delta
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Delta-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/liliustwocout/K5-L3B-DAY13-Delta-LaunchEconomics` · nhánh `main` · commit chốt: *(cập nhật sau phiên duyệt chéo 17:00)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lê Phạm Thành Đạt | 2A202604027 | datpltn205@gmail.com | liliustwocout | Người viết code (Trưởng nhóm) |
|   2 | Trần Đức Duy | 2A202604071 | tran85122@gmail.com | tran85122-afk | Người gắn nhãn 1 |
|   3 | Bùi Phước Anh | 2A202604102 | cuubui2004@gmail.com | Cuubeo | Người gắn nhãn 2, kiêm giữ hồ sơ |
|   4 | Lê Bá Nguyên | 2A202604100 | nguyenbropmt@gmail.com | lbNGuyen06 | Người kiểm số |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## LePhamThanhDat-2A202604027

### Phần việc phụ trách

- Trưởng nhóm · **Người viết code (CP1–CP2)**: khởi tạo repo nhóm, môi trường `.venv`, viết và chạy `src/lab13.py` (nhiệm vụ A, B) và hoàn thiện `report/team/bang_chi_phi.md`; điều phối đổi vai code sau giải lao và rà soát checklist toàn repo trước Gate 2a.

### Đóng góp cụ thể

- Thiết lập repo nhóm `K5-L3B-DAY13-Delta-LaunchEconomics`, môi trường Python `.venv` trong `src/`, cấu hình `TEAM.md` và khởi tạo 4 file báo cáo cá nhân trong `report/team/`.
- Triển khai A1 (3/3 phép thử biết trước ĐẠT), hàm `mo_hinh(...)` và toàn bộ bảng/trả lời CP1–CP2 (A1–A4, B1–B4) trong `src/lab13.py` và `report/team/bang_chi_phi.md` có nhãn `simulated`.
- Kéo và kiểm tra chéo các commit CP3–CP5, chạy kiểm chứng lại `src/lab13.py`, `yaml.safe_load` cho `pilot_plan.yaml` và rà soát không còn dấu `?` hay từ khóa cấm.

### Bằng chứng

- Commits: `5f7f467` (setup nhóm & báo cáo cá nhân), `9f4f15f` (`src/lab13.py` CP1–CP2 & `report/team/bang_chi_phi.md`).
- Kết quả chạy `src/lab13.py`: `Ba phép thử đáp án biết trước: ĐẠT`; A2 = `4.472 đ` (`simulated`, `16,3×` hoá đơn); A4 = `4.599 đ` (`0,38×`, `simulated`); B3 tối ưu hệ thống ở 2 lần (`6.901.220 đ`, `simulated`); B4 xem lại 100% = `11.743–12.415 đ` (`0,98–1,03×`, `simulated`).

## TranDucDuy-2A202604071

### Phần việc phụ trách

- **Người gắn nhãn 1** (CP1–CP3) & **Người viết code đổi vai trên máy thứ 2** (CP4–E1): theo dõi điều kiện "Xong khi", gắn nhãn độc lập 20 ca lỗi ở CP3 (`report/team/bang_loi.md`); hoàn thiện bảng E1, 10 event có `trace_id` và kiểm tra chéo (`report/team/chi_so.md`); chạy `src/lab13.py` trên máy thứ hai, bổ sung kiểm chứng `statsmodels` (`power` ở `MDE 0,06`) và tính thử 3 chỉ số E1.

### Đóng góp cụ thể

- Thiết lập `.venv` và chạy kiểm chứng lại toàn bộ `src/lab13.py` trên máy thứ hai (đạt `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ bảng A, B, D, E1).
- Gắn nhãn độc lập 20 ca lỗi (cột `Nhãn người 1`) trong `report/team/bang_loi.md` trước khi so nhãn với người gắn nhãn 2 và gộp bảng đồng thuận `19/20 = 95%`.
- Hoàn thiện E1 (3 chỉ số tính thử + 1 chỉ số dùng & 1 chỉ số an toàn tự đề xuất), danh sách 10 event có `trace_id` và mục kiểm tra chéo từng chỉ số trong `report/team/chi_so.md`.
- Bổ sung đối chiếu `statsmodels` (`NormalIndPower`, `power = 0,6417` ở `n = 859` với mức chênh 5 điểm) và hàm `in_nhiem_vu_e1(reqs)` (`82,83%`, `27,12%`, `4,25%` / `3,97%`) trong `src/lab13.py`.

### Bằng chứng

- Báo cáo cá nhân chi tiết: `report/team/2A202604071_TranDucDuy.md`.
- Commits: `7d5b52a` (nhãn độc lập người 1), `ed39e7d` (merge `bang_loi.md`), `31f07a6` (`report/team/chi_so.md` E1 + 10 events + kiểm tra chéo), `d746294` & `ff76670` (`src/lab13.py` kiểm chứng `statsmodels` & E1).

## BuiPhuocAnh-2A202604102

### Phần việc phụ trách

- **Người gắn nhãn 2, kiêm giữ hồ sơ**: gắn nhãn độc lập 20 ca lỗi ở CP3, tổng hợp thống nhất + quy tắc phân biệt + bảng khắc phục 5 ca (`report/team/bang_loi.md`); giữ và hoàn thiện `report/team/ho_so_launch_v0.md`; điền E2 rủi ro kinh tế (`report/team/chi_so.md`); soạn `report/team/group_report.md` và chuẩn bị `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi (nhãn người 2) trước khi so; hoàn thiện cột nhãn thống nhất (`19/20 = 95%`), quy tắc phân biệt ca 8 (`Ngầm`) và bảng khắc phục 5 ca đủ 5 loại PAIR trong `report/team/bang_loi.md`.
- Bổ sung bảng 3 rủi ro kinh tế (E2) trong `report/team/chi_so.md`; hoàn thiện đầy đủ 7 mục + đề xuất **Go có điều kiện** kèm 4 điều kiện, người phụ trách và ngày kiểm tra trong `report/team/ho_so_launch_v0.md`.
- Dựng và điền mục 1–5, 7 trong `report/team/group_report.md`; cập nhật nhóm chấm `Delta (L3B)` trong `report/team/phieu_cham.md` và báo cáo cá nhân `report/team/2A202604102_BuiPhuocAnh.md`.

### Bằng chứng

- Commits: `31fd268`, `53e2b8a`, `a6c47a3`, `5081fef`, `d063b38`, `1f454af`, `7746d43`, `59cb9cd`, `fd010c5`, `5d028f0`.

## LeBaNguyen-2A202604100

### Phần việc phụ trách

- **Người kiểm số & đổi vai code CP4**: đối chiếu số liệu CP1–CP2, cập nhật kết quả kinh tế/rủi ro từ `bang_chi_phi.md` sang `chi_so.md` và `ho_so_launch_v0.md`; triển khai phần tính cỡ mẫu D1 trong `src/lab13.py` và hoàn thiện `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Tính tay kiểm tra độc lập 3 phép thử A1, đối chiếu các số liệu từ trace A2 (CPS `4.472 đ` `simulated`, gấp `16,3×` hoá đơn; làm lại `51,8%`), A3 (loại `quoc_te` và `doi_tac`), A4 (chi phí cố định `4.599 đ`).
- Kiểm tra 9 kịch bản độ nhạy B1, kịch bản đôi B2 (`+46,3%`), chi phí hệ thống B3 (giới hạn 2 lần rẻ nhất: `6.901.220 đ`, `simulated`) và điểm hòa vốn xem lại 100% B4 (`≤ 4,8–5,1` phút, `simulated`).
- Triển khai `co_mau` và `in_nhiem_vu_d` trong `src/lab13.py`, hoàn thiện toàn bộ `report/team/pilot_plan.yaml` (cỡ mẫu D1: `1.251` YC/nhóm; `20` NV/nhóm MDE 6 điểm cần `m ≥ 299` YC/người, power `0,64`; 3 luật dừng đủ 4 vế), cập nhật bảng E2 Rủi ro kinh tế trong `chi_so.md` và mục 6 `ho_so_launch_v0.md`.
- Rà soát toàn bộ nhãn `simulated` và bảo đảm không dùng từ cấm trong hồ sơ.

### Bằng chứng

- Báo cáo cá nhân chi tiết: `report/team/2A202604100_LeBaNguyen.md`.
- Commit `80afbc3` (cập nhật rủi ro kinh tế E2 và các mục chi phí vào hồ sơ launch v0) và commit `553d283` (hoàn thành `pilot_plan.yaml`, code tính cỡ mẫu D1 trong `lab13.py` và mục 6 `ho_so_launch_v0.md`).
- Kết quả chạy `src/lab13.py` trên môi trường cá nhân đạt 100% kết quả kiểm thử.
