def main():
    # 1. Nhập dữ liệu từ bàn Phím
    # Sử dụng float() để nhận số thập phân cho kích thước
    chiều_dài = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
    chiều_rộng = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
    chiều_cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

    # Sử dụng int() vì số lượng chữ số lẻ bắt buộc phải là số nguyên
    số_lẻ = int(input("Số lượng số lẻ cần hiển thị: "))

    # 2. Tính toán diện tích đáy và thể tích
    diện_tích_đáy = chiều_dài * chiều_rộng
    thể_tích = diện_tích_đáy * chiều_cao

    # 3. Xuất kết quả theo định dạng yêu cầu
    # Sử dụng f-string kết hợp mã UNICODE \u00b2 và \u00b3
    print("\nTính và xuất kết quả theo ví dụ sau:")
    print(f"- Diện tích đáy hình chữ nhật = {diện_tích_đáy:.{số_lẻ}f} cm\u00b2")
    print(f"- Thể tích hình khối = {thể_tích:.{số_lẻ}f} cm\u00b3")
if __name__ == "__main__":
    main()