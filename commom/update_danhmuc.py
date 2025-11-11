from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def update_danhmuc(id_danhmuc, ten_danhmuc_moi, mota_moi):
    connection = None
    cursor = None
    try:
        connection = connect_mysql()
        if connection is None:
            print("❌ Không thể kết nối đến cơ sở dữ liệu.")
            return

        cursor = connection.cursor()
        sql = "UPDATE danhmuc SET ten_danhmuc = %s, mota = %s WHERE id = %s"
        data = (ten_danhmuc_moi, mota_moi, id_danhmuc)
        cursor.execute(sql, data)
        connection.commit()

        if cursor.rowcount == 0:
            print(f"⚠️ Không tìm thấy danh mục có ID: {id_danhmuc}")
        else:
            print(f"✅ Đã cập nhật danh mục ID {id_danhmuc} thành công.")
    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
