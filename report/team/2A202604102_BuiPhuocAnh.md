# Báo cáo cá nhân — BuiPhuocAnh-2A202604102

## 1. Thông tin thành viên

- Họ tên: Bùi Phước Anh
- MSSV: 2A202604102
- Email: cuubui2004@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- **Giữ hồ sơ launch v0** (`report/team/ho_so_launch_v0.md`): điền dần từ CP1 theo số chốt Nguyên (kiểm số) gửi sang; đủ bảy mục, mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập) và người phụ trách là một vai trò; chốt dòng đề xuất và gửi nhóm hội đồng trước 17:00.
- **Gắn nhãn 2 ở CP3** (`report/team/bang_loi.md`): tự gắn nhãn độc lập 20 ca lỗi trong 8 phút, không trao đổi với Duy (gắn nhãn 1); sau đó ghép hai bộ nhãn, tính tỉ lệ đồng thuận, ghi quy tắc phân biệt cho ca không trùng và cùng Duy điền bảng khắc phục 5 ca.
- **Duyệt chéo Gate 2a** (`report/team/phieu_cham.md`): phụ trách phiếu chấm khi nhóm Delta làm hội đồng cho nhóm n + 1, ghi quyết định, lý do có số và câu hỏi cho đội trình.
- **Khung báo cáo nhóm** (`report/team/group_report.md`): dựng khung, tổng hợp con số chính và đề xuất cuối từ hồ sơ.
- Kiểm tra trước khi nộp: mọi số từ cột `_simulated` có nhãn `simulated`, không có từ cấm theo quy tắc 5 của README.

## 3. Đóng góp cụ thể

- **Hồ sơ launch v0** (`ho_so_launch_v0.md`): điền đủ bảy mục. Mục 1, 2, 3, 7 đối chiếu với số người kiểm số chốt trong `bang_chi_phi.md` (khớp) và gắn nhãn `simulated`; mục 4 lấy từ `chi_so.md` (82,83% / 27,12% / 4,25%, đã tính lại từ `logix_requests.csv` và khớp); mục 5 từ `bang_loi.md` (19/20 = 95%); viết dòng đề xuất **Go có điều kiện** với 4 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra. Push lúc 16:35, trước hạn 17:00.
- **Gắn nhãn 2 ở CP3** (`bang_loi.md`): tự gắn nhãn độc lập 20 ca, push lúc 15:29 trước khi so với người gắn nhãn 1; đồng thuận 19/20 = 95%; viết quy tắc phân biệt cho ca 8 (Ngầm); cùng người gắn nhãn 1 chốt bảng khắc phục 5 ca, tôi đề xuất ca 1, 7, 3.
- **Báo cáo nhóm** (`group_report.md`): dựng khung và điền mục 2–5, 7 từ các file hồ sơ.
- **Phiếu chấm** (`phieu_cham.md`): điền nhóm chấm; chấm nhóm n + 1 trong buổi duyệt chéo.
- Xử lý conflict Git khi người viết code và tôi cùng sửa `ho_so_launch_v0.md` (mục 5 và mục 6), giữ được cả hai phần.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

| Commit | Giờ | Nội dung |
| --- | --- | --- |
| `31fd268` | 15:12 | Hồ sơ: nhãn `simulated`, trạng thái, người phụ trách mục 4–6 |
| `53e2b8a` | 15:29 | Bộ nhãn độc lập người 2 (trước khi so nhãn) |
| `a6c47a3` | 15:38 | Khung `group_report.md`, nhóm chấm trong `phieu_cham.md` |
| `5081fef` | 16:05 | Nhãn thống nhất 20 ca, quy tắc ca 8 |
| `d063b38`, `1f454af` | 16:12, 16:15 | Bảng khắc phục 5 ca, ngưỡng phát hiện, người phụ trách |
| `7746d43`, `59cb9cd` | 16:23, 16:26 | Hồ sơ mục 5 và mục 4 |
| `fd010c5` | 16:35 | Đề xuất Go có điều kiện |
| `5d028f0` | 16:38 | `group_report.md` mục 3–5, 7 |

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Claude Code (trong VS Code):** lập quy trình làm việc theo vai, trích 20 ca lỗi từ file docx, thao tác Git (pull, commit, push, gộp conflict), định dạng bảng markdown, đối chiếu số giữa các file, soát nhãn `simulated` và từ cấm.
- **Không dùng AI để gắn nhãn:** AI từ chối gắn nhãn thay (đúng `RULES.md`), chỉ giải thích định nghĩa 5 loại lỗi; 20 nhãn người 2 là do tôi tự gắn. Quy tắc ca 8 do tôi viết.
- **Phần AI gợi ý, nhóm duyệt rồi dùng:** các ngưỡng phát hiện trong bảng khắc phục (2%, 5%, 3%, ≥ 1 tin, ≥ 10 đơn), cách diễn đạt 4 điều kiện của đề xuất và các ngày kiểm tra (lấy mốc bắt đầu pilot 2026-12-07, trước `decision_date` 2027-01-05). Đây là giả định, không tính từ dữ liệu.
- **Tự kiểm tra:** so từng con số trong hồ sơ với `bang_chi_phi.md` và `chi_so.md`; tính lại 3 chỉ số E1 trực tiếp từ `logix_requests.csv` (994/1.200, 48/177, 51/1.200); tính tay power ở mức 5 điểm: h ≈ 0,112, Φ(0,112 × √(859/2) − 1,96) ≈ 0,64.

## 6. Tự đánh giá

- Làm tốt: hồ sơ đủ bảy mục và push trước 17:00; bộ nhãn độc lập được commit trước khi so, đồng thuận 95%; mọi số giả lập có nhãn `simulated`.
- Cần cải thiện: lúc đầu hai người cùng sửa `ho_so_launch_v0.md` gây trùng và conflict, lẽ ra phải thống nhất ngay từ đầu chỉ người giữ hồ sơ sửa file này; người phụ trách trong bảng khắc phục phải sửa nhiều lần do chưa đọc kỹ yêu cầu "một vai trò có quyền quyết định" trong `RUBRIC.md`.
- Điều học được: chi phí thật mỗi việc thành công (4.472 đ) gấp 16,3 lần hoá đơn token, vì giờ nhân viên chiếm 92,5%; gắn nhãn lỗi theo nguyên nhân gốc và theo việc lỗi đã lộ ra hay chưa (Hệ thống khác Ngầm).
