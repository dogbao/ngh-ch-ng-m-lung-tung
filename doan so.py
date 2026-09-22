import random

def choi_doan_so():
    
    so_bi_mat = random.randint(1, 100)
    so_lan_doan = 0
    
    print("Chào mừng bạn đến với game Đoán Số!")
    print("Tôi đã chọn một số ngẫu nhiên từ 1 đến 100. Hãy đoán thử xem!")
    
    while True:
        try:
            
            doan = int(input("Nhập số bạn đoán: "))
            so_lan_doan += 1
            
            
            if doan < so_bi_mat:
                print("Số bạn đoán quá NHỎ. Hãy thử lại!")
            elif doan > so_bi_mat:
                print("Số bạn đoán quá LỚN. Hãy thử lại!")
            else:
                print(f"Chúc mừng! Bạn đã đoán đúng số {so_bi_mat} sau {so_lan_doan} lần đoán.")
                break
        except ValueError:
            print("Vui lòng chỉ nhập một số nguyên hợp lệ!")


if __name__ == "__main__":
    choi_doan_so()
