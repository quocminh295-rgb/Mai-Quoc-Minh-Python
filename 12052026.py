//B14
x = int(input("Nhap so tien X: "))
temp_x = x
denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
total_bills = 0

print(f"So tien {temp_x} duoc doi thanh:")
for d in denominations:
    count = x // d
    x %= d
    total_bills += count
    print(f"Loai {d} gom {count} to")

print(f"TONG CONG CO {total_bills} TO"

//B20
def giai_quyet_giao_dich():
    # Bước 1: Nhập dữ liệu đầu vào
    try:
        a = int(input("Nhap so tien hang can tra (a): "))
        b = int(input("Nhap so tien khach thuc te tra (b): "))
    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le.")
        return

    # Bước 2: Kiem tra cac truong hop giao dich
    if a > b:
        print(f"So tien khach hang con thieu la: {a - b}")

    elif a == b:
        print("Cam on khach hang. Hen gap lai")

    else:
        # Truong hop b > a: Can thoi lai tien
        so_tien_thoi = b - a
        print(f"\nSo tien thoi lai {so_tien_thoi} duoc doi thanh:")

        # Danh sach cac menh gia theo thu tu giam dan
        menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        tong_so_to = 0
        tong_so_loai = 0

        # Bước 3: Thuc hien thuat toan Tham lam (Greedy Algorithm)
        for loai in menh_gia:
            # Su dung phep chia lay phan nguyen de tinh so to
            so_to = so_tien_thoi // loai

            # Neu co so to > 0 thi moi thuc hien in va dem
            if so_to > 0:
                print(f"Loai {loai} gom {so_to} to")
                tong_so_to += so_to
                tong_so_loai += 1

                # Cap nhat lai so tien thoi bang phep chia lay phan du
                so_tien_thoi %= loai

        # Bước 4: In ket qua thong ke
        print(f"TONG CONG CO {tong_so_to} TO")
        print(f"Tong so loai = {tong_so_loai}")

        # Bước 5: Tuong tac ket thuc
        input("\n(Nhan phim Enter de tiep tuc...)")
        print("Cam on khach hang. Hen gap lai")


if __name__ == "__main__":
    giai_quyet_giao_dich()