"""
BỘ KIỂM THỬ ĐỘC LẬP CHO ĐỀ TÀI DT001 - THUẬT TOÁN EUCLID VÀ ĐẾM VÒNG LẶP
Sinh viên: Huỳnh Nguyễn Tiến Anh - MSSV: N24DCDT001 - Lớp: D24CQDT01-N
INT13185 - Nhóm 03

Bộ kiểm thử gồm ít nhất 12 ca độc lập có mã định danh (TC01 - TC14),
được chia thành các nhóm theo yêu cầu của Rubric và Hướng dẫn sinh viên:
- TC01 - TC02: Hai ví dụ trên phiếu (A01, A02)
- TC03 - TC04: Hai ca tự thiết kế độc lập (A03, A04)
- TC05 - TC07: Ba ca biên hợp lệ (A05, A06, A07)
- TC08 - TC09: Ca dữ liệu vi phạm hợp đồng (A08)
- TC10 - TC11: Các ca khảo sát quy mô số lớn và dãy Fibonacci
- TC12 - TC14: Kiểm tra tính bất biến và tính năng mở rộng (UCLN mảng)
"""

import sys
import os
import math

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from euclid import ucln, dem_vong, lan_vet_ucln, ucln_mang, kiem_tra_dau_vao


class TestRunner:
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.total_asserts = 0
        self.passed_asserts = 0

    def check(self, condition: bool, msg: str = ""):
        self.total_asserts += 1
        if condition:
            self.passed_asserts += 1
        else:
            raise AssertionError(f"Kiểm tra thất bại: {msg}")

    def run_case(self, tc_id: str, desc: str, func):
        self.total_tests += 1
        try:
            func(self)
            self.passed_tests += 1
            print(f"[{tc_id}] PASS | {desc}")
        except Exception as e:
            self.failed_tests += 1
            print(f"[{tc_id}] FAIL | {desc} -> Lỗi: {e}")


