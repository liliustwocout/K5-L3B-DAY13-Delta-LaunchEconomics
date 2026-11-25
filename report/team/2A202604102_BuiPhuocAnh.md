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

- CP1–CP2: đối chiếu số trong `ho_so_launch_v0.md` với `bang_chi_phi.md` (mục 1, 2, 3, 7 khớp); bổ sung nhãn `simulated` cho các con số giả lập, trạng thái và người phụ trách mục 4–6.
- CP3: tự gắn nhãn độc lập 20 ca lỗi (nhãn người 2), commit trước khi so với nhãn người 1.
- Dựng khung `group_report.md` (mục 2–4 có con số chính từ CP1–CP2); điền nhóm chấm trong `phieu_cham.md`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `31fd268`: hồ sơ launch v0, bổ sung nhãn `simulated`, trạng thái, người phụ trách.
- Commit `53e2b8a` (15:29): bộ nhãn độc lập người 2 trong `bang_loi.md`, đẩy lên trước khi so nhãn.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code (trong VS Code): lập quy trình làm việc theo vai, trích 20 ca lỗi từ file docx, thao tác Git (pull, commit, push), định dạng bảng markdown, đối chiếu số giữa các file.
- Không dùng AI để gắn nhãn: 20 nhãn trong `bang_loi.md` là do tôi tự gắn (đúng `RULES.md`); AI chỉ giải thích định nghĩa 5 loại lỗi.
- Tự kiểm tra: so từng con số trong hồ sơ với `bang_chi_phi.md` do người kiểm số chốt.

## 6. Tự đánh giá

- *(Cập nhật khi hoàn tất bài làm)*
