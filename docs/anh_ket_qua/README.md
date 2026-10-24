# Danh mục và Kế hoạch 11 Ảnh Minh chứng (A01 – A11)

Đề tài: **DT001 - Thuật toán Euclid và đếm vòng lặp**  
Sinh viên: **Huỳnh Nguyễn Tiến Anh** - MSSV: **N24DCDT001** - Lớp: **D24CQDT01-N**  
Môn học: Cấu trúc dữ liệu và giải thuật (INT13185 - Nhóm 03)

---

## Bảng quy hoạch 11 ảnh minh chứng bắt buộc

| Mã ảnh | Tên file ảnh gợi ý | Lệnh chạy / Thao tác | Nội dung minh chứng | Vị trí trong Báo cáo |
|:---:|:---|:---|:---|:---:|
| **A01** | `01_vi_du_1.png` | `python demo.py --vd1` | Chạy Ví dụ 1 trên phiếu: $a=48, b=18 \to \gcd=6$, số vòng = 3, dãy số dư $[12, 6, 0]$. | Hình 4.1 |
| **A02** | `02_vi_du_2.png` | `python demo.py --vd2` | Chạy Ví dụ 2 trên phiếu: $a=89, b=55 \to \gcd=1$, số vòng = 9 (hai số Fibonacci liên tiếp). | Hình 4.2 |
| **A03** | `03_tu_thiet_ke_1.png` | `python demo.py` (chọn 6 nhập $252, 105$) | Ca tự thiết kế 1: $a=252, b=105 \to \gcd=21$, số vòng = 3. | Hình 4.3 |
| **A04** | `04_tu_thiet_ke_2.png` | `python demo.py` (chọn 6 nhập $1000, 350$) | Ca tự thiết kế 2: $a=1000, b=350 \to \gcd=50$, số vòng = 3. | Hình 4.4 |
| **A05** | `05_bien_1.png` | `python demo.py` (chọn 6 nhập $12, 12$) | Ca biên 1: Hai số bằng nhau $a=12, b=12 \to \gcd=12$, số vòng = 1. | Hình 4.5 |
| **A06** | `06_bien_2.png` | `python demo.py` (chọn 6 nhập $35, 1$) | Ca biên 2: Số chia bằng 1 $a=35, b=1 \to \gcd=1$, số vòng = 1. | Hình 4.6 |
| **A07** | `07_bien_3.png` | `python demo.py` (chọn 6 nhập $9, 0$) | Ca biên 3: Số chia bằng 0 $a=9, b=0 \to \gcd=9$, số vòng = 0 (dừng ngay, không chia). | Hình 4.7 |
| **A08** | `08_input_khong_hop_le.png` | `python demo.py` (chọn 6 nhập số âm `-15, 10`) | Validator phát hiện lỗi, ném ngoại lệ rõ ràng và từ chối xử lý dữ liệu sai. | Hình 4.8 |
| **A09** | `09_tong_ket_kiem_thu.png` | `python test/test_euclid.py` | Toàn bộ 14 ca kiểm thử chạy tự động, in rõ số ca PASS (14/14) và số assert đạt (31/31). | Hình 4.9 |
| **A10** | `10_clone_sach_chay_lai.png` | `git clone ...` sang thư mục mới rồi chạy `test_euclid.py` | Kiểm chứng tính độc lập: clone từ commit C trên Git về máy và chạy thành công ngay lập tức. | Hình 4.10 |
| **A11** | `11_github_repo_commit.png` | Chụp màn hình trình duyệt GitHub | Trang repository thật trên GitHub cá nhân hiển thị rõ username, commit C và đường dẫn mã nguồn. | Hình 4.11 |

---

## Hướng dẫn chụp ảnh
1. Chụp rõ ràng toàn bộ cửa sổ Terminal / PowerShell (thấy được lệnh chạy và kết quả in ra).
2. Lưu các file ảnh chụp vào đúng thư mục này: `C:\ctdl\N24DCDT001_DT001_Euclid\docs\anh_ket_qua\`.
3. Chèn các file ảnh này vào đúng các mục tương ứng trong file Báo cáo Word.