def main():
    runner = TestRunner()
    print("=" * 78)
    print("CHẠY BỘ KIỂM THỬ TỰ ĐỘNG - ĐỀ TÀI DT001 (EUCLID VÀ ĐẾM VÒNG LẶP)")
    print("Sinh viên: Huỳnh Nguyễn Tiến Anh - MSSV: N24DCDT001")
    print("=" * 78)

    # TC01: Ví dụ 1 trên phiếu (Mã ảnh A01)
    def tc01(r):
        a, b = 48, 18
        res = lan_vet_ucln(a, b)
        r.check(res['gcd'] == 6, "UCLN phải bằng 6")
        r.check(res['so_vong'] == 3, "Số vòng lặp phải bằng 3")
        r.check(res['cac_so_du'] == [12, 6, 0], "Dãy số dư phải là [12, 6, 0]")
    runner.run_case("TC01 (A01)", "Ví dụ 1 phiếu: a=48, b=18 -> gcd=6, so_vong=3, du=[12,6,0]", tc01)

    # TC02: Ví dụ 2 trên phiếu (Mã ảnh A02)
    def tc02(r):
        a, b = 89, 55
        res = lan_vet_ucln(a, b)
        r.check(res['gcd'] == 1, "UCLN hai số Fibonacci liên tiếp phải bằng 1")
        r.check(res['so_vong'] == 9, "Số vòng lặp phải bằng 9")
    runner.run_case("TC02 (A02)", "Ví dụ 2 phiếu: a=89, b=55 -> gcd=1, so_vong=9 (Fibonacci)", tc02)

    # TC03: Tự thiết kế 1 (Mã ảnh A03)
    def tc03(r):
        a, b = 252, 105
        # 252 = 21 * 12, 105 = 21 * 5
        g = ucln(a, b)
        v = dem_vong(a, b)
        r.check(g == 21, "UCLN của 252 và 105 phải là 21")
        r.check(v == 3, f"Số vòng lặp thực tế {v} phải bằng 3 (252%105=42, 105%42=21, 42%21=0)")
    runner.run_case("TC03 (A03)", "Tự thiết kế 1: a=252, b=105 -> gcd=21, so_vong=3", tc03)

    # TC04: Tự thiết kế 2 (Mã ảnh A04)
    def tc04(r):
        a, b = 1000, 350
        # 1000 % 350 = 300; 350 % 300 = 50; 300 % 50 = 0 -> gcd=50, 3 vòng
        g = ucln(a, b)
        v = dem_vong(a, b)
        r.check(g == 50, "UCLN của 1000 và 350 phải là 50")
        r.check(v == 3, "Số vòng lặp phải là 3")
    runner.run_case("TC04 (A04)", "Tự thiết kế 2: a=1000, b=350 -> gcd=50, so_vong=3", tc04)

    # TC05: Ca biên 1 - Hai số bằng nhau (Mã ảnh A05)
    def tc05(r):
        a, b = 12, 12
        g = ucln(a, b)
        v = dem_vong(a, b)
        r.check(g == 12, "UCLN của 12 và 12 phải bằng 12")
        r.check(v == 1, "Số vòng lặp khi a=b phải bằng 1 (12 % 12 = 0)")
    runner.run_case("TC05 (A05)", "Ca biên 1: Hai số bằng nhau a=12, b=12 -> gcd=12, so_vong=1", tc05)

    # TC06: Ca biên 2 - Số chia bằng 1 (Mã ảnh A06)
    def tc06(r):
        a, b = 35, 1
        g = ucln(a, b)
        v = dem_vong(a, b)
        r.check(g == 1, "UCLN của 35 và 1 phải bằng 1")
        r.check(v == 1, "Số vòng lặp khi b=1 phải bằng 1")
    runner.run_case("TC06 (A06)", "Ca biên 2: Số chia b=1: a=35, b=1 -> gcd=1, so_vong=1", tc06)

    # TC07: Ca biên 3 - Số chia bằng 0 (Mã ảnh A07)
    def tc07(r):
        a, b = 9, 0
        g = ucln(a, b)
        v = dem_vong(a, b)
        r.check(g == 9, "UCLN khi b=0 phải trả về chính a=9")
        r.check(v == 0, "Số vòng lặp khi b=0 phải bằng 0 (dừng ngay, không chia)")
    runner.run_case("TC07 (A07)", "Ca biên 3: Số chia b=0: a=9, b=0 -> gcd=9, so_vong=0 (dừng ngay)", tc07)

    # TC08: Ca input sai 1 - Số âm (Mã ảnh A08)
    def tc08(r):
        da_bat_loi = False
        try:
            kiem_tra_dau_vao(-15, 10)
        except ValueError as e:
            da_bat_loi = True
            r.check("không âm" in str(e), "Thông báo lỗi phải nêu rõ số không âm")
        r.check(da_bat_loi, "Validator phải từ chối số âm")
    runner.run_case("TC08 (A08a)", "Input sai 1: a=-15, b=10 bị validator từ chối ném ValueError", tc08)

    # TC09: Ca input sai 2 - Cả hai số bằng 0 hoặc sai kiểu dữ liệu (Mã ảnh A08b)
    def tc09(r):
        da_bat_00 = False
        try:
            kiem_tra_dau_vao(0, 0)
        except ValueError:
            da_bat_00 = True
        r.check(da_bat_00, "Validator phải từ chối khi a=0 và b=0")

        da_bat_type = False
        try:
            kiem_tra_dau_vao("48", 18)
        except TypeError:
            da_bat_type = True
        r.check(da_bat_type, "Validator phải từ chối kiểu chuỗi")
    runner.run_case("TC09 (A08b)", "Input sai 2: a=0, b=0 và input chuỗi bị từ chối", tc09)

    # TC10: Khảo sát cặp Fibonacci kế tiếp F12/F11 (144, 89)
    def tc10(r):
        a, b = 144, 89
        g = ucln(a, b)
        v = dem_vong(a, b)
        r.check(g == 1, "UCLN(144, 89) = 1")
        r.check(v == 10, "Số vòng lặp của F12 và F11 phải là 10 (đúng định lý Lamé)")
    runner.run_case("TC10", "Fibonacci lớn hơn: a=144, b=89 -> gcd=1, so_vong=10", tc10)

    # TC11: Số nguyên quy mô lớn (10^9)
    def tc11(r):
        # Hai số nguyên tố cùng nhau lớn
        a = 1_000_000_000
        b = 999_999_937 # số nguyên tố
        g = ucln(a, b)
        v = dem_vong(a, b)
        r.check(g == 1, "UCLN phải bằng 1")
        r.check(v <= 25, "Số vòng lặp không được vượt quá 5 * log10(b)")
    runner.run_case("TC11", "Quy mô lớn: a=10^9, b=999999937 -> chạy tức thời, gcd=1", tc11)

    # TC12: Kiểm tra tính đúng của bất biến lặp gcd(a, b) = gcd(b, a % b)
    def tc12(r):
        a, b = 360, 144
        expected_gcd = math.gcd(a, b) # Dùng hàm thư viện chuẩn làm Oracle đối chứng độc lập
        res = lan_vet_ucln(a, b)
        r.check(res['gcd'] == expected_gcd, "UCLN tính được phải khớp với math.gcd chuẩn")
        for buoc in res['cac_buoc']:
            cur_a = buoc['a']
            cur_b = buoc['b']
            r.check(math.gcd(cur_a, cur_b) == expected_gcd, f"Bất biến gcd({cur_a}, {cur_b}) phải giữ nguyên")
    runner.run_case("TC12", "Kiểm tra tính đúng bất biến: gcd(a, b) = gcd(b, a % b) qua mọi bước", tc12)

    # TC13: Số có 6 chữ số theo yêu cầu phiếu phân tích
    def tc13(r):
        a, b = 999999, 123456
        # 999999 = 3 * 333333; 123456 = 3 * 41152; gcd = 3
        g = ucln(a, b)
        r.check(g == 3, "UCLN của 999999 và 123456 phải bằng 3")
        r.check(g == math.gcd(a, b), "Khớp với đối chứng math.gcd")
    runner.run_case("TC13", "Khảo sát số 6 chữ số: a=999999, b=123456 -> gcd=3", tc13)

    # TC14: Yêu cầu mở rộng - Tính UCLN của mảng số nguyên
    def tc14(r):
        mang1 = [48, 72, 120] # UCLN = 24
        mang2 = [105, 140, 175] # UCLN = 35
        mang3 = [13, 26, 39, 52] # UCLN = 13
        r.check(ucln_mang(mang1) == 24, "UCLN([48, 72, 120]) phải bằng 24")
        r.check(ucln_mang(mang2) == 35, "UCLN([105, 140, 175]) phải bằng 35")
        r.check(ucln_mang(mang3) == 13, "UCLN([13, 26, 39, 52]) phải bằng 13")
    runner.run_case("TC14", "Yêu cầu mở rộng: Tính UCLN của các mảng số nguyên dương", tc14)

    print("=" * 78)
    print("TỔNG KẾT KẾT QUẢ KIỂM THỬ (PHỤC VỤ MINH CHỨNG A09):")
    print(f"- Tổng số ca kiểm thử độc lập: {runner.total_tests}")
    print(f"- Số ca ĐẠT (PASS):            {runner.passed_tests} / {runner.total_tests}")
    print(f"- Số ca HỎNG (FAIL):           {runner.failed_tests} / {runner.total_tests}")
    print(f"- Tổng số phép kiểm (assert): {runner.total_asserts}")
    print(f"- Số phép kiểm đạt:            {runner.passed_asserts} / {runner.total_asserts}")
    print("=" * 78)

    if runner.failed_tests > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
