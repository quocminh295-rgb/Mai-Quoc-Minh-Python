
#Sử dụng hàm Lambda, all(), any() để tìm số đồng nhất và số hoàn thiện

# 1. Định nghĩa hàm lambda kiểm tra Số đồng nhất bằng cách sử dụng all()

# Chuyển số n thành chuỗi và kiểm tra xem tất cả các ký tự có trùng với ký tự đầu tiên không.

is_repdigit = lambda n: all(char == str(n)[0] for char in str(n))

# 2. Định nghĩa hàm lambda kiểm tra Số hoàn thiện bằng cách sử dụng any()
# Tính tổng các ước số từ 1 đến n-1.

# Sử dụng any([biểu_thức_so_sánh]) để trả về True nếu tổng ước bằng chính nó.

is_perfect_number = lambda n: any([sum(i for i in range(1, n) if n % i == 0) == n])

# Duyệt và in các số trong khoảng từ 1 đến 10000
if __name__ == "__main__":
    print("--- CÁC SỐ ĐỒNG NHẤT TỪ 1 ĐẾN 10000 ---")
    repdigits = [num for num in range(1, 10001) if is_repdigit(num)]
    print(repdigits)
    print(f"Tổng cộng có {len(repdigits)} số đồng nhất.")

    print("\n--- CÁC SỐ HOÀN THIỆN TỪ 1 ĐẾN 10000 ---")
    perfect_numbers = [num for num in range(1, 10001) if is_perfect_number(num)]
    print(perfect_numbers)
    print(f"Tổng cộng có {len(perfect_numbers)} số hoàn thiện.")