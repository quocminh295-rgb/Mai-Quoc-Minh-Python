
def generate_strobogrammatic(n, is_extended=False):
    # Ham de quy xay dung chuoi tu do dai nho len do dai lon
    # current_n: do dai chuoi dang xay dung
    # target_n: do dai toi da n cua de bai
    def helper(current_n, target_n):
        # Base case (Diem dung cua de quy)
        if current_n == 0:
            return [""]
        if current_n == 1:
            if is_extended:
                return ["0", "1", "8", "2", "5"]
            else:
                return ["0", "1", "8"]
        
        # Lay danh sach cac chuoi o buoc truoc (ngan hon 2 ky tu)
        middle_results = helper(current_n - 2, target_n)
        result = []
        
        # Them cac cap chu so strobogrammatic vao 2 dau cua chuoi giua
        for middle in middle_results:
            # So 0 khong the dung o vi tri ngoai cung cua mot so nhieu chu so
            if current_n != target_n:
                result.append("0" + middle + "0")
            
            # Cac cap chuan
            result.append("1" + middle + "1")
            result.append("8" + middle + "8")
            result.append("6" + middle + "9")
            result.append("9" + middle + "6")
            
            # Cac cap mo rong
            if is_extended:
                result.append("2" + middle + "2")
                result.append("5" + middle + "5")
                
        return result

    # Bat dau goi de quy
    return helper(n, n)

# --- CHUONG TRINH CHINH ---
if __name__ == "__main__":
    # Nhap va kiem tra du lieu dau vao (2 <= n <= 10)
    while True:
        try:
            n = int(input("Nhap so nguyen n (2 <= n <= 10): "))
            if 2 <= n <= 10:
                break
            else:
                print("Vui long nhap n trong khoang tu 2 den 10.")
        except ValueError:
            print("Dau vao khong hop le. Vui long nhap mot so nguyen.")

    # Xu ly Cau a
    result_a = generate_strobogrammatic(n, is_extended=False)
    print(f"\n--- a. Cac so strobogrammatic chuan gom {n} chu so ---")
    print(f"Tong cong co: {len(result_a)} so")
    print(result_a)

    # Xu ly Cau b
    result_b = generate_strobogrammatic(n, is_extended=True)
    print(f"\n--- b. Cac so strobogrammatic mo rong gom {n} chu so ---")
    print(f"Tong cong co: {len(result_b)} so")

    print(result_b)