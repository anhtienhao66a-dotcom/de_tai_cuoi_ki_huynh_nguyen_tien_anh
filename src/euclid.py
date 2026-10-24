"""
HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG - CƠ SỞ TẠI TP. HỒ CHÍ MINH
KHOA CÔNG NGHỆ THÔNG TIN
Môn học: Cấu trúc dữ liệu và giải thuật (INT13185 - Nhóm 03)
Giảng viên hướng dẫn: Hồ Nhựt Minh

ĐỀ TÀI: DT001 - THUẬT TOÁN EUCLID VÀ ĐẾM VÒNG LẶP
Sinh viên thực hiện: Huỳnh Nguyễn Tiến Anh
Mã số sinh viên: N24DCDT001
Lớp: D24CQDT01-N

Giáo trình căn cứ: INT1306, Chương 1, Mục 1.2.4 (trang PDF 27-28), Mục 1.6 Bài 16 (trang PDF 43).
"""

from typing import List, Tuple, Dict, Any


def kiem_tra_dau_vao(a: Any, b: Any) -> None:
    """
    Hợp đồng dữ liệu vào (Validator):
    - a, b phải là số nguyên (hoặc kiểu có thể chuyển đổi chính xác sang số nguyên).
    - a >= 0, b >= 0 và không đồng thời cả a = 0 và b = 0.
    - Trường hợp b = 0 chỉ hợp lệ khi a > 0.
    - Miền giá trị theo phiếu: 0 <= a, b <= 10^9.
    """
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(f"Giá trị a={a!r} không phải là số nguyên hợp lệ.")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(f"Giá trị b={b!r} không phải là số nguyên hợp lệ.")
    
    if a < 0 or b < 0:
        raise ValueError(f"Dữ liệu vào phải không âm (nhận được a={a}, b={b}).")
    
    if a == 0 and b == 0:
        raise ValueError("Không xác định ước chung lớn nhất khi cả hai số a và b đều bằng 0.")
    
    if a > 10**9 or b > 10**9:
        raise ValueError(f"Giá trị vượt quá giới hạn 10^9 theo yêu cầu của phiếu giao đề tài (a={a}, b={b}).")


def ucln(a: int, b: int) -> int:
    """
    Tìm ước chung lớn nhất (UCLN / GCD) của hai số a và b bằng thuật toán Euclid (chia lấy dư).
    Bất biến lặp: gcd(a, b) = gcd(b, a mod b).
    Điều kiện dừng: khi b = 0, kết quả là a.
    Độ phức tạp thời gian: O(log(min(a, b))).
    Độ phức tạp không gian: O(1).
    """
    kiem_tra_dau_vao(a, b)
    while b != 0:
        a, b = b, a % b
    return a


def dem_vong(a: int, b: int) -> int:
    """
    Đếm số vòng lặp thực hiện trong thuật toán Euclid cho đến khi b = 0.
    Mỗi bước chia lấy dư (khi b > 0) tính là 1 vòng lặp.
    Nếu b = 0 ngay từ đầu (với a > 0), số vòng lặp là 0.
    """
    kiem_tra_dau_vao(a, b)
    so_vong = 0
    curr_a, curr_b = a, b
    while curr_b != 0:
        curr_a, curr_b = curr_b, curr_a % curr_b
        so_vong += 1
    return so_vong


def lan_vet_ucln(a: int, b: int) -> Dict[str, Any]:
    """
    Lần vết từng bước của thuật toán Euclid.
    Trả về từ điển gồm:
    - 'a_ban_dau': a ban đầu
    - 'b_ban_dau': b ban đầu
    - 'cac_buoc': danh sách các bước lặp với thông tin:
        - 'vong': số thứ tự vòng lặp (1, 2, ...)
        - 'a': giá trị a trước khi chia
        - 'b': giá trị b trước khi chia
        - 'du': phần dư r = a % b
        - 'a_moi': giá trị a sau cập nhật (= b)
        - 'b_moi': giá trị b sau cập nhật (= r)
    - 'gcd': ước chung lớn nhất tìm được
    - 'so_vong': tổng số vòng lặp
    - 'cac_so_du': danh sách các số dư r qua từng vòng
    """
    kiem_tra_dau_vao(a, b)
    cac_buoc = []
    cac_so_du = []
    curr_a, curr_b = a, b
    vong = 0

    while curr_b != 0:
        vong += 1
        r = curr_a % curr_b
        cac_so_du.append(r)
        cac_buoc.append({
            'vong': vong,
            'a': curr_a,
            'b': curr_b,
            'du': r,
            'a_moi': curr_b,
            'b_moi': r
        })
        curr_a, curr_b = curr_b, r

    return {
        'a_ban_dau': a,
        'b_ban_dau': b,
        'cac_buoc': cac_buoc,
        'gcd': curr_a,
        'so_vong': vong,
        'cac_so_du': cac_so_du
    }


def in_bang_lan_vet(a: int, b: int) -> None:
    """
    In bảng lần vết thuật toán Euclid theo định dạng Bảng 1.7 giáo trình trang 28.
    """
    ket_qua = lan_vet_ucln(a, b)
    print("=" * 64)
    print(f"LẦN VẾT THUẬT TOÁN EUCLID: a = {a}, b = {b}")
    print("=" * 64)
    print(f"{'Trước vòng':<14} | {'a':<12} | {'b':<12} | {'a mod b':<12}")
    print("-" * 64)
    
    if not ket_qua['cac_buoc']:
        print(f"{'Khởi đầu':<14} | {a:<12} | {b:<12} | {'(dừng ngay)':<12}")
    else:
        for b_info in ket_qua['cac_buoc']:
            print(f"Vòng {b_info['vong']:<9} | {b_info['a']:<12} | {b_info['b']:<12} | {b_info['du']:<12}")
            
    print("-" * 64)
    print(f"KẾT QUẢ: gcd = {ket_qua['gcd']} | Số vòng lặp: {ket_qua['so_vong']}")
    print(f"Dãy số dư: {ket_qua['cac_so_du']}")
    print("=" * 64)


def ucln_mang(danh_sach: List[int]) -> int:
    """
    Yêu cầu mở rộng: Tính UCLN của một mảng các số nguyên dương
    bằng cách áp dụng thuật toán Euclid liên tiếp:
    gcd(a1, a2, ..., an) = gcd(gcd(...gcd(a1, a2), a3)..., an).
    """
    if not danh_sach:
        raise ValueError("Mảng không được rỗng.")
    
    for x in danh_sach:
        if not isinstance(x, int) or isinstance(x, bool) or x <= 0:
            raise ValueError(f"Phần tử mảng phải là số nguyên dương (nhận được {x!r}).")
    
    ket_qua = danh_sach[0]
    for x in danh_sach[1:]:
        ket_qua = ucln(ket_qua, x)
        if ket_qua == 1:
            break
    return ket_qua


def tao_day_fibonacci(n: int) -> List[int]:
    """
    Tạo danh sách n số Fibonacci đầu tiên: F1=1, F2=1, F3=2, F4=3, F5=5, ...
    Dùng để khảo sát trường hợp xấu nhất của thuật toán Euclid (Định lý Lamé).
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
