"""
Chương trình minh họa (Demo) đề tài DT001 - Thuật toán Euclid và đếm vòng lặp
Sinh viên: Huỳnh Nguyễn Tiến Anh - MSSV: N24DCDT001 - Lớp: D24CQDT01-N
Học phần: Cấu trúc dữ liệu và giải thuật (INT13185 - Nhóm 03)
"""

import sys
import os

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Đảm bảo import được module từ thư mục src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from euclid import ucln, dem_vong, lan_vet_ucln, in_bang_lan_vet, ucln_mang, tao_day_fibonacci, kiem_tra_dau_vao


def chay_vi_du_1():
    print("\n" + "#" * 60)
    print("VÍ DỤ 1 TRÊN PHIẾU: a = 48, b = 18")
    print("#" * 60)
    in_bang_lan_vet(48, 18)


def chay_vi_du_2():
    print("\n" + "#" * 60)
    print("VÍ DỤ 2 TRÊN PHIẾU: a = 89, b = 55 (Hai số Fibonacci F11 và F10)")
    print("#" * 60)
    in_bang_lan_vet(89, 55)


def chay_nam_ca_phieu():
    print("\n" + "#" * 60)
    print("NĂM CA KIỂM TRA BẮT BUỘC TRÊN PHIẾU GIAO ĐỀ TÀI")
    print("#" * 60)
    cac_ca = [
        (48, 18, 6, 3, "1. Ví dụ 1 thông thường"),
        (89, 55, 1, 9, "2. Cặp Fibonacci liên tiếp (xấu nhất)"),
        (12, 12, 12, 1, "3. Hai số bằng nhau (a = b)"),
        (35, 1, 1, 1, "4. Số chia bằng 1 (b = 1)"),
        (9, 0, 9, 0, "5. Số chia bằng 0 (b = 0, dừng ngay)")
    ]
    
    print(f"{'Mô tả':<32} | {'Input (a, b)':<14} | {'Kỳ vọng':<12} | {'Thực tế':<12} | {'Kết luận'}")
    print("-" * 85)
    for a, b, exp_gcd, exp_vong, desc in cac_ca:
        act_gcd = ucln(a, b)
        act_vong = dem_vong(a, b)
        ket_luan = "PASS" if (act_gcd == exp_gcd and act_vong == exp_vong) else "FAIL"
        print(f"{desc:<32} | ({a}, {b}){'':<6} | gcd={exp_gcd}, v={exp_vong:<3} | gcd={act_gcd}, v={act_vong:<3} | {ket_luan}")


def khao_sat_fibonacci():
    print("\n" + "#" * 60)
    print("KHẢO SÁT CÁC CẶP SỐ FIBONACCI LIÊN TIẾP (ĐỊNH LÝ LAMÉ)")
    print("#" * 60)
    fib = tao_day_fibonacci(15)
    print(f"Dãy 14 số Fibonacci đầu: {fib[1:]}\n")
    print(f"{'Cặp Fibonacci (F_k+1, F_k)':<26} | {'Giá trị':<18} | {'gcd':<6} | {'Số vòng lặp':<12} | {'Nhận xét'}")
    print("-" * 80)
    for k in range(2, len(fib)):
        a = fib[k]
        b = fib[k - 1]
        g = ucln(a, b)
        v = dem_vong(a, b)
        nhan_xet = f"vòng lặp = k - 2 = {k - 1}"
        print(f"k={k+1:<2} (F_{k+1}, F_{k}){'':<10} | ({a}, {b}){'':<8} | {g:<6} | {v:<12} | {nhan_xet}")


def demo_ucln_mang():
    print("\n" + "#" * 60)
    print("YÊU CẦU MỞ RỘNG: TÍNH UCLN CỦA MỘT MẢNG SỐ NGUYÊN")
    print("#" * 60)
    mang_test = [
        [48, 18, 30],
        [120, 80, 40, 20],
        [17, 34, 51, 68],
        [89, 55, 144]
    ]
    for m in mang_test:
        kq = ucln_mang(m)
        print(f"Mảng: {m} -> UCLN = {kq}")


def nhap_tu_ban_phim():
    print("\n" + "#" * 60)
    print("CHẾ ĐỘ NHẬP DỮ LIỆU TỪ BÀN PHÍM (GIẢNG VIÊN KIỂM TRA)")
    print("#" * 60)
    try:
        raw_a = input("Nhập số nguyên dương a (hoặc a > 0 nếu b = 0): ").strip()
        raw_b = input("Nhập số nguyên không âm b: ").strip()
        a = int(raw_a)
        b = int(raw_b)
        kiem_tra_dau_vao(a, b)
        in_bang_lan_vet(a, b)
    except ValueError as e:
        print(f"[LỖI ĐẦU VÀO]: {e}")
    except TypeError as e:
        print(f"[LỖI KIỂU DỮ LIỆU]: {e}")
    except Exception as e:
        print(f"[LỖI KHÔNG XÁC ĐỊNH]: {e}")


def menu():
    while True:
        print("\n" + "=" * 60)
        print("ĐỒ ÁN CTDL&GT: THUẬT TOÁN EUCLID VÀ ĐẾM VÒNG LẶP (DT001)")
        print("Sinh viên: Huỳnh Nguyễn Tiến Anh - MSSV: N24DCDT001")
        print("=" * 60)
        print("1. Chạy Ví dụ 1 (a = 48, b = 18) [Ảnh A01]")
        print("2. Chạy Ví dụ 2 (a = 89, b = 55) [Ảnh A02]")
        print("3. Chạy 5 ca kiểm tra bắt buộc trên phiếu")
        print("4. Khảo sát trường hợp xấu nhất với các cặp số Fibonacci")
        print("5. Thử nghiệm tính UCLN của mảng (Yêu cầu mở rộng)")
        print("6. Nhập dữ liệu mới từ bàn phím (Cho giảng viên thử)")
        print("7. Chạy tất cả các mục demo")
        print("0. Thoát")
        print("=" * 60)
        
        chon = input("Chọn chức năng (0-7): ").strip()
        if chon == "1":
            chay_vi_du_1()
        elif chon == "2":
            chay_vi_du_2()
        elif chon == "3":
            chay_nam_ca_phieu()
        elif chon == "4":
            khao_sat_fibonacci()
        elif chon == "5":
            demo_ucln_mang()
        elif chon == "6":
            nhap_tu_ban_phim()
        elif chon == "7":
            chay_vi_du_1()
            chay_vi_du_2()
            chay_nam_ca_phieu()
            khao_sat_fibonacci()
            demo_ucln_mang()
        elif chon == "0":
            print("Kết thúc chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 7.")


if __name__ == "__main__":
    # Nếu chạy có tham số dòng lệnh --all thì in tất cả demo (tiện cho test và chụp ảnh)
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        chay_vi_du_1()
        chay_vi_du_2()
        chay_nam_ca_phieu()
        khao_sat_fibonacci()
        demo_ucln_mang()
    elif len(sys.argv) > 1 and sys.argv[1] == "--vd1":
        chay_vi_du_1()
    elif len(sys.argv) > 1 and sys.argv[1] == "--vd2":
        chay_vi_du_2()
    else:
        menu()
