import math


# 1 hàm lambda kiểm tra bội của 13 hoặc 19.
# Trả về True nếu n chia hết cho 13 hoặc 19, ngược lại trả về False
check_boi_so = lambda n: (n % 13 == 0 or n % 19 == 0)


# 2 hàm lambda phân loai tam giác.

# Sử dụng biểu thức điều kiện lồng nhau để kiểm tra và phân loại
classify_triangle = lambda a, b, c: (
    "Khong phai la tam giac"
    if not (a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0)
    else (
        "Tam giac deu" if a == b == c
        else "Tam giac vuong can" if (
                (a == b or b == c or a == c) and
                (math.isclose(a ** 2 + b ** 2, c ** 2) or math.isclose(a ** 2 + c ** 2, b ** 2) or math.isclose(
                    b ** 2 + c ** 2, a ** 2))
        )
        else "Tam giac can" if (a == b or b == c or a == c)
        else "Tam giac vuong" if (
                math.isclose(a ** 2 + b ** 2, c ** 2) or math.isclose(a ** 2 + c ** 2, b ** 2) or math.isclose(
            b ** 2 + c ** 2, a ** 2)
        )
        else "Tam giac thuong"
    )
)


#CHẠY THỬ CHƯƠNG TRÌNH (MAIN FUNCTION)
if __name__ == "__main__":
    print("1: KIEM TRA BOI SO")
    test_numbers = [26, 38, 45, 0]
    for num in test_numbers:
        print(f"So {num}: Boi cua 13/19? -> {check_boi_so(num)}")

    print("\n" + "=" * 40 + "\n")

    print("2: PHAN LOAI TAM GIAC")
    test_triangles = [
        (3, 4, 5),  # Vuông
        (6, 6, 6),  # Đều
        (5, 5, 8),  # Cân
        (1, 1, math.sqrt(2)),  # Vuông cân
        (7, 9, 12),  # Thường
        (1, 2, 4)  # Không hợp lệ
    ]

    for a, b, c in test_triangles:
        # Làm tròn số thực khi hiển thị cho gọn
        a_disp = round(a, 2) if isinstance(a, float) else a
        b_disp = round(b, 2) if isinstance(b, float) else b
        c_disp = round(c, 2) if isinstance(c, float) else c

        result = classify_triangle(a, b, c)
        print(f"Bo ba canh ({a_disp}, {b_disp}, {c_disp}) -> {result}")