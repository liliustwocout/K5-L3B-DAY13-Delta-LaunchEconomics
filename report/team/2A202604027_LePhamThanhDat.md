# Báo cáo cá nhân — LePhamThanhDat-2A202604027

## 1. Thông tin thành viên

- Họ tên: Lê Phạm Thành Đạt
- MSSV: 2A202604027
- Email: datpltn205@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code (Trưởng nhóm)

## 2. Phần việc phụ trách

- Thiết lập repo nhóm `K5-L3B-DAY13-Delta-LaunchEconomics`, môi trường Python `.venv` trong `src/` và cấu hình thông tin nhóm, phân công luồng công việc (`TEAM.md`).
- Triển khai phần code CP1–CP2 trong `src/lab13.py` (hàm A1, `mo_hinh` cho A2–A4 và B1–B4) và hoàn thiện bảng số liệu `report/team/bang_chi_phi.md`.
- Điều phối luồng làm việc, chuyển giao phần code CP4–E1 sang thành viên khác chạy trên máy thứ hai, kiểm tra checklist toàn repo trước Gate 2a và chuẩn bị bảo vệ hồ sơ trước hội đồng.

## 3. Đóng góp cụ thể

- **Bước chuẩn bị (setup):** Đồng bộ nhánh `main` với `upstream`, tạo `.venv` (Python 3.11.9) và cài đặt `pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`; điền thông tin 4 thành viên vào `TEAM.md` và khởi tạo sẵn 4 file báo cáo cá nhân trong `report/team/` (giữ nguyên file mẫu `MSSV_HoTen.md`).
- **CP1 (Nhiệm vụ A):** Cài đặt 3 hàm kinh tế chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 3/3 phép thử biết trước (`1,20 · 1,25 · 1,25`). Viết `mo_hinh` và `in_nhiem_vu_a` tính chi phí từ trace (tử số gồm mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `thanh_cong`), tách theo 4 loại yêu cầu kèm tỉ lệ `ok` theo từng lần thử, và tính tác động chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang`.
- **CP2 (Nhiệm vụ B):** Viết `in_nhiem_vu_b` chạy 9 kịch bản độ nhạy B1, kịch bản cặp `Token x2 + Xem lại x2`, tính chi phí cả hệ thống (cộng `12.000 đ × số ca không thành công`) cho giới hạn 1/2/3 lần chạy, và kịch bản xem lại 100% ở cả hai mức thời gian làm lại (`9` phút theo đề và `15,3` phút theo dữ liệu `phut_lam_lai_simulated`). Điền đầy đủ bảng A1–A4, B1–B4 và câu trả lời ≤ 3 dòng có nhãn `simulated` vào `report/team/bang_chi_phi.md`.
- **Rà soát trước Gate 2a:** Kéo và kiểm tra đồng bộ commit của các thành viên, chạy lại `src/lab13.py` sau phần bổ sung CP4/E1, kiểm tra `yaml.safe_load` cho `report/team/pilot_plan.yaml`, kiểm tra không còn `?` và không có từ cấm trong `report/team/`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `5f7f467`: thiết lập `TEAM.md`, tiêu đề hồ sơ và khởi tạo 4 file báo cáo cá nhân trong `report/team/`.
- Commit `9f4f15f`: triển khai `src/lab13.py` (A1–A4, B1–B4) và hoàn thiện `report/team/bang_chi_phi.md`.
- Kết quả chạy `src/lab13.py`:
  - A1: `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`).
  - A2: `4.472 đ/việc thành công` (`simulated`, gấp `16,3×` hoá đơn `274,7 đ`); làm lại chiếm `51,8%`, xem lại `40,7%`; chi phí cả hệ thống `5.865 đ/yêu cầu` (`0,49×`, `simulated`).
  - A3–A4: loại `quoc_te` (`22.515 đ = 1,88×`, thành công `27,3%`, `ok` giảm `30,0% → 11,4% → 2,2%`) và `doi_tac` (`0,85×`); phạm vi `noi_dia + hang_nang` cộng cố định 40 triệu/tháng đạt `4.599 đ` (`0,38×` ở 45.000 YC/tháng) và `5.784 đ` (`0,48×` ở nửa khối lượng, `simulated`).
  - B1–B4: top 3 yếu tố nhạy nhất (làm lại `+51,8%`, xem lại `+40,7%`, lương `+23,1%`, `simulated`); giới hạn 2 lần rẻ nhất hệ thống (`6.901.220 đ`, `simulated`); xem lại 100% tốn `11.743–12.415 đ` (`0,98–1,03×`, hòa vốn `≤ 4,8–5,1` phút, `simulated`).

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Công cụ:** Trợ lý AI (Gemini qua Antigravity IDE).
- **Dùng vào việc gì:** Tóm tắt yêu cầu đề bài/rubric, thiết lập `.venv` và kiểm tra Git, gợi ý cấu trúc code A1–A4 và B1–B4 trong `src/lab13.py`, trình bày bảng trong `report/team/bang_chi_phi.md` và chạy các lệnh rà soát checklist (`yaml.safe_load`, quét dấu `?` và từ khóa cấm).
- **Cách tự kiểm tra:** Chạy trực tiếp `src/lab13.py` kiểm chứng đạt cả 3 phép thử A1; đối chiếu từng khoản mục A2–A4 và B1–B4 với công thức trong `docs/du_lieu_va_cong_thuc.md` (đọc CSV có `keep_default_na=False`, kiểm tra tính tuyến tính của kịch bản giảm một nửa = −1/2 mức tăng gấp đôi); rà soát diff từng commit khi pull bài của các thành viên trước khi duyệt chéo.

## 6. Tự đánh giá

- Hoàn thành đúng mốc CP1–CP2 theo luồng, phân tách file rõ ràng giúp cả nhóm phối hợp nhanh và hoàn thiện đầy đủ hồ sơ trước mốc 17:00.
- Điểm cần lưu ý thêm: luôn đồng bộ kỹ người giữ từng file trước khi sửa để tránh conflict nhỏ ở `ho_so_launch_v0.md`, và sau phiên duyệt chéo Gate 2a sẽ cập nhật ngay kết quả chấm hội đồng vào báo cáo nhóm.
