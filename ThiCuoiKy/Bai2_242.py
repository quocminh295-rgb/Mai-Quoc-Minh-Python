import math
#1: IN BẢNG CỬU CHƯƠNG TỪ A ĐẾN B (HOẶC NGƯỢC LẠI)
def nhap_hai_so_bai_1():
    """Nhập 2 số nguyên cách nhau bằng dấu phẩy."""
    while True:
        try:
            dong_nhap = input("Nhập hai số nguyên a và b (cách nhau bởi dấu phẩy ','): ")
            cac_phan_tu = dong_nhap.split(',')
            if len(cac_phan_tu) != 2:
                print("Lỗi: Bạn phải nhập đúng 2 số và cách nhau bằng một dấu phẩy!")
                continue
            a = int(cac_phan_tu[0].strip())
            b = int(cac_phan_tu[1].strip())
            return a, b
        except ValueError:
            print("Lỗi: Dữ liệu không hợp lệ. Vui lòng nhập các số nguyên.")


def in_mot_bang_cuu_chuong(n):
    """In chi tiết một bảng cửu chương của số n."""
    print(f"=== BẢNG CỬU CHƯƠNG {n} ===")
    for i in range(1, 11):
        print(f"{n:2d} x {i:2d} = {n * i:3d}")
    print()


def bai_1_bang_cuu_chuong():
    """Hàm thực thi chính của Bài 1."""
    print("\n--- BÀI 1: IN BẢNG CỬU CHƯƠNG THEO ĐOẠN ---")
    a, b = nhap_hai_so_bai_1()
    bat_dau = min(a, b)
    ket_thuc = max(a, b)
    print(f"\nTiến hành in các bảng cửu chương từ {bat_dau} đến {ket_thuc}:\n")
    for i in range(bat_dau, ket_thuc + 1):
        in_mot_bang_cuu_chuong(i)



# 2: LIỆT KÊ SỐ NGUYÊN TỐ < N


def nhap_so_nguyen_duong(thong_bao):
    """Hàm dùng chung để ép buộc nhập số nguyên dương > 0."""
    while True:
        try:
            n = int(input(thong_bao))
            if n > 0:
                return n
            else:
                print("Lỗi: Số nhập vào phải lớn hơn 0. Vui lòng thử lại!")
        except ValueError:
            print("Lỗi: Định dạng không hợp lệ. Vui lòng nhập một số nguyên!")


def la_so_nguyen_to(k):
    """Kiểm tra một số có phải số nguyên tố hay không (Tối ưu hóa căn bậc 2)."""
    if k <= 1:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    can_bac_hai = int(math.sqrt(k))
    for i in range(3, can_bac_hai + 1, 2):
        if k % i == 0:
            return False
    return True


def bai_2_liet_ke_snt():
    """Hàm thực thi chính của Bài 2."""
    print("\n--- BÀI 2: LIỆT KÊ SỐ NGUYÊN TỐ < N ---")
    n = nhap_so_nguyen_duong("Nhập vào một số nguyên dương n: ")
    danh_sach_snt = [i for i in range(2, n) if la_so_nguyen_to(i)]

    if not danh_sach_snt:
        print(f"Không có số nguyên tố nào nhỏ hơn {n}.")
    else:
        print(f"Có {len(danh_sach_snt)} số nguyên tố nhỏ hơn {n}:")
        print(", ".join(map(str, danh_sach_snt)))




# HÀM ĐIỀU PHỐI CHÍNH (MENU HỆ THỐNG)
def main():
    while True:
        print("\n CHƯƠNG TRÌNH TỔNG HỢP")
        print("1. Bài 1: In các bảng cửu chương từ a đến b (nhập dạng a,b)")
        print("2. Bài 2: Liệt kê các số nguyên tố nhỏ hơn n")
        print("0. Thoát chương trình")
        print("=======================================================")

        luachon = input("Chọn bài toán muốn chạy (0-2): ").strip()

        if luachon == "1":
            bai_1_bang_cuu_chuong()
        elif luachon == "2":
            bai_2_liet_ke_snt()
        elif luachon == "0":
            print("Tạm biệt!")
            break
        else:
            print("không hợp lệ!,nhập số từ 0 đến 2.")


if __name__ == "__main__":
    main()