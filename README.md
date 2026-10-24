# DT001 — THUẬT TOÁN EUCLID VÀ ĐẾM VÒNG LẶP

## 1. Thông tin sinh viên & Đề tài
- **Họ và tên:** Huỳnh Nguyễn Tiến Anh
- **Mã số sinh viên:** N24DCDT001
- **Lớp:** D24CQDT01-N
- **Môn học:** Cấu trúc dữ liệu và giải thuật (INT13185 - Nhóm 03)
- **Giảng viên hướng dẫn:** Hồ Nhựt Minh
- **Mã đề tài:** `DT001`
- **Căn cứ giáo trình:** *Giáo trình Cấu trúc dữ liệu và Giải thuật (INT1306)*
  - Chương 1, Mục 1.2.4 (Ví dụ 1.1) và Mục 1.6 Bài tập 16
  - Trang in: 15–16, 31 | Trang PDF: 27–28, 43

---

## 2. Mô tả đề tài & Hợp đồng dữ liệu
- **Bài toán:** Tìm ước chung lớn nhất (UCLN / GCD) của hai số nguyên dương bằng phép chia lấy dư, theo dõi biến qua từng vòng lặp, in bảng lần vết $(a, b, a \pmod b)$ và đếm tổng số vòng lặp. Khảo sát trường hợp xấu nhất trên các cặp số Fibonacci liên tiếp.
- **Hợp đồng đầu vào (Input):**
  - $a, b$ là số nguyên, $0 \le a, b \le 10^9$.
  - Không đồng thời cả $a = 0$ và $b = 0$.
  - Nếu $b = 0$ thì bắt buộc $a > 0$.
  - Nhập trực tiếp từ bàn phím hoặc truyền làm tham số cho hàm.
- **Kết quả ra (Output):**
  - Ước chung lớn nhất ($\gcd$), tổng số vòng lặp, và bảng lần vết các bước trước khi cập nhật.

---

## 3. Cấu trúc thư mục
```text
N24DCDT001_DT001_Euclid/
├── src/
│   └── euclid.py            # Thuật toán Euclid, bộ validator, lần vết, đếm vòng lặp, UCLN mảng
├── test/
│   └── test_euclid.py       # Bộ 14 ca kiểm thử tự động độc lập (đạt 100% PASS)
├── docs/
│   └── anh_ket_qua/         # Thư mục lưu 11 ảnh minh chứng gốc (A01 - A11)
├── demo.py                  # Giao diện menu demo, nhập từ bàn phím, phân tích Fibonacci
├── README.md                # Tài liệu hướng dẫn sử dụng và kiểm thử
└── .gitignore               # Cấu hình bỏ qua các tệp tạm, cache
```

---

## 4. Hướng dẫn chạy chương trình

### 4.1. Môi trường yêu cầu
- Python 3.8+ (khuyên dùng Python 3.10 trở lên; chương trình đã kiểm thử đạt trên Python 3.14).
- Chỉ sử dụng thư viện chuẩn của Python (`math`, `sys`, `os`, `typing`), không cần cài đặt thêm gói ngoài.

### 4.2. Chạy chương trình chính (Demo & Tương tác bàn phím)
Mở Terminal hoặc PowerShell tại thư mục này:

1. **Chạy giao diện Menu chọn chức năng:**
   ```powershell
   python demo.py
   ```
2. **Chạy nhanh toàn bộ các mục minh họa:**
   ```powershell
   python demo.py --all
   ```
3. **Chạy riêng Ví dụ 1 trên phiếu (để chụp ảnh A01):**
   ```powershell
   python demo.py --vd1
   ```
4. **Chạy riêng Ví dụ 2 trên phiếu (để chụp ảnh A02):**
   ```powershell
   python demo.py --vd2
   ```

### 4.3. Chạy bộ kiểm thử tự động (14 ca độc lập)
Để chạy toàn bộ ca kiểm thử và in thống kê số ca PASS cùng số lượng assert:
```powershell
python test/test_euclid.py
```

---

## 5. Quy trình đưa lên GitHub & Kiểm chứng hai Commit C / S

### Bước 1: Khởi tạo Git và đẩy mã nguồn (Commit C)
```powershell
git init
git add .
git commit -m "Commit C: Hoan thien thuat toan Euclid, demo va 14 ca test dat chuan"
git branch -M main
git remote add origin https://github.com/anhtienhao66a-dotcom/de_tai_cuoi_ki_huynh_nguyen_tien_anh.git
git push -u origin main
```
Lấy mã SHA commit C bằng lệnh:
```powershell
git rev-parse HEAD
```
*(Ghi mã SHA này vào Báo cáo và file thông tin nộp).*

### Bước 2: Kiểm chứng clone sạch (để chụp ảnh A10)
Mở một thư mục tạm khác (ví dụ `C:\ctdl\kiem_tra_clone\`) và chạy:
```powershell
git clone https://github.com/anhtienhao66a-dotcom/de_tai_cuoi_ki_huynh_nguyen_tien_anh.git .
python test/test_euclid.py
```
*(Chụp màn hình thao tác này làm ảnh A10).*

### Bước 3: Đưa ảnh kết quả vào thư mục `docs/anh_ket_qua/` và chốt Commit S
```powershell
git add docs/anh_ket_qua/
git commit -m "Commit S: Bo sung 11 anh ket qua thuc nghiem va hoan tat tai lieu nop"
git push
git rev-parse HEAD
```
Lấy mã SHA commit S này để điền vào file `ThongTinNop.txt`.
