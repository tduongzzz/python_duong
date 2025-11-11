from commom.insert_danhmuc import insert_danhmuc

while True:
    print("\n=== THÊM DANH MỤC MỚI ===")
    ten_danhmuc = input("Nhập tên danh mục: ")
    mota = input("Nhập mô tả: ")

    insert_danhmuc(ten_danhmuc, mota)

    con = input("\n👉 Nhấn 'y' để tiếp tục, hoặc phím bất kỳ để thoát: ").lower()
    if con != "y":
        print("👋 Kết thúc chương trình.")
        break
