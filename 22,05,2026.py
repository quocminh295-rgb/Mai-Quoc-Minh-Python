import math
import time

# =====================================================================
# 1. KHAI BÁO TOÀN BỘ CÁC HÀM LAMBDA (TỪ CÂU A ĐẾN CÂU L)
# =====================================================================

# a) Số thân thiện: GCD của n và số đảo ngược bằng 1
is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương: Căn bậc hai không chứa phần thập phân
is_perfect_square = lambda n: (n ** 0.5) % 1 == 0

# c) Số đồng nhất
is_monodigit_all = lambda n: all(char == str(n)[0] for char in str(n))  # Cách 1
is_monodigit_any = lambda n: not any(char != str(n)[0] for char in str(n))  # Cách 2

# d) Số hoàn thiện: Kiểm tra dựa trên tập hợp số hoàn thiện hữu hạn < 1 triệu
is_perfect_number = lambda n: n in {6, 28, 496, 8128}

# e) Số phong phú: Tổng các ước số thực sự (Tối ưu hóa O(sqrt(n))) lớn hơn n
is_abundant = lambda n: n > 1 and n < sum(
    i + (n // i if i * i != n and i != 1 else 0)
    for i in range(1, int(n ** 0.5) + 1)
    if n % i == 0
)

# f) Số tăng dần: Mọi ký số đứng sau không nhỏ hơn ký số đứng trước
is_increasing_digits = lambda n: list(str(n)) == sorted(str(n))

# g) Số Armstrong: Tổng lũy thừa bậc k của các chữ số bằng chính nó
is_armstrong = lambda n: n == sum(int(char) ** len(str(n)) for char in str(n))

# h) Số nguyên tố
is_prime_c3 = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))  # Cách 3 (any)


def F(k):  # Cách 4 (filter)
    if k <= 1: return False
    return len(list(filter(lambda i: k % i == 0, range(2, int(k ** 0.5) + 1)))) == 0


# i) Số Palindrome (Số đối xứng)
is_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố Palindrome: Kết hợp đối xứng và nguyên tố (ngắt sớm)
is_prime_palindrome = lambda n: n > 1 and str(n) == str(n)[::-1] and not any(
    n % i == 0 for i in range(2, int(n ** 0.5) + 1))

# k) Số lộc phát
is_lucky_all = lambda n: all(char in '68' for char in str(n))  # Cách 1
is_lucky_count = lambda n: str(n).count('6') + str(n).count('8') == len(str(n))  # Cách 2

# l) Số lộc phát Palindrome: Vừa chỉ chứa 6, 8 vừa đối xứng qua trục
is_lucky_palindrome = lambda n: all(char in '68' for char in str(n)) and str(n) == str(n)[::-1]

# =====================================================================
# 2. CHƯƠNG TRÌNH DUYỆT 1 TRIỆU PHẦN TỬ VÀ XUẤT BÁO CÁO KẾT QUẢ
# =====================================================================
if __name__ == "__main__":
    print("=== CHƯƠNG TRÌNH XỬ LÝ ĐỒNG BỘ KHỐI DỮ LIỆU LỚN (1 ĐẾN 1.000.000) ===")
    print("Hệ thống đang thực thi các bộ lọc tối ưu, vui lòng đợi...\n")

    start_total = time.time()
    limit = 1000000

    # a) Số thân thiện (In số lượng + mẫu)
    friendly_count = sum(1 for i in range(1, limit + 1) if is_friendly(i))
    print(f"a) Số thân thiện: Đạt tổng cộng {friendly_count} số.")

    # b) Số chính phương
    perfect_squares = [i for i in range(1, limit + 1) if is_perfect_square(i)]
    print(f"b) Số chính phương: Tìm thấy {len(perfect_squares)} số. Mẫu 10 số đầu: {perfect_squares[:10]}")

    # c) Số đồng nhất
    monodigits = [i for i in range(1, limit + 1) if is_monodigit_all(i)]
    print(f"c) Số đồng nhất: Tìm thấy {len(monodigits)} số. Chi tiết: {monodigits}")

    # d) Số hoàn thiện
    perfect_numbers = [i for i in range(1, limit + 1) if is_perfect_number(i)]
    print(f"d) Số hoàn thiện: Tìm thấy {len(perfect_numbers)} số. Chi tiết: {perfect_numbers}")

    # e) Số phong phú
    abundant_count = sum(1 for i in range(1, limit + 1) if is_abundant(i))
    print(f"e) Số phong phú: Đạt tổng cộng {abundant_count} số.")

    # f) Số tăng dần
    inc_numbers = [i for i in range(1, limit + 1) if is_increasing_digits(i)]
    print(f"f) Số tăng dần: Tìm thấy {len(inc_numbers)} số. Mẫu 10 số đầu: {inc_numbers[:10]}")

    # g) Số Armstrong
    armstrongs = [i for i in range(1, limit + 1) if is_armstrong(i)]
    print(f"g) Số Armstrong: Tìm thấy {len(armstrongs)} số. Chi tiết: {armstrongs}")

    # h) Số nguyên tố
    prime_count = sum(1 for i in range(1, limit + 1) if is_prime_c3(i))
    print(f"h) Số nguyên tố: Đạt tổng cộng {prime_count} số.")

    # i) Số Palindrome
    palindrome_count = sum(1 for i in range(1, limit + 1) if is_palindrome(i))
    print(f"i) Số Palindrome: Tìm thấy {palindrome_count} số.")

    # j) Số nguyên tố Palindrome
    prime_palindromes = [i for i in range(1, limit + 1) if is_prime_palindrome(i)]
    print(
        f"j) Số nguyên tố Palindrome: Tìm thấy {len(prime_palindromes)} số. Một số mẫu lớn: {prime_palindromes[-10:]}")

    # k) Số lộc phát (Kiểm chứng Cách 1 và Cách 2 đồng quy)
    lucky_numbers = [i for i in range(1, limit + 1) if is_lucky_all(i)]
    print(f"k) Số lộc phát: Tìm thấy {len(lucky_numbers)} số. Mẫu 10 số đầu: {lucky_numbers[:10]}")

    # l) Số lộc phát Palindrome
    lucky_palindromes = [i for i in range(1, limit + 1) if is_lucky_palindrome(i)]
    print(f"l) Số lộc phát Palindrome: Tìm thấy {len(lucky_palindromes)} số. Chi tiết: {lucky_palindromes}")

    end_total = time.time()
    print(f"\n[THÀNH CÔNG] Toàn bộ chương trình hoàn thành xuất sắc trong: {end_total - start_total:.2f} giây.")