from commom.update_danhmuc import update_danhmuc

id_danhmuc = int(input("Nhập ID danh mục cần cập nhật: "))
ten_moi = input("Nhập tên danh mục mới: ")
mota_moi = input("Nhập mô tả mới: ")

update_danhmuc(id_danhmuc, ten_moi, mota_moi)
