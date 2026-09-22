def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0:
        return " Lỗi: Không thể chia cho 0!"
    return x / y

def main():
    print(" MÁY TÍNH ")
    print("Các phép tính: +, -, *, /")
    print("Gõ 'q' tại bất kỳ bước nào để thoát.")

    while True:
        # Nhập số thứ nhất
        num1_input = input("\nNhập số thứ nhất: ").strip().lower()
        if num1_input == 'q': break
        try:
            num1 = float(num1_input)
        except ValueError:
            print(" Vui lòng nhập một số hợp lệ!")
            continue

        # Nhập phép toán
        choice = input("Nhập phép tính (+, -, *, /): ").strip()
        if choice == 'q': break
        if choice not in ['+', '-', '*', '/']:
            print("️ Phép tính không hợp lệ!")
            continue

        # Nhập số thứ hai
        num2_input = input("Nhập số thứ hai: ").strip().lower()
        if num2_input == 'q': break
        try:
            num2 = float(num2_input)
        except ValueError:
            print(" Vui lòng nhập một số hợp lệ!")
            continue

        # Thực hiện tính toán và xuất kết quả
        if choice == '+':
            print(f" Kết quả: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '-':
            print(f"️ Kết quả: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '*':
            print(f"️ Kết quả: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '/':
            print(f"️ Kết quả: {num1} / {num2} = {divide(num1, num2)}")

    print("\n Cảm ơn bạn đã sử dụng máy tính!")

if __name__ == "__main__":
    main()
