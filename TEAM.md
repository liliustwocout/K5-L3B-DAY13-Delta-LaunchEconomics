# Team

## Thông tin nhóm

- Tên nhóm: Delta
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Delta-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/liliustwocout/K5-L3B-DAY13-Delta-LaunchEconomics` · nhánh `main` · commit chốt: *(cập nhật khi chốt nộp)*

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

- Trưởng nhóm · **Người viết code**: khởi tạo repo nhóm, môi trường `.venv`, viết và chạy `src/lab13.py` (nhiệm vụ A, B, D1); tham gia hoàn thiện `report/team/pilot_plan.yaml` và `report/team/chi_so.md`.

### Đóng góp cụ thể

- *(Cập nhật sau khi hoàn thành các checkpoint)*

### Bằng chứng

- *(Cập nhật commit, output chạy `src/lab13.py` và các file liên quan)*

## TranDucDuy-2A202604071

### Phần việc phụ trách

- **Người gắn nhãn 1**: đọc đề, theo dõi điều kiện "Xong khi" ở từng checkpoint; gắn nhãn độc lập 20 ca lỗi ở CP3 (`report/team/bang_loi.md`); tham gia thống nhất quy tắc phân biệt, bảng khắc phục và rà soát chéo.

### Đóng góp cụ thể

- *(Cập nhật sau khi hoàn thành các checkpoint)*

### Bằng chứng

- *(Cập nhật commit, bảng nhãn độc lập CP3 và các mục liên quan)*

## BuiPhuocAnh-2A202604102

### Phần việc phụ trách

- **Người gắn nhãn 2, kiêm giữ hồ sơ**: điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn độc lập 20 ca lỗi ở CP3 (`report/team/bang_loi.md`); cùng nhóm hoàn thiện `report/team/chi_so.md`, `report/team/phieu_cham.md` và `report/team/group_report.md`.

### Đóng góp cụ thể

- *(Cập nhật sau khi hoàn thành các checkpoint)*

### Bằng chứng

- *(Cập nhật commit, bảng nhãn độc lập CP3 và file hồ sơ)*

## LeBaNguyen-2A202604100

### Phần việc phụ trách

- **Người kiểm số**: tính tay đối chiếu số liệu từ trace và công thức, điền `report/team/bang_chi_phi.md` (nhiệm vụ A, B); kiểm tra cỡ mẫu nhiệm vụ D và tham gia đổi vai viết code/kiểm tra chéo trên máy khác.

### Đóng góp cụ thể

- Tính tay kiểm tra độc lập 3 phép thử A1, đối chiếu các số liệu từ trace A2 (CPS 4.472 đ `simulated`, gấp 16,3× hoá đơn; làm lại 51,8%), A3 (loại `quoc_te` và `doi_tac`), A4 (chi phí cố định 4.599 đ).
- Kiểm tra 9 kịch bản độ nhạy B1, kịch bản đôi B2 (+46,3%), chi phí hệ thống B3 (giới hạn 2 lần rẻ nhất: 6.901.220 đ) và điểm hòa vốn xem lại 100% B4 (≤ 4,8–5,1 phút).
- Kiểm tra cỡ mẫu D1 (1.251 YC/nhóm; 20 NV/nhóm MDE 6 điểm cần m ≥ 299 YC/người, power 0,64); hoàn thiện bảng E2 Rủi ro kinh tế trong `chi_so.md`; rà soát toàn bộ nhãn `simulated` và cam kết không dùng từ "production".

### Bằng chứng

- Báo cáo cá nhân chi tiết: `report/team/2A202604100_LeBaNguyen.md`.
- Commit `80afbc3` (cập nhật rủi ro kinh tế E2 và các mục chi phí vào hồ sơ launch v0) và commit `553d283` (hoàn thành `pilot_plan.yaml` và code tính cỡ mẫu D1 trong `lab13.py`).
- Kết quả chạy `src/lab13.py` trên môi trường cá nhân đạt 100% kết quả kiểm thử.
