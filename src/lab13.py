"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not (0 < p <= 1):
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not (0 < p <= 1):
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    tien_chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()

    token = float(tien_token.sum())
    tool = float(tien_tool.sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return {
        'token': token,
        'tool': tool,
        'chay_lai': float(tien_chay_lai),
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong,
        'hoa_don_moi_yc': (token + tool) / len(reqs),
    }


def in_nhiem_vu_a(runs, reqs):
    """In kết quả Nhiệm vụ A (A1, A2, A3, A4) để kiểm chứng và điền bang_chi_phi.md."""
    print('\n=== A1 · Ba phép thử đáp án biết trước ===')
    print(f'Tối đa 2 lần (p=0.8): {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'Chạy đến đúng (p=0.8): {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'Hệ số chi phí, tối đa 3 lần: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    ket_qua = mo_hinh(runs, reqs)
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:16s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:16s} {gia_tri:>14,.0f}')
    print(f"so_lan_goi_tool  {runs['tool_calls'].sum():>14,.0f}")
    print(f"phut_xem_lai_sim {reqs['phut_xem_lai_simulated'].sum():>14,.0f}")
    print(f"phut_lam_lai_sim {reqs['phut_lam_lai_simulated'].sum():>14,.0f}")
    print(f"gap_hoa_don      {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:>14,.1f}x")
    print(f"ty_trong_xem_lai {ket_qua['xem_lai'] / ket_qua['tong'] * 100:>13,.1f}%")
    print(f"ty_trong_lam_lai {ket_qua['lam_lai'] / ket_qua['tong'] * 100:>13,.1f}%")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'he_thong_moi_yc  {he_thong_moi_yc:>14,.0f} ({he_thong_moi_yc / BASELINE:.2f}x)')

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        ti_le_tc = kq['thanh_cong'] / len(sub) * 100
        chay_tb = sub['so_lan_chay'].mean()
        print(
            f"{loai:10s} | n={len(sub):3d} | tc={ti_le_tc:5.1f}% | "
            f"chay/yc={chay_tb:.2f} | cps={kq['cps']:8,.0f} đ [sim] | {kq['cps'] / BASELINE:.2f}x"
        )

    print('\n--- Tỉ lệ ok theo lần thử (attempt) ---')
    pivot_ok = (
        runs.assign(ok=(runs['status'] == 'ok').astype(int))
        .merge(reqs[['request_id', 'loai']], on='request_id')
        .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
        .loc[['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']]
    )
    print((pivot_ok * 100).round(1).to_string())

    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_mau = kq_pv['thanh_cong'] / len(reqs)
    chi_phi_cd_thang = 40_000_000
    for nhan_kl, tong_yc_thang in [('45.000 yêu cầu/tháng', 45_000), ('Một nửa khối lượng (22.500)', 22_500)]:
        viec_tc_thang = tong_yc_thang * ti_le_tc_mau
        cd_moi_viec = chi_phi_cd_thang / viec_tc_thang
        tong_cps = kq_pv['cps'] + cd_moi_viec
        print(
            f'{nhan_kl:30s} | tc/thang={viec_tc_thang:8,.0f} | '
            f'cd={cd_moi_viec:6,.0f} đ | cps+cd={tong_cps:6,.0f} đ [sim] | {tong_cps / BASELINE:.2f}x'
        )
    return ket_qua


def in_nhiem_vu_b(runs, reqs, goc_a2):
    """In kết quả Nhiệm vụ B (B1, B2, B3, B4) để điền bảng độ nhạy."""
    goc = goc_a2['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    print('\n=== B1 · Đổi từng yếu tố [simulated] ===')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} | {cps:8,.0f} đ | {(cps / goc - 1) * 100:+6.1f}%')

    print('\n=== B2 · Đổi một cặp [simulated] ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f'Token x2 + Xem lại x2        | {cps_cap:8,.0f} đ | {(cps_cap / goc - 1) * 100:+6.1f}%')

    print('\n=== B3 · Chi phí cả hệ thống theo giới hạn chạy lại [simulated] ===')
    for max_k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=max_k)
        khong_tc = len(reqs) - kq['thanh_cong']
        ca_he_thong = kq['tong'] + BASELINE * khong_tc
        print(
            f'Giới hạn {max_k} lần | trợ lý={kq["tong"]:10,.0f} đ | '
            f'không TC={khong_tc:3d} | hệ thống={ca_he_thong:10,.0f} đ | cps={kq["cps"]:6,.0f} đ'
        )

    print('\n=== B4 · Xem lại 100% (noi_dia + hang_nang) [simulated] ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_yc_co_ok = int(runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique())
    so_ca_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    so_tc_pv = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    phi_agent_pv = float(
        (runs_pv['tokens_in'] / 1000.0 * GIA_VAO + runs_pv['tokens_out'] / 1000.0 * GIA_RA).sum()
        + (runs_pv['tool_calls'] * GIA_TOOL).sum()
    )
    tien_xem_100 = so_yc_co_ok * 5 * LUONG_PHUT
    phut_lam_lai_tb_data = float(pham_vi.loc[pham_vi['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())
    phut_lam_lai_tb_all = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())
    for nhan_ll, phut_ll in [('Đề bài (9 phút/ca)', 9.0), ('Dữ liệu simulated (toàn bộ lam_lai)', phut_lam_lai_tb_all)]:
        tien_ll = so_ca_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = phi_agent_pv + tien_xem_100 + tien_ll
        cps_b4 = tong_b4 / so_tc_pv
        hoa_von_phut = (so_tc_pv * BASELINE - phi_agent_pv - tien_ll) / (so_yc_co_ok * LUONG_PHUT)
        print(
            f'{nhan_ll:36s} | ok={so_yc_co_ok}, ll={so_ca_lam_lai}, tc={so_tc_pv} | '
            f'tong={tong_b4:10,.0f} đ | cps={cps_b4:6,.0f} đ ({cps_b4 / BASELINE:.2f}x) | '
            f'hòa vốn xem lại <= {hoa_von_phut:.1f} phút'
        )
    print(f'Trung bình phut_lam_lai_simulated trong phạm vi: {phut_lam_lai_tb_data:.2f}; toàn bộ: {phut_lam_lai_tb_all:.2f}')


from statistics import NormalDist


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Tính cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập (z-test hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    tu_so = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    mau_so = (p2 - p1) ** 2
    return math.ceil(tu_so / mau_so)


def in_nhiem_vu_d(reqs):
    """In kết quả tính cỡ mẫu và kiểm tra điều kiện Nhiệm vụ D (D1)."""
    print('\n=== D1 · Cỡ mẫu và hệ số thiết kế ===')
    baseline = 0.70
    alpha = 0.05
    power = 0.80
    icc = 0.02

    # a) Chia theo yêu cầu (+5 điểm)
    n_a = co_mau(baseline, baseline + 0.05, alpha=alpha, power=power)
    print(f'a) Chia theo yêu cầu (MDE=0.05): {n_a} yêu cầu mỗi nhóm')

    # b) Theo nhân viên, m = 75
    m_b = 75
    de_b = 1 + (m_b - 1) * icc
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / m_b)
    print(f'b) Theo nhân viên, m=75: DE={de_b:.2f} -> {n_b} YC/nhóm ({nv_b} NV/nhóm, tổng {nv_b * 2} > 40: KHÔNG ĐỦ)')

    # c) 20 nhân viên mỗi nhóm
    n_eff_max_c = 20 / icc
    print(f'c) 20 nhân viên mỗi nhóm: tối đa c/ICC = {n_eff_max_c:.0f} hiệu dụng (< {n_a} cho MDE 0.05: KHÔNG ĐẠT)')

    # d) 6 depot mỗi nhóm
    n_eff_max_d = 6 / icc
    print(f'd) 6 depot mỗi nhóm: tối đa c/ICC = {n_eff_max_d:.0f} hiệu dụng (quá ít cụm: KHÔNG ĐẠT)')

    # e) Mức chênh 6 điểm, 20 nhân viên mỗi nhóm
    mde_e = 0.06
    n_e = co_mau(baseline, baseline + mde_e, alpha=alpha, power=power)
    m_req_e = (0.98 * n_e) / (20 - icc * n_e)
    m_e = math.ceil(m_req_e)
    de_e = 1 + (m_e - 1) * icc
    print(
        f'e) Mức chênh 6 điểm ({n_e}/nhóm), 20 NV/nhóm: m >= {m_e} YC/NV (DE={de_e:.2f}) -> ĐẠT VỚI MDE 6 ĐIỂM'
    )

    ti_le_mo_lai = float(reqs['mo_lai_trong_7_ngay'].mean()) * 100
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ti_le_mo_lai_pv = float(pv['mo_lai_trong_7_ngay'].mean()) * 100
    print(f'\nTỉ lệ mo_lai_trong_7_ngay hiện tại: toàn bộ {ti_le_mo_lai:.2f}%, phạm vi noi_dia+hang_nang {ti_le_mo_lai_pv:.2f}%')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua_a2 = in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs, ket_qua_a2)
    in_nhiem_vu_d(reqs)
