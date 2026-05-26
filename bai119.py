
import math

# 1 Ham kiem tra so nguyen to
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Toi uu hoa Chi kiem tra cac so co dang 6k +- 1
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# 2 Ham xoay so 180 do tra ve chuoi xoay hoac None neu chua so khong the xoay
def get_rotated_number(num_str, extended=False):
    # Bo quy tac xoay chuan
    mapping = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    
    # Neu la mo rong them 2 va 5
    if extended:
        mapping['2'] = '2'
        mapping['5'] = '5'
        
    rotated_str = ""
    # Duyet nguoc chuoi tu cuoi len dau de mo phong viec xoay 180 do
    for char in reversed(num_str):
        if char not in mapping:
            return None # Chua chu so khong the xoay vd 3 4 7
        rotated_str += mapping[char]
        
    return rotated_str
# CHUONG TRINH CHINH
limit = 1000000

# Khoi tao cac danh sach de luu ket qua
list_a = []
list_b = []
list_c = []
list_d = []
list_e = []

print("Dang xu ly du lieu vui long doi vai giay")

# Thay vi duyet tu 1 den 1000000 co the hoi cham chung ta duyet va phan loai truc tiep
for i in range(limit):
    num_str = str(i)
    
    # Xu ly chuan Cau a b e
    rotated_std = get_rotated_number(num_str, extended=False)
    if rotated_std is not None: # Neu so nay CO THE xoay duoc theo chuan
        rotated_std_int = int(rotated_std)
        is_strobogrammatic = (rotated_std == num_str)
        
        # Cau a So strobogrammatic chuan
        if is_strobogrammatic:
            list_a.append(i)
            # Cau b So nguyen to strobogrammatic chuan
            if is_prime(i):
                list_b.append(i)
                
        # Cau e Khong strobogrammatic khong nguyen to nhung xoay xong la nguyen to
        elif not is_prime(i) and is_prime(rotated_std_int):
            list_e.append(i)

    # Xu ly mo rong Cau c d
    rotated_ext = get_rotated_number(num_str, extended=True)
    if rotated_ext is not None:
        if rotated_ext == num_str:
            list_c.append(i)
            if is_prime(i):
                list_d.append(i)

# IN KET QUA
print("\n--- KET QUA ---")
print(f"a Co {len(list_a)} so strobogrammatic nho hon 1 trieu")
# In ra mot so ket qua dau tien cua cau a de tranh tran man hinh
print(f"   Vi du {list_a[:15]}...\n")

print("b Cac so nguyen to strobogrammatic nho hon 1 trieu")
print("  ", list_b, "\n")

print(f"c Co {len(list_c)} so strobogrammatic mo rong nho hon 1 trieu")
print(f"   Vi du {list_c[:15]}...\n")

print("d Cac so nguyen to strobogrammatic mo rong nho hon 1 trieu")
print("  ", list_d, "\n")

print(f"e Cac so thoa man Khong strobogrammatic khong nguyen to xoay 180 do ra nguyen to in 20 so dau")

print("  ", list_e[:20], "...")